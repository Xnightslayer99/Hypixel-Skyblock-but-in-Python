import random
gameworks = 1
coins = 0
eyes = 0
stats = 1001
xp = 20
souls = 0
cxp = 9000
csl = 9
cm = 1
sm=1
cslxp = 1
while(gameworks==1):
   A = input("what do you want to do?")
   if A == "fight":
      B = random.randint(1,1)
      if B == 1:
         print("you found a zombie and fight it.")
         if stats>=150:
            print("you kill it +5 strength, +5 coins, and +5 combat xp")
            stats=stats+5
            coins=coins+5
            cxp=cxp+500
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
