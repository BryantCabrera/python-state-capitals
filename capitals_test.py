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
for i in range(0, len(states)):
    print(states[i]['name'])