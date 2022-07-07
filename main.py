#Choose your own adventure game

#My Checklist
#3 options in one decision
#make it a bit funnier
#

#these help the game run multiple times
import time

phone = "no"
protection = "no"
game = "yes"
name=input("Enter your name: ")

#this loop start the game as long as game = yes
while game == "yes":
    time.sleep(1.2)
    print(name + ", You wake up in a cabin on a cruise ship with no memory of how you got there. ")
    time.sleep(1.2)
    print("You hear a commotion outside. ")
    time.sleep(1.2)
    print("Do you leave your cabin to check it out? ")
    time.sleep(.5)
    answer_1 = input("yes or no? ")

    if answer_1 == "yes":
        time.sleep(1.2)
        print("When you step outside you hear what sounds like shouting coming form the main deck.")
        time.sleep(1.2)
        print("Do you grab something to protect yourself? ")
    else:
        time.sleep(1.2)
        print("you close your cabin door and lock it.")
        time.sleep(1.2)
        print("You think to yourself that you need to call for help. ")
        time.sleep(1.2)
        print("You search for your phone, but realize you let it in the common room.")
        time.sleep(1.2)
        print("Do you go look for it? ")
        time.sleep(.5)  
        phone = input("yes or no? ")

        while phone == "no":
            time.sleep(1.2)
            print("are you sure? You might need it later.... ")
            time.sleep(1.2)
            print("Do you want to look for your phone")
            time.sleep(.5)
            phone = input("yes or no? ")

        time.sleep(1.2)
        print("you open the door and tiptoe into the common area. ")
        time.sleep(1.2)
        print("As you grab your phone you begin to hear shouting outside. ")
        time.sleep(1.2)
        print("Do you grab something to protect yourself? ") 

    time.sleep(.5)
    protection = input("Yes or no? ")

    if protection == "yes":
        time.sleep(1.2)
        print("You picked up your fishing rod. ")
        time.sleep(1.2) 
        print("Do you want to head towards the noise?")
    else: 
        time.sleep(1.2)
        print("This sounds like it could be dangerous, do you want to keep heading towards the noise? ")
       
        time.sleep(.5)
    answer_3 = input("yes or no? ")
    if answer_3 == "yes":
            time.sleep(1.2)
            print("you walk outside and can tell the noise is coming from the bridge.")
            time.sleep(1.2)
            print("It sounds like people are fighting. ") 
            time.sleep(1.2)
            print("Do you want to call the coast guard? ")

            time.sleep(.5)
            answer_4 = input("yes or no? ")
            if answer_4 == "yes":

                if phone == "yes" and answer_4 =="yes":
                    time.sleep(1.2)
                    print("good idea. You call the Coast Guard and wait for them to arrive. ")
                    time.sleep(1.2)
                    print("Congratulations, " + name + " you win! ")
                else:
                    time.sleep(1.2)
                    print("you try to dial for help but realize you don't have your phone. ") 
                    time.sleep(1.2)
                    print("As you're standing there a pirate walks out of the bridge and sees you ")
                    time.sleep(1.2)
                    print("He says.... 'You're coming with me... it's time to walk the plank!' ")
                    #add another question and condition here to loop it back?
            else:
                time.sleep(1.2)
                print("you slowly reach for the door and pull it open to reavel... ")
                time.sleep(1.2)
                print("A pirate hijacking the boat! ")
                time.sleep(1.2)
                print("you you want to hit him? ")
                answer_5 = input("yes or no? ")
                if answer_5 =="no":
                    time.sleep(1.2)
                    print("The Pirate hears you open the door and turns around to say:. ")
                    time.sleep(1.2)
                    print("Yaarggghhh, you're coming with me landlubber! ")
                    time.sleep(1.2)
                    print("You've been captured by the pirates! ")
                elif protection == "yes" and answer_5 == "yes":
                    print("WHACK!")
                    time.sleep(1.2)
                    print("You knocked the pirate out cold. ")
                    time.sleep(1.2)
                    print("Congrats on saving the day " + name +"!  You Win! ")
                else:
                    time.sleep(1.2)
                    print("Why would you do that? ...you don't know karate... you should have brought protection..... ")
                    time.sleep(1.2)
                    print("You slap the pirate, but it only makes him angry. ")
                    time.sleep(1.2)
                    print("He turns around and says: ")
                    time.sleep(1.2)
                    print("Arrrgghhh matey.... you're coming with me! ")
                    time.sleep(1.2)
                    print("OH NO! You've been captured by the pirates! ")

    else:
            time.sleep(1.2)
            print("you go back to your room, lock the door and call the authorities. ")
            time.sleep(1.2)
            print("Congratulations " + name + " You win! ")

    time.sleep(.5)
    game = input("Game over. Do you want to start over? ")
