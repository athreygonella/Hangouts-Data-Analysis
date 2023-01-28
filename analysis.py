
import json

try:
    file = open('Takeout/Hangouts/Hangouts.json', 'r', encoding='utf-8')
    data = json.load(file)
except FileNotFoundError:
    print('Error: Takeout/Hangouts/Hangouts.json file was not found. Please make sure that the current directory contains Takeout directory')

# Construct Map [gaia ID -> name]
ID_to_name = {}
for conversation in data['conversations']:
    participant_data = conversation['conversation']['conversation']['participant_data']

    for participant in participant_data:
        gaia_id = participant['id']['gaia_id']
        if 'fallback_name' in participant.keys():
            name = participant['fallback_name']
            # Check that name isn't an email address
            if '@' not in name:
                ID_to_name[gaia_id] = name

# Automatically determine user's name
user_ID = data['conversations'][0]['conversation']['conversation']['self_conversation_state']['self_read_state']['participant_id']['gaia_id']
user_name = ID_to_name[user_ID]

# Map [Friend Name -> # of direct messages]
messages_by_friend = {}

# Map [Group Name -> [# of messages sent by user, total # of chat messages]]
group_chat_map = {}

for conversation in data['conversations']:
    conversation_metadata = conversation['conversation']
    conversation_type = conversation_metadata['conversation']['type']

    participant_IDs = [participant['id']['gaia_id'] for participant in conversation_metadata['conversation']['participant_data']]

    events = conversation['events']

    if conversation_type == 'STICKY_ONE_TO_ONE' or len(participant_IDs) == 2:
        # Direct Message

        # Determine friend's name (None if a conversation invite from ID was never accepted)
        friend = None
        for id in participant_IDs:
            if id in ID_to_name.keys() and user_name.lower() not in ID_to_name[id].lower():
                friend = ID_to_name[id]

        if friend is not None:
            messages_by_friend[friend] = messages_by_friend.get(friend, 0) + len(events)
    
    elif conversation_type == 'GROUP':
        # Group Chat
        
        try:
            chat_name = conversation_metadata['conversation']['name']
        except KeyError:
            # (Caused by no name attribute)
            participant_names = [ID_to_name[id] if id in ID_to_name else 'Unknown User' for id in participant_IDs]
            chat_name = 'Chat with ' + ', '.join(participant_names)

        total_chat_messages = 0
        num_messages_from_user = 0
        for event in events:
            event_type = event['event_type']
            sender_id = event['sender_id']['gaia_id']
            if event_type == 'REGULAR_CHAT_MESSAGE':
                total_chat_messages += 1 
            if event_type == 'REGULAR_CHAT_MESSAGE' and sender_id in ID_to_name.keys() and user_name.lower() in ID_to_name[sender_id].lower():
                num_messages_from_user += 1

        group_chat_map[chat_name] = [num_messages_from_user, total_chat_messages]


# Sort results
sorted_messages_by_friend = dict(sorted(messages_by_friend.items(), key = lambda item: item[1], reverse=True))

sorted_group_chats_by_num_messages_from_user = dict(sorted(group_chat_map.items(), key = lambda item: item[1], reverse=True))

sorted_group_chats_by_num_total_messages = dict(sorted(group_chat_map.items(), key = lambda item: item[1][1], reverse=True))

