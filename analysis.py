# Code for processing Hangouts JSON data
# 
# Author: Athrey Gonella


import json

try:
    file = open("Takeout/Hangouts/Hangouts.json", 'r')
    data = json.load(file)
except FileNotFoundError:
    print('Takeout/Hangouts/Hangouts.json file was not found. Please make sure that the current directory contains Takeout directory')

user_name = input('Welcome to Hangouts Wrapped!! What''s your name? ')

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
            

# Map [Friend Name -> # of direct messages]
messages_by_friend = {}

for conversation in data['conversations']:
    conversation_metadata = conversation['conversation']
    conversation_type = conversation_metadata['conversation']['type']

    if conversation_type == 'STICKY_ONE_TO_ONE':
        # Direct Message

        participant_IDs = [participant['id']['gaia_id'] for participant in conversation_metadata['conversation']['participant_data']]

        # Determine friend's name (None if a conversation invite from ID was never accepted)
        friend = None
        for id in participant_IDs:
            if id in ID_to_name.keys() and user_name.lower() not in ID_to_name[id].lower():
                friend = ID_to_name[id]
        
        events = conversation['events']

        if friend is not None:
            messages_by_friend[friend] = len(events)


# Print results
sorted_messages_by_friend = dict(sorted(messages_by_friend.items(), key = lambda item: item[1], reverse=True))

print("Here are your friends ranked by # of messages: ")

for item in sorted_messages_by_friend:
    print('\n' + item + ': ' + str(sorted_messages_by_friend[item]))



