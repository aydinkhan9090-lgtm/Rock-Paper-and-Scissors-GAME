import random
print("WELCOME TO ROCK PAPER SCISSORS GAME!❤❤❤😊")
while True:
    guess = input("enter your choice rock, paper or scissors 💪🔥: ")  
    secret_sign = random.choice(["rock", "paper", "scissors"])  
    print("Computer chose:",  secret_sign)
    if guess==secret_sign:
            print("it's a tie! try again") 
    elif guess=="rock"and secret_sign=="scissors":
            print("congratulatioons!you win ")
            break
    elif guess=="paper" and secret_sign=="rock":
            print("congratulatioons!you win ")
            break
    elif guess=="scissors" and secret_sign=="paper":
            print("congratulatioons!you win")
            break 
    else:
        print("you lose! 😢 try again!")  
        

            # THANKS FOR PLAYING THIS GAME!😊😘😆💋💋👏💋💋💕🙌😘👌

        
        
        
        
        
        
    
        
    


   
     