states = [
{
    "name": "Alabama",
    "capital": "Montgomery"
}, {
    "name": "Alaska",
    "capital": "Juneau"
}, {
    "name": "Arizona",
    "capital": "Phoenix"
}]


print('~~~~~~~~~~~~~~~~~~~~ \n Hello player, welcome to Bryant Cabrera\'s State Capitals Game. \n In your terminal, you will be prompted to type the capital of the state named.  Answers are case sensitive. \n For every correct answer, your correct counter goes up by 1. \n For every incorrect answer, your incorrect counter goes up by 1. \n Once all states have been cycled through, you will get a tally of how many you got correct and how many you got incorrect. \n Try to improve your score until you get all 50 correct! \n ~~~~~~~~~~~~~~~~~~~~ ')

from random import shuffle
# while len(states) > 0:
#     random_number = random.randint(0, len(states))
#     print(states[random_number])
#     states.remove(states[random_number])



randomized_states = [[states[i]] for i in range(0, len(states))]
shuffle(randomized_states)

# print(randomized_states)
for i in range(0, len(randomized_states)):
    randomized_states[i][0]['correct'] = 0
    randomized_states[i][0]['incorrect'] = 0

def startGame():
    for i in range(0, len(randomized_states)):
        print('What is the capital of ' + randomized_states[i][0]['name'] + '?')
        answer = input()
        if answer == randomized_states[i][0]['capital']:
            randomized_states[i][0]['correct'] = randomized_states[i][0]['correct'] + 1
            print(answer, ' is correct. You have gotten it correct ', randomized_states[i][0]['correct'], ' times.')
        else:
            randomized_states[i][0]['incorrect'] = randomized_states[i][0]['incorrect'] + 1
            print(answer, ' is incorrect. You have gotten it incorrect ', randomized_states[i][0]['incorrect'], ' times.')

    print('~~~~~~~~~~~~~~~~~~~~ \n That is all ', len(randomized_states), ' states.  Would you like to play again? Y/N \n ~~~~~~~~~~~~~~~~~~~~')

    continueGame = input()
    if continueGame == 'Y':
        startGame()
    else:
        print('Thank you for playing!')


startGame()