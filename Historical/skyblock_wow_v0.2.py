import random
import time
gameworks = 1
coins = 0
stats = 0
haswatch = 0
xp = 20
fibsh = 0
time = 0
eyes = 0
souls = 0
cxp = 0
csl = 0
cm = 1
sm=1
cslxp = 1
fslxp = 1
fcm = 1
fsm = 1
fsl = 0
fxp = 0
fslm = 1
print("Join the testing discord server for updates and some info!https://discord.gg/Sn2A36M")
while(gameworks==1):
   fxpg = (12*fslm)
   A = input("What action do you want to do?")
   J = random.randint(1,1000)
   if A == "check balance":
       print(coins)
       time=time+1
   elif A == "+100 strength":
      stats = stats+100
      time=time+1
   elif A == "check stats":
       print(stats)
       time=time+1
   elif A == "forage":
       C = random.randint(1,10)
       print("you break a tree")
       if C == 7:
           print("+1 strength")
           stats = stats+1
           time=time+1
   elif A == "catch fibsh":
      print("you catch fibsh")
      fibsh = fibsh+(10*fslm)
      time=time+1
      fxp=fxp+fxpg
   elif A == "eat fibsh":
      print("you ate", fibsh, "fibsh")
      fibsh = 0
      time=time+1
   elif A == "+100 time":
      time=time+100
   elif A == "check time":
      print(time)
   elif A == "explore":
       X = random.randint(1,5)
       if X == 1:
           print("you stumble upon wheat and get 7 coins")
           coins = coins+7
           time=time+1
       if X == 2:
           if stats>1:
               print("you found a zombie and killed it, you got 9 coins")
               coins = coins+9
               stats = stats+1
               time=time+1
               cxp=cxp+5
           else:
               print("""you found and zombie and it killed you, you die, L
you also lose half of your coins, what a noob""")
               coins = coins/2
               time=time+1
       if X == 3:
           print("you stumble upon a tree and break it, +1 stats and +2 coins")
           stats = stats+1
           coins = coins+1
           time=time+1
       if X == 4:
           if stats>20:
               print("you fight an enderman and kill it, +70 coins and +5 strength")
               stats=stats+5
               coins=coins+70
               time=time+1
           else:
               print("you find an enderman and try to fight it")
               print("you are not strong enough and almost die but you get lucky")
               print("someone comes and kills it so you survive")
               time=time+1
       if X == 5:
          print("you find a mine and collect ores, then some weird enemy appears")
          if stats>100:
             print("you kill it and it drops a weird watch, you decide to keep it")
             haswatch=haswatch+1
             time=time+1
             cxp=cxp+20
          else:
             print("you quickly realize that you can't fight it and decide to run away")
             time=time+1
   elif A == "fight":
           G = random.randint(1,2)
           if G == 1:
              print("you find a random zombie")
              if stats>=150:
                 print("you kill it and gain some coins, +5 coins, +5 strength")
                 coins=coins+5
                 stats=stats+5
                 time=time+1
                 cxp=cxp+35
              if stats<150:
                    print("you died and lost half your coins")
                    coins=coins/2
                    time=time+1
           if G == 2:
               print("you find a spider and fight it")
               if stats>=160:
                  print("you kill it, +6 coins, +6 strength")
                  coins=coins+6
                  stats=stats+6
                  time=time+1
                  cxp=cxp+12
               if stats<160:
                  print("you died L you lost half your coins")
                  coins=coins/2
                  time=time+1
   if cxp == 1000:
      print("you leveled up your combat to lvl 1 gratz and gained 10k coins")
      coins=coins+10000
      stats=stats+100
      csl=csl+1
      print("Next combat level is at 2000 combat xp")
   if cxp == (csl+1)*1000:
      csl=csl+1
      print("you leveled up your combat to lvl", csl, "gratz and gained", 10*cm, "k coins")
      coins=coins+(10000*sm)
      stats=stats+(100*sm)
      print("Next combat level is at", (csl+1)*1000, "combat xp")
   if (csl*cslxp) == (10*cslxp):
      cslxp=cslxp+1
      sm=sm+1
      cm=cm+1
   if A == "check coin multiplier":
      print(cm)
   if A == "check stat multiplier":
      print(sm)
   if A == "check combat lvl":
      print(csl)
   if cm == 3:
      if (cxp*cslxp) == (10000*cslxp):
         cm=cm-2
   if fxp == 1000:
      print("you leveled up your fibsh skill to lvl 1 gratz and gained 10k coins")
      coins=coins+10000
      stats=stats+100
      csl=csl+1
      print("Next combat level is at 2000 fibshing xp")
   if fxp == (fsl+1)*1000:
      fsl=fsl+1
      print("you leveled up your fibshing to lvl", fsl, "gratz and gained", 10*fcm, "k coins")
      coins=coins+(10000*fsm)
      stats=stats+(100*fsm)
      print("Next fibshing level is at", (fsl+1)*1000, "fibshing xp")
   if (fsl*fslxp) == (10*fslxp):
      fslxp=fslxp+1
      fsm=fsm+1
      fcm=fcm+1
      fslm=fslm+0.5
   if A == "check fibsh coin multiplier":
      print(fcm)
   if A == "check fibsh stat multiplier":
      print(fsm)
   if A == "check fibsh lvl":
      print(fsl)
   if fcm == 3:
      if (fxp*fslxp) == (10000*fslxp):
         fcm=fcm-2
   if A == "grind eyes":
          print("you stumble upon a portal")
          if stats>=1000:
             D = random.randint(1,420)
             if D == 420: 
               print("you decide to enter it, you find an enderman with a portal frame and kill it, you get a summoning eye")
               stats=stats+1
               coins=coins+15
               B = input("do you want to sell the eye?")
               if B == "yes":
                  print("Ok I'll pay 600k coins")
                  coins=coins+600000
               if B == "no":
                  print("ok")
                  eyes=eyes+1
                  xp = xp+2
             else:
                print("you enter the portal and find a Zealot, you kill it")
                xp = xp+1
                coins=coins+15
                cxp=cxp+60
                time=time+1
          else:
             print("A strange force prevents you from entering it")
   elif A == "summon drag":
      if eyes>=8:
         C = input("are you sure?")
         if C == "yes":
            print("ok you'll summon a dragon")
            eyes=eyes-8
            E = random.randint(1,7)
         if C == "no":
            print("ok have a good day")
         if E == 1:
            print("you summoned a young dragon")
         if E == 2:
            print("you summoned a old dragon")
            print("F in the chat")
         if E == 3:
            print("you summoned a wise dragon")
         if E == 4:
            print("you summoned a protector dragon")
            print("F in the chat")
         if E == 5:
            print("you summoned a strong dragon")
         if E == 6:
            print("you summoned a unstable dragon")
         if E == 7:
            print("you summoned a superior dragon")
   elif A == "eye count":
      print(eyes)
   elif A == "tia":
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
   if J == 1000:
      print("you found a fairy soul colect 5 and give them to tia to get a stat boost")
      print("there is a command called tia")
      souls=souls+1
   elif A == "dark auction":
      M = random.randint(1,12)
      if M == 1:
         print("We have a midas sword up")
         print("would you like to purchace it?")
         A = input("What is your answer?")
         if A == "yes":
            print("Very well that will be 50mil for the sword")
         if A == "no":
            print("Very well Come back soon")
         if A == "yes":
            B = input("are you sure?")
            if B == "yes":
               coins=coins-50000000
               stats=stats+50000
               time=time+1
      if M == 2:
         print("We have a Spirit mask up")
         print("would you like to purchase it?")
         A = input("What is your answer?")
         if A == "yes":
           print("Very well that will be 1k for the Spirit mask ")
         if A == "no":
                print("Very well Come back soon")
         if A == "yes":
            B = input("are you sure?")
            if B == "yes":
               coins=coins-1000
               stats=stats*1.2
               time=time+1
      if M == 3:
         print("We have a Ender Artifact up")
         print("would you like to purchase it?")
         A = input("What is your answer?")
         if A == "yes":
              print("Very well that will be 10mil for the Ender Artifact")
         if A == "no":
                  print("Very well Come back soon")
         if A == "yes":
            B = input("are you sure?")
            if B == "yes":
               coins=coins-10000000
               stats=stats+100
               time=time+1
      if M == 4:
         print("We have a Wither artifact up")
         print("would you like to purchase it?")
         A = input("What is your answer?")
         if A == "yes":
        	 print("Very well that will be 12mil for the wither artifact")
         if A == "no":
             print("Very well Come back soon")
         if A == "yes":
            B = input("are you sure?")
            if B == "yes":
               coins=coins-12000000
               stats=stats+100
               time=time+1
      if M == 5:
         print("We have a Parrot Pet for sale")
         print("would you like to purchase him/her?")
         A = input("What is your answer?")
         if A == "yes":
            print("Very well that will be 7.5mil for the Pet Parrot")
         if A == "no":
            print("Very well Come back soon")
         if A == "yes":
            B = input("are you sure?")
            if B == "yes":
               coins=coins-7500000
               stats=stats+10000
               time=time+1
      if M == 6:
         print("We have a Turtle Pet for sale")
         print("would you like to purchase him/her?")
         A = input("What is your answer?")
         if A == "yes":
            print("Very well that will be 20mil for the Pet Turtle")
         if A == "no":
            print("Very well Come back soon")
         if A == "yes":
            B = input("are you sure?")
            if B == "yes":
               coins=coins-20000000
               stats=stats+10000
               time=time+1
      if M == 7:
         print("We have a Jellyfish Pet for sale")
         print("would you like to purchase him/her?")
         A = input("What is your answer?")
         if A == "yes":
            print("Very well that will be 20.5mil for the Pet Jellyfish")
         if A == "no":
          print("Very well Come back soon")
         if A == "yes":
            B = input("are you sure?")
            if B == "yes":
               coins=coins-20500000
               stats=stats+10000
               time=time+1
      if M == 8:
         print("We have a Sharp VI book for sale")
         print("would you like to purchase it?")
         A = input("What is your answer?")
         if A == "yes":
            print("Very well that will be 9mil for the sharp 6 book")
         if A == "no":
            print("Very well Come back soon")
         if A == "yes":
            B = input("are you sure?")
            if B == "yes":
               coins=coins-9000000
               stats=stats+1000
               time=time+1
      if M == 9:
         print("We have a Giant slayer VI book for sale")
         print("would you like to purchase it?")
         A = input("What is your answer?")
         if A == "yes":
            print("Very well that will be 6mil for the Giant killer 6 book")
         if A == "no":
            print("Very well Come back soon")
         if A == "yes":
            B = input("are you sure?")
            if B == "yes":
               coins=coins-6000000
               stats=stats+1000
               time=time+1
      if M == 10:
         print("We have a Prot VI book for sale")
         print("would you like to purchase it?")
         A = input("What is your answer?")
         if A == "yes":
            print("Very well that will be 3mil for the Prot 6 book")
         if A == "no":
            print("Very well Come back soon")
         if A == "yes":
            B = input("are you sure?")
            if B == "yes":
               coins=coins-3000000
               stats=stats+1000
               time=time+1
      if M == 11:
         print("We have a Growth VI book for sale")
         print("would you like to purchase it?")
         A = input("What is your answer?")
         if A == "yes":
            print("Very well that will be 3mil for the Growth 6 book")
         if A == "no":
            print("Very well Come back soon")
         if A == "yes":
            B = input("are you sure?")
            if B == "yes":
               coins=coins-3000000
               stats=stats+1000
               time=time+1
      if M == 12:
         print("We have a Power VI book for sale")
         print("would you like to purchase it?")
         A = input("What is your answer?")
         if A == "yes":
            print("Very well that will be 9mil for the Power 6 book")
         if A == "no":
            print("Very well Come back soon")
         if A == "yes":
            B = input("are you sure?")
            if B == "yes":
               coins=coins-9000000
               stats=stats+1000
               time=time+1
      if coins < 0:
         print("no more game for u")
         C = input("what do you say bout that?")
         if C == "/":
            print("no more game for u now")
            gameworks=0
         else:
            gameworks=0
   if time == 100:
               print("oringo has come")
               C = input("will you go to oringo?")
               if C == "yes":
                   print("hello I am Oringo I travel around the world colecting pets.")
                   D = input(" would you like to buy one of the pets i have colected?")
                   if D == "yes":
                       print("wonderful I have only 1 pet at the moment sorry.")
                       print("(dev note:I will try add more pets to oringo as in instead of 1 there wil be 3.)")
                       E = random.randint(1,6)
                       if E == 1:
                           F = random.randint(1,5)
                           if F == 1:
                               G = "common"
                           if F == 2:
                               G = "uncommon"
                           if F == 3:
                               G = "rare"
                           if F == 4:
                               G = "epic"
                           if F == 5:
                               G = "legendary"
                               print("I have a", G, "blue whale pet for sale.")
                               A = input("What is your answer?")
                               if A == "yes":
                                   if F == 1:
                                       print("Very well that will be 10k for the Common blue whale pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-10000
                                               stats=stats+10
                                   if F == 2:
                                       print("Very well that will be 25k for the Uncommon blue whale pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-25000
                                               stats=stats+100
                                   if F == 3:
                                       print("Very well that will be 100k for the rare blue whale pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-100000
                                               stats=stats+1000
                                   if F == 4:
                                       print("Very well that will be 1mil for the epic blue whale pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-1000000
                                               stats=stats+10000
                                   if F == 5:
                                       print("Very well that will be 10mil for the legendary blue whale pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-10000000
                                               stats=stats+100000
                                   if A == "no":
                                       print("Very well. Next time I will try to satisfy you.")
                    
                       if E == 2:
                           F = random.randint(1,5)
                           if F == 1:
                               G = "common"
                           if F == 2:
                               G = "uncommon"
                           if F == 3:
                               G = "rare"
                           if F == 4:
                               G = "epic"
                           if F == 5:
                               G = "legendary"
                               print("I have a", G, "lion pet for sale.")
                               A = input("What is your answer?")
                               if A == "yes":
                                   if F == 1:
                                       print("Very well that will be 10k for the Common lion pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-10000
                                               stats=stats+10
                                   if F == 2:
                                       print("Very well that will be 25k for the Uncommon lion pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-25000
                                               stats=stats+100
                                   if F == 3:
                                       print("Very well that will be 100k for the rare lion pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-100000
                                               stats=stats+1000
                                   if F == 4:
                                       print("Very well that will be 1mil for the epic lion pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-1000000
                                               stats=stats+10000
                                   if F == 5:
                                       print("Very well that will be 15mil for the legendary lion pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-15000000
                                               stats=stats+100000
                                   if A == "no":
                                       print("Very well. Next time I will try to satisfy you.")
                       if E == 3:
                           F = random.randint(1,5)
                           if F == 1:
                               G = "common"
                           if F == 2:
                               G = "uncommon"
                           if F == 3:
                               G = "rare"
                           if F == 4:
                               G = "epic"
                           if F == 5:
                               G = "legendary"
                               print("I have a", G, "tiger pet for sale.")
                               A = input("What is your answer?")
                               if A == "yes":
                                   if F == 1:
                                       print("Very well that will be 10k for the Common tiger pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-10000
                                               stats=stats+10
                                   if F == 2:
                                       print("Very well that will be 25k for the Uncommon tiger pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-25000
                                               stats=stats+100
                                   if F == 3:
                                       print("Very well that will be 100k for the rare tiger pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                                coins=coins-100000
                                                stats=stats+1000
                                   if F == 4:
                                       print("Very well that will be 1mil for the epic tiger pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-1000000
                                               stats=stats+10000
                                   if F == 5:
                                       print("Very well that will be 15mil for the legendary tiger pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-15000000
                                               stats=stats+100000
                                   if A == "no":
                                       print("Very well. Next time I will try to satisfy you.")
                       if E == 4:
                           F = random.randint(1,5)
                           if F == 1:
                              G = "common"
                           if F == 2:
                              G = "uncommon"
                           if F == 3:
                              G = "rare"
                           if F == 4:
                              G = "epic"
                           if F == 5:
                              G = "legendary"
                              print("I have a", G, "giraffe pet for sale.")
                              A = input("What is your answer?")
                              if A == "yes":
                                    if F == 1:
                                       print("Very well that will be 10k for the Common giraffe pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-10000
                                               stats=stats+10
                                    if F == 2:
                                       print("Very well that will be 25k for the Uncommon giraffe pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-25000
                                               stats=stats+100
                                    if F == 3:
                                       print("Very well that will be 100k for the rare giraffe pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-100000
                                               stats=stats+1000
                                    if F == 4:
                                       print("Very well that will be 1mil for the epic giraffe pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-1000000
                                               stats=stats+10000
                                    if F == 5:
                                       print("Very well that will be 10mil for the legendary giraffe pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-10000000
                                               stats=stats+100000
                                    if A == "no":
                                       print("Very well. Next time I will try to satisfy you.")
                       if E == 5:
                           F = random.randint(1,5)
                           if F == 1:
                               G = "common"
                           if F == 2:
                               G = "uncommon"
                           if F == 3:
                               G = "rare"
                           if F == 4:
                               G = "epic"
                           if F == 5:
                               G = "legendary"
                               print("I have a", G, "elephant pet for sale.")
                               A = input("What is your answer?")
                               if A == "yes":
                                   if F == 1:
                                       print("Very well that will be 10k for the Common elephant pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-10000
                                               stats=stats+10
                                   if F == 2:
                                       print("Very well that will be 25k for the Uncommon elephant pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-25000
                                               stats=stats+100
                                   if F == 3:
                                       print("Very well that will be 100k for the rare elephant pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-100000
                                               stats=stats+1000
                                   if F == 4:
                                       print("Very well that will be 1mil for the epic elephant pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-1000000
                                               stats=stats+10000
                                   if F == 5:
                                       print("Very well that will be 15mil for the legendary elephant pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-15000000
                                               stats=stats+100000
                                   if A == "no":
                                       print("Very well. Next time I will try to satisfy you.")
                       if E == 6:
                            F = random.randint(1,5)
                            if F == 1:
                               G = "common"
                            if F == 2:
                               G = "uncommon"
                            if F == 3:
                               G = "rare"
                            if F == 4:
                               G = "epic"
                            if F == 5:
                               G = "legendary"
                            print("I have a", G, "monkey pet for sale.")
                            A = input("What is your answer?")
                            if A == "yes":
                                   if F == 1:
                                       print("Very well that will be 10k for the Common monkey pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-10000
                                               stats=stats+10
                                   if F == 2:
                                       print("Very well that will be 25k for the Uncommon monkey pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-25000
                                               stats=stats+100
                                   if F == 3:
                                       print("Very well that will be 100k for the rare monkey pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-100000
                                               stats=stats+1000
                                   if F == 4:
                                       print("Very well that will be 1mil for the epic monkey pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-1000000
                                               stats=stats+10000
                                   if F == 5:
                                       print("Very well that will be 18mil for the legendary monkey pet")
                                       if A == "yes":
                                           B = input("are you sure?")
                                           if B == "yes":
                                               coins=coins-18000000
                                               stats=stats+100000
                                   if A == "no":
                                       print("Very well. Next time I will try to satisfy you.")
               time=0      
   if eyes<0:   
      gameworks=0
   if souls<0:
      gameworks=0
else:
   print("This action does not exist")
   time=time+1
   if haswatch>0:
      stats=stats+haswatch
