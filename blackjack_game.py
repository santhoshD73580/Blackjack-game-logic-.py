import random
#from art import logo



def value():
    """task as return ramdom number for list"""
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    """takes the list cards and return the value want to be changed"""
    if sum(cards)== 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user,computer):
    if user == computer:
        return "The match is drow "
    elif computer == 0 :
        return "you lose the game opponent has blackjack"
    elif user == 0:
        return "yow wins the game"
    elif user >21:
        return "you loses"
    elif computer >21:
        return "computer loses"
    elif user > computer:
        return "user wins"
    else:
        return "you lose"




def play_game():
    # start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    #print(logo)
    user = []
    computer = []
    computer_score=-1
    user_score=-1
    is_game_over= False
    for _ in range(2):
        user.append(value())
        computer.append(value())

    while not is_game_over:
        user_score= calculate_score(user)
        computer_score= calculate_score(computer)
        print(f"user card:{user},current score: {user_score}")
        print(f"computer first card: {computer[0]}")

        if user==0 or computer==0 or user_score > 21:
            is_game_over= True
        else:
            user_should_deal= input("type 'y' to get another card or 'n' to pass:").lower()
            if user_should_deal== "y":
                user.append(value())
    while computer_score !=0 or computer_score< 17:
        computer.append(value())
        computer_score= calculate_score(computer)

    print(f"your final hand :{user},final score{user_score}")
    print(f"computer final hand: {computer}, final score{computer_score}")
    print(compare(user,computer))
# print(start)
while input("do you want to play this game blackjack 'y' or 'n' ") =="y":
    print("/n"*20)
    play_game()