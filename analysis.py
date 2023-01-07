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

# Map [Friend Name -> # of direct messages]
messages_by_friend = {}

for conversation in data['conversations']:
    conversation_metadata = conversation['conversation']
    conversation_type = conversation_metadata['conversation']['type']

    if conversation_type == 'STICKY_ONE_TO_ONE':
        # Direct Message

        participant_names = [participant['fallback_name'] for participant in conversation_metadata['conversation']['participant_data'] if 'fallback_name' in participant.keys()]

        friend = next((name for name in participant_names if user_name not in name), None)

        events = conversation['events']

        if friend is not None:
            messages_by_friend[friend] = len(events)


# Print results
sorted_messages_by_friend = dict(sorted(messages_by_friend.items(), key = lambda item: item[1], reverse=True))

print("Here are your friends ranked by # of messages: ")

for item in sorted_messages_by_friend:
    print('\n' + item + ': ' + str(sorted_messages_by_friend[item]))



