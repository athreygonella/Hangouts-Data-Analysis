
import analysis

first_name = analysis.user_name.split()[0]        

def displayRankedFriends():
    print('\nHi ' + first_name + '! Here are your top friends, ranked by # of direct messages: \n')
    print('************************************************************')
    print('************************************************************', end='')

    count = 1
    for item in analysis.sorted_messages_by_friend:
        print('\n' + str(count) + '. ' + item + ': ' + str(analysis.sorted_messages_by_friend[item]))
        if count == 5:
            print('************************************************************')
            print('************************************************************')
            input('Press Enter to show full rankings: ')
        count += 1

def displayRankedGroupChatsByInvolvement():
    print('\nHi ' + first_name + '! Here are the top 10 group chats that you\'ve been most involved in: \n')
    print('************************************************************')
    print('************************************************************', end='')

    count = 1
    for item in analysis.sorted_group_chats_by_num_messages_from_user:
        print('\n' + str(count) + '. You\'ve sent ' + str(analysis.sorted_group_chats_by_num_messages_from_user[item][0]) + ' messages in ' + item)
        if count == 10:
            print('************************************************************')
            print('************************************************************')
            break
        count += 1

def displayRankedGroupChatsByTotalMessages():
    print('\nHi ' + first_name + '! Here are the top 10 most active group chats that you\'re in: \n')
    print('************************************************************')
    print('************************************************************', end='')

    count = 1
    for item in analysis.sorted_group_chats_by_num_total_messages:
        print('\n' + str(count) + '. ' + str(analysis.sorted_group_chats_by_num_total_messages[item][1]) + ' total messages in ' + item)
        if count == 10:
            print('************************************************************')
            print('************************************************************')
            break
        count += 1

def showMenu():
    print('\n\nMenu')
    print('[1] View ranking of friends by # of DMs you have with them.')
    print('[2] View top 10 group chats that you\'ve been most active in')
    print('[3] View top 10 group chats by total # of messages')
    print('[q] Quit')
    choice = input('\nPlease select from the options in the menu above: ')
    while not (choice == str(1) or choice == str(2) or choice == str(3) or choice.lower() == 'q'):
        choice = input('\nPlease select from the options in the menu above: ')
    if choice == str(1):
        displayRankedFriends()
        showMenu()
    elif choice == str(2):
        displayRankedGroupChatsByInvolvement()
        showMenu()
    elif choice == str(3):
        displayRankedGroupChatsByTotalMessages()
        showMenu()
    else:
        print("quitting program...")
        exit()
            
print('\n\nWelcome to Hangouts Wrapped, ' + analysis.user_name + '!!')
showMenu()

