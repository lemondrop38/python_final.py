# LM IG SB VC 6th Team Game
# Display the game


def welcome(info):
      return float(input(f"What is your {info}"))#function

name = input("What is your name?")#variable
age = input("How old are you?")#variable
play = input("Would you like to play a game?(0 means no, 1 means yes)")

if play == "1":
      print(f"Good Morning", (name),". Your birthday's today. Happy Birthday, you are", (age),"years old! You just woke up in a cabin in the middle of the woods, and you dont know where you are. You either...") # Lily (background of story)
      question1 = input("Look around or try to escape...(2 means look around, 3 means try to escape)") # sophia (options of what to do)
      if question1 == "2":
            print("As you look around you find a birthday card and keys in a desk drawer. You open the card and is says Happy Birthday,", (name),"!") #sophia (choose where to go)
            question3 = input("You see a door you try to open it and its locked, you remember you have a key and you open it. You close the door behind you and you see a bear coming at you. You try to go back inside but the door is now stuck. Do you run or stay and fight the bear?(6 means run 7 means fight)") # sophia 
            if question3 == "6":
                  print("You run then end up tripping on a log and now you can't do anything else because your hurt. You lost!")  # sophia(explaination of ending 1)
                  SystemExit
            elif question3 == "7":
                  print("You stayed to fight, very brave. Why did you do that though? You never stood chance, and now you're dead. You lost!") # Lily/ Victoria (explaination of ending 2)
                  SystemExit
      elif question1 == "3":
            print("You see a way out through a window. You grab a nearby rock and throw it at the window then climb out. ") # Lily (option of what to do)
            question2 = input("You're outside and hear water.(4 means go towards the water 5 means go in the oppisite direction)") #isabella german (choose where to go)
            if question2 == "4":
                  print("You start to walk towords the water and find a river. Along the river is your house where you see a birthday banner with",name,"on it.") # lily/isabella (explaination to ending 3)
                  friends = ["Sekora Delora", "Billy Bob Joe", "Al O'Vera","Marsha Mellow"]
                  for friends in friends:
                        print(f"Congtatulations! You got back to your party, and {friends} is there.")#isabella/Lily/sophia
            elif question2 == "5":
                  print("You start walking in the oppisite direction you, you see people at a campsite and ask for help. They help you get back home. The end!")#Victoria Cisneros (explaination of ending 4)
            
elif play == "0":
      print("Okay, have a good day!") # victoria(you didn't want to play)
#isabella german the greeting and introduction