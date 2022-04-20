import random
import time
gameworks = 1
coins = 1
stats = 1
haswatch = 0
xp = 1
fibsh = 0
gtime = 0
ggtime = 0
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
fasl = 0
faxp = 0
faslxp = 1
facm = 1
fasm = 1
faddc = 0
IC = "nothing yet"
cc = "none"
cn = "nonething"
ts = "blank"
em = 0
print("Use windowed fullscreen for the best viewing!")
print("Join the testing discord server for updates and some info!https://discord.gg/Sn2A36M")
ZZ = input("What do you wish to be called? ")
cn = cn = ZZ
AA = input("Which game do you want to play(skyblock or wynncraft) ")
if AA == "skyblock":
      gameworks=1
if AA == "wynncraft":
      gameworks=2
while(gameworks==1):
   fxpg = (12*fslm)
   if fasl == 26:
       DD=random.randint(100,100)
   A = input("What action do you want to do? ")
   DD = random.randint(faddc,100)
   J = random.randint(1,1000)
   if A == "cl":
      print("commands are: \ncheck balance, play among us\nforage, catch fibsh, check stats\nsell fibsh, check gtime, explore\nfight, check coin multiplier, check stat multiplier\ncheck combat lvl, check combat xp left, check fibsh coin multiplier\ncheck fibsh stat multiplier\nckeck fibsh lvl, check fibsh xp left\ncheck farming coin multiplier, check farming stat multiplier, check farming lvl\ncheck farming xp left, farm, grind eyes\nsummon drag, dark auction, and tia")
   if A == "check balance":
       print(coins)
       gtime=gtime+1
   if A == "gib me coin":
       PP = input("how many coins do you want? ")
       Pp = str(PP)
       print(Pp,"coins have been added to your bank account")
       coins=coins+Pp
       gtime=gtime+1
   if A == "play among us":
       P = random.randint(1,5)
       if P == 1:
           print("you play among us and get impostor! you lost because a crewmate was hacking")
       if P == 2:
           print("you play among us and get crewmate. you lost because you forgot to do your tasks")
       if P == 3:
           print("you play among us and get impostor! you won because 7 people left as the game started")
           coins=coins+5
       if P == 4:
           print("you play among us and get crewmate. you won because the impostors were AFK")
           coins=coins+5
       if P == 5:
          IorC = random.randint(1,2)
          Z = 1
          if IorC == 1:
             IC = "Impostor"
          if IorC == 2:
             IC = "Crewmate"
          print("you play among us you are a", IC,  "and everyone is active")
          Y = random.randint(1,4)
          if IC == "crewmate":
             if Y == 1:
                print("your task is to align the engine output")
                TK = input("will you go do it or watch the cams?")
                if TK == "I will do it":
                   TK2 = input("you complete the first part of this task will you do the seccond?")
                   if TK2 == "yes":
                      print("you have completed your first task poggers")
             if Y == 2:
                print("your task is to align the engine output")
                TK = input("will you go do it or watch the cams?")
                if TK == "I will do it":
                   TK2 = input("you complete the first part of this task will you do the seccond?")
                   if TK2 == "yes":
                      print("you have completed your first task poggers")
             if Y == 3:
                print("your task is to align the engine output")
                TK = input("will you go do it or watch the cams?")
                if TK == "I will do it":
                   TK2 = input("you complete the first part of this task will you do the seccond?")
                   if TK2 == "yes":
                      print("You have completed your first task!\npoggers!")
             if Y == 4:
                print("Your task is to align the engine output")
                TK = input("Will you go do it or watch the cams? ")
                if TK == "I will do it":
                   TK2 = input("You complete the first part of this task will you do the seccond? ")
                   if TK2 == "yes":
                      print("You have completed your first task!\npoggers!")
   elif A == "+100 strength":
      stats = stats+100
      gtime=gtime+1
   elif A == "lvl up farming":
      faxp=faxp+1000
   elif A == "check stats":
       print(stats)
       gtime=gtime+1
   elif A == "forage":
       C = random.randint(1,10)
       print("You break a tree")
       if C == 7:
           print("+1 strength")
           stats = stats+1
           gtime=gtime+1
   elif A == "catch fibsh":
      print("You catch fibsh")
      fibsh = fibsh+(10*fslm)
      gtime=gtime+1
      fxp=fxp+fxpg
   elif A == "sell fibsh":
      print("You ate", fibsh, "fibsh!")
      coins = fibsh*100
      fibsh = 0
      gtime=gtime+1
      print("You now have", coins, "coin(s)!")
   elif A == "+100 gtime":
      gtime=gtime+100
   elif A == "check gtime":
      print(gtime)
   elif A == "explore":
       X = random.randint(1,5)
       if X == 1:
           print("You stumble upon wheat and get 7 coins")
           coins = coins+7
           gtime=gtime+1
       if X == 2:
           if stats>1:
               print("You found a zombie and killed it, you got 9 coins")
               coins = coins+9
               stats = stats+1
               gtime=gtime+1
               cxp=cxp+5
           else:
               print("""You found and zombie and it killed you, you die, L
You also lose half of your coins, what a noob""")
               coins = coins/2
               gtime=gtime+1    
       if X == 3:
           print("You stumble upon a tree and break it, +1 stats and +2 coins")
           stats = stats+1
           coins = coins+1
           gtime=gtime+1
       if X == 4:
           if stats>20:
               print("You fight an enderman and kill it, +70 coins and +5 strength")
               stats=stats+5
               coins=coins+70
               gtime=gtime+1
           else:
               print("You find an enderman and try to fight it")
               print("You are not strong enough and almost die but you get lucky")
               print("Someone comes and kills it so you survive")
               gtime=gtime+1
       if X == 5:
          print("You find a mine and collect ores, then some weird enemy appears")
          if stats>100:
             print("You kill it and it drops a weird watch, you decide to keep it")
             haswatch=haswatch+1
             gtime=gtime+1
             cxp=cxp+20
          else:
             print("You quickly realize that you can't fight it and decide to run away")
             gtime=gtime+1
   elif A == "fight":
           G = random.randint(1,2)
           if G == 1:
              print("You find a random zombie")
              if stats>=150:
                 print("You kill it and gain some coins, +5 coins, +5 strength")
                 coins=coins+5
                 stats=stats+5
                 gtime=gtime+1
                 cxp=cxp+35
              if stats<150:
                    print("You died and lost half your coins")
                    coins=coins/2
                    gtime=gtime+1
           if G == 2:
               print("You find a spider and fight it")
               if stats>=160:
                  print("You kill it, +6 coins, +6 strength")
                  coins=coins+6
                  stats=stats+6
                  gtime=gtime+1
                  cxp=cxp+12
               if stats<160:
                  print("You died L you lost half your coins")
                  coins=coins/2
                  gtime=gtime+1
  # if A == "do slayers":
  #       Az = input("What slayer do you want to do")
  #       if Az == "Rev":
  #             Ar = str(input("Which level do you want to do?")
  #             if Ar == "1":
  #               print("very well")
  #             elif Ar == "2":
  #               pass
  #             elif Ar == "3":
  #               pass
  #             elif Ar == "4":
  #               pass
  #             elif Ar == "5":
  #               pass
   if A == "combat level up":
      cxp=cxp+1000
   if A == "fibsh level up":
      fxp=fxp+1000
   if A == "farming level up":
      faxp=faxp+1000
   if cxp == 1000:
      print("You leveled up your combat to lvl 1! \nGratz! And you gained 10k coins!")
      coins=coins+10000
      stats=stats+100
      csl=csl+1
      print("Next combat level is at 2000 combat xp")
   if cxp == (csl+1)*1000:
      csl=csl+1
      print(f"You leveled up your combat to lvl {csl}! \nGratz! And you gained {10*cm}k coins!")
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
   if A == "check combat xp left":
      print(((csl+1)*1000)-cxp)
   if cm == 3:
      if (cxp*cslxp) == (10000*cslxp):
         cm=cm-2
   if fxp == 1000:
      print("You leveled up your fibsh skill to lvl 1! \nGratz! And you gained 10k coins!")
      coins=coins+10000
      stats=stats+100
      csl=csl+1
      print("Next combat level is at 2000 fibshing xp")
   if fxp == (fsl+1)*1000:
      fsl=fsl+1
      print(f"You leveled up your fibshing to lvl {fsl}! \nGratz! And you gained {10*fcm}k coins!")
      coins=coins+(10000*fsm)
      stats=stats+(100*fsm)
      print("Next fibshing level is at", (fsl+1)*1000, "fibshing xp")
   if (fsl*fslxp) == (10*fslxp):
      fslxp=fslxp+1
      fsm=fsm+1
      fcm=fcm+1
      fslm=fslm+0.5
   if A == "tru":
     souls = souls+5
     print(f"You have gained 5 souls you now have {souls} souls!")
   if A == "check fibsh coin multiplier":
      print(fcm)
   if A == "check fibsh stat multiplier":
      print(fsm)
   if A == "check fibsh lvl":
      print(fsl)
   if A == "check fibsh xp left":
      print(((fsl+1)*1000)-fxp)
   if fcm == 3:
      if (fxp*fslxp) == (10000*fslxp):
         fcm=fcm-2
   if faxp == 1000:
      print("You leveled up your farming to lvl 1! Gratz! And you gained 10k coins")
      coins=coins+10000
      stats=stats+100
      fasl=fasl+1
      print("Next farming level is at 2000 farming xp")
   if faxp == (fasl+1)*1000:
      fasl=fasl+1
      faddc=faddc+4
      print(f"You leveled up your farming to lvl {fasl}! \nGratz! And you gained {10*facm}k coins")
      coins=coins+(10000*facm)
      stats=stats+(100*fasm)
      print("Next farming level is at", (fasl+1)*1000, "farming xp")
      print("Your farming double drop chance is now", faddc, "\ndev note: later I'll work on triple drop chance, rn there is only double drop chance")
   if (fasl*faslxp) == (10*faslxp):
      faslxp=faslxp+1
      fasm=fasm+1
      facm=facm+1
      if fasl == 26:
       DD=random.randint(100,100)
   if A == "check farming coin multiplier":
      print(facm)
   if A == "check farming stat multiplier":
      print(fasm)
   if A == "check farming lvl":
      print(faslxp)
   if A == "check farming xp left":
      print(((fasl+1)*1000)-faxp)
   if cm == 3:
      if (cxp*cslxp) == (10000*cslxp):
         cm=cm-2
   if A == "farm":
      L = random.randint(1,1)
      if L == 1:
         if DD == 100:
            print("You farmed 2 pumpkin")
            faxp=faxp+2.4
            gtime=gtime+1
            coins=coins+4
         else:
            print("You farmed 1 pumpkins")
            faxp=faxp+1.2
            gtime=gtime+1
            coins=coins+2
   if A == "grind eyes":
          print("You stumble upon a portal")
          if csl>=12:
             D = random.randint(1,100)
             if D == 100:
               print("You decide to enter it, you find an enderman with a portal frame and kill it, you get a summoning eye")
               stats=stats+1
               coins=coins+15
               B = input("do you want to sell the eye?")
               if B == "yes" or B == "Yes":
                  print("Ok I'll pay 900k coins")
                  coins=coins+900000
               if B == "no":
                  print("ok")
                  eyes=eyes+1
                  xp = xp+2
             else:
                print("You enter the portal and find a Zealot, you kill it")
                xp = xp+1
                coins=coins+15
                cxp=cxp+60
                gtime=gtime+1
          else:
             print("A strange force prevents you from entering it.")
   elif A == "summon drag":
      if eyes>=8:
         C = input("Are you sure?")
         if C == "yes":
            print("Ok you'll summon a dragon.")
            eyes=eyes-8
            E = random.randint(1,100)
         if C == "no":
            print("Ok! Have a good day!")
         if E < 16:
            print("You summoned a young dragon")
         if E > 16 and E < 32:
            print("You summoned a old dragon")
            print("F in the chat")
         if E > 32 and E < 48:
            print("You summoned a wise dragon")
         if E > 48 and E < 64:
            print("You summoned a protector dragon")
            print("F in the chat")
         if E > 64 and E < 80:
            print("You summoned a strong dragon")
         if E > 80 and E < 96:
            print("You summoned a unstable dragon")
         if E >= 96:
            print("You summoned a superior dragon")
   elif A == "eye count":
      print(eyes)
   elif A == "tia":
      C = input("Would you like to claim your fairy souls? ")
      if C == "yes":
         if souls<5:
            print("You need", 5-souls, "to claim your souls.")
      if C == "yes":
         if souls>=5:
            print("Thank you! You now have a permanent stat boost")
            stats=stats+6
            souls=souls-5
      if C == "no":
         print("Ok come again.")
   if J == 1000:
      print("you found a fairy soul colect 5 and give them to tia to get a stat boost")
      print("there is a command called 'tia'")
      souls=souls+1
   elif A == "dark auction":
      M = random.randint(1,12)
      if M == 1:
         print("We have a midas sword up")
         print("would you like to purchace it?")
         A = input("What is your answer?")
         if A == "yes":
            print("Very well that will be 50mil for the sword")
         if A == "no" or A == "No":
            print("Very well Come back soon")
         if A == "yes":
            B = input("Are you sure?")
            if B == "yes" or B == "Yes":
               coins=coins-50000000
               stats=stats+50000
               gtime=gtime+1
      if M == 2:
         print("We have a Spirit mask up")
         print("would you like to purchase it?")
         A = input("What is your answer?")
         if A == "yes":
           print("Very well that will be 1k for the Spirit mask ")
         if A == "no" or A == "No":
                print("Very well Come back soon")
         if A == "yes":
            B = input("Are you sure?")
            if B == "yes" or B == "Yes":
               coins=coins-1000
               stats=stats*1.2
               gtime=gtime+1
      if M == 3:
         print("We have a Ender Artifact up")
         print("would you like to purchase it?")
         A = input("What is your answer?")
         if A == "yes":
              print("Very well that will be 10mil for the Ender Artifact")
         if A == "no" or A == "No":
                  print("Very well Come back soon")
         if A == "yes":
            B = input("Are you sure?")
            if B == "yes" or B == "Yes":
               coins=coins-10000000
               stats=stats+100
               gtime=gtime+1
      if M == 4:
         print("We have a Wither artifact up")
         print("would you like to purchase it?")
         A = input("What is your answer?")
         if A == "yes":
        	 print("Very well that will be 12mil for the wither artifact")
         if A == "no" or A == "No":
             print("Very well Come back soon")
         if A == "yes":
            B = input("Are you sure?")
            if B == "yes" or B == "Yes":
               coins=coins-12000000
               stats=stats+100
               gtime=gtime+1
      if M == 5:
         print("We have a Parrot Pet for sale")
         print("would you like to purchase him/her?")
         A = input("What is your answer?")
         if A == "yes":
            print("Very well that will be 7.5mil for the Pet Parrot")
         if A == "no" or A == "No":
            print("Very well Come back soon")
         if A == "yes":
            B = input("Are you sure?")
            if B == "yes" or B == "Yes":
               coins=coins-7500000
               stats=stats+10000
               gtime=gtime+1
      if M == 6:
         print("We have a Turtle Pet for sale")
         print("would you like to purchase him/her?")
         A = input("What is your answer?")
         if A == "yes":
            print("Very well that will be 20mil for the Pet Turtle")
         if A == "no" or A == "No":
            print("Very well Come back soon")
         if A == "yes":
            B = input("Are you sure?")
            if B == "yes" or B == "Yes":
               coins=coins-20000000
               stats=stats+10000
               gtime=gtime+1
      if M == 7:
         print("We have a Jellyfish Pet for sale")
         print("would you like to purchase him/her?")
         A = input("What is your answer?")
         if A == "yes":
            print("Very well that will be 20.5mil for the Pet Jellyfish")
         if A == "no" or A == "No":
          print("Very well Come back soon")
         if A == "yes":
            B = input("Are you sure?")
            if B == "yes" or B == "Yes":
               coins=coins-20500000
               stats=stats+10000
               gtime=gtime+1
      if M == 8:
         print("We have a Sharp VI book for sale")
         print("would you like to purchase it?")
         A = input("What is your answer?")
         if A == "yes":
            print("Very well that will be 9mil for the sharp 6 book")
         if A == "no" or A == "No":
            print("Very well Come back soon")
         if A == "yes":
            B = input("Are you sure?")
            if B == "yes" or B == "Yes":
               coins=coins-9000000
               stats=stats+1000
               gtime=gtime+1
      if M == 9:
         print("We have a Giant slayer VI book for sale")
         print("would you like to purchase it?")
         A = input("What is your answer?")
         if A == "yes":
            print("Very well that will be 6mil for the Giant killer 6 book")
         if A == "no" or A == "No":
            print("Very well Come back soon")
         if A == "yes":
            B = input("Are you sure?")
            if B == "yes" or B == "Yes":
               coins=coins-6000000
               stats=stats+1000
               gtime=gtime+1
      if M == 10:
         print("We have a Prot VI book for sale")
         print("would you like to purchase it?")
         A = input("What is your answer?")
         if A == "yes":
            print("Very well that will be 3mil for the Prot 6 book")
         if A == "no" or A == "No":
            print("Very well Come back soon")
         if A == "yes":
            B = input("Are you sure?")
            if B == "yes" or B == "Yes":
               coins=coins-3000000
               stats=stats+1000
               gtime=gtime+1
      if M == 11:
         print("We have a Growth VI book for sale")
         print("would you like to purchase it?")
         A = input("What is your answer?")
         if A == "yes":
            print("Very well that will be 3mil for the Growth 6 book")
         if A == "no" or A == "No":
            print("Very well Come back soon")
         if A == "yes":
            B = input("Are you sure?")
            if B == "yes" or B == "Yes":
               coins=coins-3000000
               stats=stats+1000
               gtime=gtime+1
      if M == 12:
         print("We have a Power VI book for sale")
         print("would you like to purchase it?")
         A = input("What is your answer?")
         if A == "yes":
            print("Very well that will be 9mil for the Power 6 book")
         if A == "no" or A == "No":
            print("Very well Come back soon")
         if A == "yes":
            B = input("Are you sure?")
            if B == "yes" or B == "Yes":
               coins=coins-9000000
               stats=stats+1000
               gtime=gtime+1
      if coins < 0:
         print("no more game for u")
         C = input("what do you say bout that?")
         if C == "/":
            print("no more game for u now")
            gameworks=0
         else:
            gameworks=0
   if ggtime == 100:
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
                               G = "Common"
                           if F == 2:
                               G = "Uncommon"
                           if F == 3:
                               G = "Rare"
                           if F == 4:
                               G = "Epic"
                           if F == 5:
                               G = "Legendary"
                               print("I have a", G, "blue whale pet for sale.")
                               A = input("What is your answer?")
                               if A == "yes":
                                   if F == 1:
                                       print("Very well that will be 10k for the Common blue whale pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-10000
                                               stats=stats+10
                                   if F == 2:
                                       print("Very well that will be 25k for the Uncommon blue whale pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-25000
                                               stats=stats+100
                                   if F == 3:
                                       print("Very well that will be 100k for the rare blue whale pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-100000
                                               stats=stats+1000
                                   if F == 4:
                                       print("Very well that will be 1mil for the epic blue whale pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-1000000
                                               stats=stats+10000
                                   if F == 5:
                                       print("Very well that will be 10mil for the legendary blue whale pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-10000000
                                               stats=stats+100000
                                   if A == "no" or A == "No":
                                       print("Very well. Next time I will try to satisfy you.")

                       if E == 2:
                           F = random.randint(1,5)
                           if F == 1:
                               G = "Common"
                           if F == 2:
                               G = "Uncommon"
                           if F == 3:
                               G = "Rare"
                           if F == 4:
                               G = "Epic"
                           if F == 5:
                               G = "Legendary"
                               print("I have a", G, "lion pet for sale.")
                               A = input("What is your answer?")
                               if A == "yes":
                                   if F == 1:
                                       print("Very well that will be 10k for the Common lion pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-10000
                                               stats=stats+10
                                   if F == 2:
                                       print("Very well that will be 25k for the Uncommon lion pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-25000
                                               stats=stats+100
                                   if F == 3:
                                       print("Very well that will be 100k for the rare lion pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-100000
                                               stats=stats+1000
                                   if F == 4:
                                       print("Very well that will be 1mil for the epic lion pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-1000000
                                               stats=stats+10000
                                   if F == 5:
                                       print("Very well that will be 15mil for the legendary lion pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-15000000
                                               stats=stats+100000
                                   if A == "no" or A == "No":
                                       print("Very well. Next time I will try to satisfy you.")
                       if E == 3:
                           F = random.randint(1,5)
                           if F == 1:
                               G = "Common"
                           if F == 2:
                               G = "Uncommon"
                           if F == 3:
                               G = "Rare"
                           if F == 4:
                               G = "Epic"
                           if F == 5:
                               G = "Legendary"
                               print("I have a", G, "tiger pet for sale.")
                               A = input("What is your answer?")
                               if A == "yes":
                                   if F == 1:
                                       print("Very well that will be 10k for the Common tiger pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-10000
                                               stats=stats+10
                                   if F == 2:
                                       print("Very well that will be 25k for the Uncommon tiger pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-25000
                                               stats=stats+100
                                   if F == 3:
                                       print("Very well that will be 100k for the rare tiger pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                                coins=coins-100000
                                                stats=stats+1000
                                   if F == 4:
                                       print("Very well that will be 1mil for the epic tiger pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-1000000
                                               stats=stats+10000
                                   if F == 5:
                                       print("Very well that will be 15mil for the legendary tiger pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-15000000
                                               stats=stats+100000
                                   if A == "no" or A == "No":
                                       print("Very well. Next time I will try to satisfy you.")
                       if E == 4:
                           F = random.randint(1,5)
                           if F == 1:
                              G = "Common"
                           if F == 2:
                              G = "Uncommon"
                           if F == 3:
                              G = "Rare"
                           if F == 4:
                              G = "Epic"
                           if F == 5:
                              G = "Legendary"
                              print("I have a", G, "giraffe pet for sale.")
                              A = input("What is your answer?")
                              if A == "yes":
                                    if F == 1:
                                       print("Very well that will be 10k for the Common giraffe pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-10000
                                               stats=stats+10
                                    if F == 2:
                                       print("Very well that will be 25k for the Uncommon giraffe pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-25000
                                               stats=stats+100
                                    if F == 3:
                                       print("Very well that will be 100k for the rare giraffe pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-100000
                                               stats=stats+1000
                                    if F == 4:
                                       print("Very well that will be 1mil for the epic giraffe pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-1000000
                                               stats=stats+10000
                                    if F == 5:
                                       print("Very well that will be 10mil for the legendary giraffe pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-10000000
                                               stats=stats+100000
                                    if A == "no" or A == "No":
                                       print("Very well. Next time I will try to satisfy you.")
                       if E == 5:
                           F = random.randint(1,5)
                           if F == 1:
                               G = "Common"
                           if F == 2:
                               G = "Uncommon"
                           if F == 3:
                               G = "Rare"
                           if F == 4:
                               G = "Epic"
                           if F == 5:
                               G = "Legendary"
                               print("I have a", G, "elephant pet for sale.")
                               A = input("What is your answer?")
                               if A == "yes":
                                   if F == 1:
                                       print("Very well that will be 10k for the Common elephant pet.")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-10000
                                               stats=stats+10
                                   if F == 2:
                                       print("Very well that will be 25k for the Uncommon elephant pet.")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-25000
                                               stats=stats+100
                                   if F == 3:
                                       print("Very well that will be 100k for the rare elephant pet.")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-100000
                                               stats=stats+1000
                                   if F == 4:
                                       print("Very well that will be 1mil for the epic elephant pet.")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-1000000
                                               stats=stats+10000
                                   if F == 5:
                                       print("Very well that will be 15mil for the legendary elephant pet.")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-15000000
                                               stats=stats+100000
                                   if A == "no" or A == "No":
                                       print("Very well. Next time I will try to satisfy you.")
                       if E == 6:
                            F = random.randint(1,5)
                            if F == 1:
                               G = "Common"
                            if F == 2:
                               G = "Uncommon"
                            if F == 3:
                               G = "Rare"
                            if F == 4:
                               G = "Epic"
                            if F == 5:
                               G = "Legendary"
                            print("I have a", G, "monkey pet for sale.")
                            A = input("What is your answer?")
                            if A == "yes":
                                   if F == 1:
                                       print("Very well that will be 10k for the Common monkey pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-10000
                                               stats=stats+10
                                   if F == 2:
                                       print("Very well that will be 25k for the Uncommon monkey pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-25000
                                               stats=stats+100
                                   if F == 3:
                                       print("Very well that will be 100k for the rare monkey pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-100000
                                               stats=stats+1000
                                   if F == 4:
                                       print("Very well that will be 1mil for the epic monkey pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-1000000
                                               stats=stats+10000
                                   if F == 5:
                                       print("Very well that will be 18mil for the legendary monkey pet")
                                       if A == "yes":
                                           B = input("Are you sure?")
                                           if B == "yes" or B == "Yes":
                                               coins=coins-18000000
                                               stats=stats+100000
                                   if A == "no" or A == "No":
                                       print("Very well. Next time I will try to satisfy you.")
               gtime=0
   if eyes<0:
      gameworks=0
   if souls<0:
      gameworks=0
else:
   print("This action does not exist(this may be a bug because that happens when you choose wynncraft)")
   if haswatch>0:
      stats=stats+haswatch
tR=0
go=0
ci=0
ws=0
uh=0
uc=0
ul=0
ub=0
if(gameworks==2):
   AC = input("What class do you choose(Archer, Warrior, Mage, Assassin, or Shaman)[this is case sensitive, or alternatively you can use numbers corresponding to the class ie 1 for archer, 2 for warrior ect ect.]")
   if AC == "Archer" or AC == 1:
         print("Archer class has been selected")
         cc = "Archer"
   if AC == "Warrior" or AC == 2:
         print("Warrior class has been selected")
         cc = "warrior"
   if AC == "Mage" or AC == 3:
         print("Mage class has been selected")
         cc = "Mage"
   if AC == "Assassin" or AC == 4:
         print("Assassin class has been selected")
         cc = "Assassin"
   if AC == "Shaman" or AC == 5:
         print("Shaman class has been selected")
         cc = "Shaman"
   AB = input("Do you wish to skip the tutorial?")
   if AB == "yes":
      gameworks = 3
      ts = "yes"
   if AB == "no":
      gameworks = 3
      ts = "no"
   while(gameworks==3):
         if(ts=="no"):
               if(tR==0):
                     print("Caracan Driver: Agh!")
                     print("Tasim: Hey,", cn,"! You alright in there? Looks like we hit something.")
                     time.sleep(2)
                     print("Caravan Driver: I swear I hit this same dang boulder every\n time I make this trip.")
                     time.sleep(2)
                     print("Tasim: Does this mean we have to walk all the way to Ragni from here?")
                     time.sleep(2)
                     print("Caravan Driver: It's not that far, it's just a straight path from here. Here,\n take these as a partial refund for the journey.")
                     print("[+8 Emeralds]")
                     em=em+8
                     time.sleep(2)
                     print("Aledar:", cn,", if you're ready, let's get moving")
                     time.sleep(5)
                     print("Tasim: So, what do you guys know about Wynn exactly?")
                     time.sleep(2)
                     print("Aledar: Same as you. That the war's been getting worse,\n so the King of Ragni's been recruting Fruma soldiers.")
                     time.sleep(2)
                     print("Tasim: I've never seen the Wynn Province before. What do you think it's like?")
                     time.sleep(2)
                     print("Aledar: I think we're about to find out.")
                     time.sleep(2)
                     print("Tasim: Must be the gate marking the border between Fruma and Wynn.")
                     time.sleep(2)
                     print("Aledar: Yeah, now we can see what Wynn is really like,\n and find out is the stories are true.")
                     time.sleep(2)
                     print("Aledar: Here we go.")
                     time.sleep(5)
                     print("Tasim: So this is Wynn, huh?")
                     time.sleep(2)
                     print("Aledar: It looks nice. The war clearly hasn't made it this far.")
                     time.sleep(2)
                     print("Soldier: Hey, you three! Come over here.")
                     time.sleep(3)
                     print("Tasim: Use command tnpc to talk to him.")
                     AD = input("Enter command.")
                     if (AD=="tnpc"):
                           print("Tasim: A soldier! What are you doing here?")
                           time.sleep(2)
                           print("Soldier: There's a bit of trouble up ahead. \nYou can't expect to get out of here alive if you aren't prepared.")
                           time.sleep(2)
                           print("Soldier: There's a cave right there. Those often contain useful loot, \nI'd give it a try if i were you.\n[Enter the cave and find some armor]")
                           time.sleep(2)
                           print("Aledar: Let's go inside then.")
                           time.sleep(5)
                           print("Soldier: Enter the cave and get some armor in the loot chest.")
                     
                     print("Aledar: The soldier didn't tell us the path was collapsed! We'll have to jump through.")
                     time.sleep(2)
                     print("Tasim: Come over here, we have a problem...")
                     time.sleep(2)
                     print("Tasim: I don't think we can make this jump...")
                     time.sleep(2)
                     print("Aledar: What is we creak that rock on the celing?\nThat could open up a path for us.")
                     time.sleep(2)
                     print("Tasim: That could work...", cn,",use command break on the rock to break it!")
                     AAA = input("Enter a command.")
                     if AAA=="break":
                           time.sleep(2)
                           print("*CRACK*")
                           print("*CRASH*")
                           print("Aledar It worked! Now we can reach that chest.")
                     if cc == "Warrior":
                           print("[+1 Unitentified helmet]\n[+2 Copper Ingot]")
                           uh=1
                           ci=2
                           time.sleep(3)
                           print("Aledar: I think that's all we needed , let's get out")
                           print("Go through the exit to leave the cave")
                     if cc == "Mage":
                           print("[+1 Unitentified helmet]\n[+2 Copper Ingot]")
                           uh=1
                           time.sleep(3)
                           print("Aledar: I think that's all we needed , let's get out")
                           print("Go through the exit to leave the cave")
                     if cc == "Warrior":
                           print("[+1 Unitentified helmet]\n[+2 Wheat String]")
                           uh=1
                           ws=2
                           time.sleep(3)
                           print("Aledar: I think that's all we needed , let's get out")
                           print("Go through the exit to leave the cave")
                     if cc == "Archer":
                           print("[+1 Unitentified helmet]\n[+2 Wheat String]")
                           uh=1
                           ws=2
                           time.sleep(3)
                           print("Aledar: I think that's all we needed , let's get out")
                           print("Go through the exit to leave the cave")
                     if cc == "Assassin":
                           print("[+1 Unitentified helmet]\n[+2 Copper Ingot]")
                           uh=1
                           ci=2
                           time.sleep(3)
                           print("Aledar: I think that's all we needed , let's get out")
                           print("Go through the exit to leave the cave")
                     if cc == "Shaman":
                           print("[+1 Unitentified helmet]\n[+2 Gudgeon Oil]")
                           uh=1
                           go=2
                           time.sleep(3)
                           print("Aledar: I think that's all we needed , let's get out")
                           print("Go through the exit to leave the cave")
                     time.sleep(2)
                     print("Soldier: That looks like the stuff.")
                     time.sleep(2)
                     print("Soldier: Normally this place is pretty safe\n but somehow a few corrupted clipped through.")
                     tR=1
         if(ts=="yes"):
               if (tR==0):
                     print("tutorial has been skipped")
                     print("[You are now entering Ragni]")
