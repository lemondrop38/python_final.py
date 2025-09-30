# LM IG SB VC 6th Build A Game.


# Display the game

def welcome(info):
      return float(input(f"What is your {info}"))#function


name = input("What is your name?")#variable
age = input("How old are you?")#variable
play = input("would you like to play a game?(0 means no, 1 means yes)")

if play == "1":
     print(f"Good Morning", (name),". Your birthday's today. Happy Birthday, you are", (age),"years old! You just woke up in a cabin in the middle of the woods, and you dont know where you are. You either...") # Lily
     question1 = input("look around or try to escape...(2 means look around, 3 means try to escape)") # sophia question

if question1 == "2":
print("You find a birthday card and keys in a desk drawer. You open the card and is says Happy Birthday,", (name),"!") #sophia

question3 = input("You see a door you try to open it and its locked, you remember you have a key and you open it. You close the door behind you and you see a bear coming at you. You try to go back inside but the door is now stuck. Do you run or stay and fight the bear?(6 means run 7 means fight)") # sophia 

if question3 == "6":
      print("You run then end up tripping on a log and now you can't do anything else because your hurt. You lost!")  # sophia
elif question3 == "7":
      print("You stayed to fight, very brave. Why did you do that though? You never stood chance, and now you're dead. You lost!") # Lily
      
      
elif question1 == "3":
      print("You see a way out through a window. You grab a rock and throw it at the window then climb out. ") # Lily 
      question2 = input("You're outside and hear water.(4 means go twords the water 5 means go in the oppisite direction)") #isabella german

      if question2 == "4":
            print("You start to walk towords the water and then 10 minutes later you find a river! you start to walk along side the river and you find a beach! you keep on walking for a couple hours and suddenly come across a couple on the beach(8 means go up to them 9 means ignore them)") #isabella german
      
      elif question2 == "8":
            print("You go up to them and they help you find your way home") #isabella german
            friends = ["Sekora Delora", "Billy Bob Joe", "Al O'Vera","Marsha Mellow"]
            
            for friends in friends:
                  print(f"You see {friends} at your birthday party!") #sophia
                  print("Mission complete: you got back to your party!")#isabella

      elif question2 == "9": 
            print("They ask you if you need help, you say yes and they help you get back home to your party!")#isabella german
            friends = ["Sekora Delora", "Billy Bob Joe", "Al O'Vera","Marsha Mellow"]
            
            for friends in friends:
                  print(f"You see {friends} at your birthday party!") #sophia
                  print("Mission complete: you got back to your party!")#isabella
      elif question2 == "5":
            print("You start walking in the oppisite direction you, you see a campsite(10 means steal some of the campers belongings 11 means stay and wait for the campers to return and ask for help) .")#Victoria Cisneros
      elif question2 == "10":
            print("You look through their belongings and find a phone you call 911 and ask them for help, they find you and they take you home to your birthday party")#Victoria Cisneros 

      elif question2 == "11":
            print("You patiently wait for the campers to come back and then you ask them for help and they take you home")#victoria cisneros 

      elif play == "0":
            print("Okay, have a good day!")
#isabella german the greeting and introduction