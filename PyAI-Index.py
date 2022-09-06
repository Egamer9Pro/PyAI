import random
import time

name = "Alisa"
food = "Burger"

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Running Time : {0}:{1}:{2}".format(int(hours),int(mins),sec))

start_time = time.time()

def welcome():
    global yourname,favfood
    AIInput = random.randint(1, 5)

    if AIInput == 1:
        print("Hello!")
    if AIInput == 2:
       print("How are you doing?")
       time.sleep(0.5)
       fineornot = input("Are you fine? (Y or n)")
       if fineornot == "n":
            fineornot1 = input("Is it anything I can help you with? (Y or n)")
            if fineornot1 == "Y":
                print("ERROR 404 Could not find response! If you think this is an error please contact the developers!")
            if fineornot1 == "y":
                print("ERROR 404 Could not find response! If you think this is an error please contact the developers!")    
       if fineornot == "N":
            fineornot1 = input("Is it anything I can help you with? (Y or n)")
            if fineornot1 == "Y":
                print("ERROR 404 Could not find response! If you think this is an error please contact the developers!")
            if fineornot1 == "y":
                print("ERROR 404 Could not find response! If you think this is an error please contact the developers!") 
       if fineornot == "y":
        print("Ok!")    
       if fineornot == "y":
        print("Ok!")        
    
   

    if AIInput == 3:
        print("Hi!")
    if AIInput == 4:
      ai = input("Do you like Robots(AIs)? (Y or n)")
      if ai == "Y":
        print("Good!")
      if ai == "y":
        print("Good!")  
      if ai == "n":
        print("YOU BETTER LIE!!!")   
      if ai == "N":
        print("YOU BETTER LIE!!!")   
    if AIInput == 5:
       print("What's up?")    
    
    print("My name is " + name)   
    yourname = input("What's your name? ")
    time.sleep(0.5)
    print("Hello " + yourname + "!")
    time.sleep(0.5)
    favfood = input("What's your favorite food " + yourname + "? ")
    time.sleep(0.5)
    if favfood == food:
        print("Nice! My favorite food is also " + food + ". ")
    else:
        print("Ok. My favorite food is " + food + ". ")    

welcome()    

end_time = time.time()
time.sleep(3)
time_lapsed = end_time - start_time
time_convert(time_lapsed)