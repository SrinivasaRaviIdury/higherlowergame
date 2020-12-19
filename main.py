#refrence:https://repl.it/@appbrewery/higher-lower-final?embed=1&output=1#main.py
#Todo List:
#display Logo
from replit import clear
def compare_users(opt1,opt2):
    if opt1['follower_count']>opt2['follower_count']:
        return 'a'
    else:
        return 'b'
import art
print(art.logo)
#select A from list of dict with description
import game_data
import random
def random_data():
    return random.randint(0,49)
score = 0
flag = 1
def random_ab():
    return game_data.data[random_data()]
a,b = random_ab(),random_ab()

while flag:

    print(f"Compare A: {a['name']},a {a['description']},from {a['country']}")
    #display vs symbol
    print(art.vs)
    #select B from list of dict with description
    # print(b['name','description','country'])
    
    print(f"Aganist B: {b['name']},a {b['description']},from {b['country']}")
    #ask user to type 'a' or 'b' who has more followers

    user_choice = input("Guess Who has more followers type 'A' or 'B' : ").lower()
    #check who has more followers a or b compare a and b followers
    high_followers = compare_users(a,b)
    if high_followers == 'b':
        a=b
    #if user guesses correct change b to a 
    if user_choice == high_followers:
        print("you are correct")
        #increase the score of user
        score +=1
        #again show a vs b 
        b = random_ab()
        clear()
    else:
        #if user is incorrect display that's wrong Final score X 
        print(f"Sorry, that's wrong. Final score {score}")
        flag = 0



