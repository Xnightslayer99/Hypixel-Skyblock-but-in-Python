import random
gameworks = 1
coins = 0
eyes = 0
stats = 1001
xp = 20
souls = 0
while(gameworks==1):
   A = input("what do you want to do?")
   B = random.randint(1,1)
   if A == "d":
      print("nice?")
      if B == 1:
         print("you found a fairy soul colect 5 and give them to tia to get a stat boost")
         print("there is a command called tia")
         souls=souls+1
   elif A =="tia":
      C = input("would you like to claim your fairy souls?")
      if C == "yes":
         if souls<5:
            print("you need", 5-souls, "to claim your souls.")
      if C == "yes":
         if souls>=5:
            print("thank you, you now have a permanent stat boost")
            stats=stats+6
            souls=souls-5
      if C == "no":
         print("Ok come again.")
      
