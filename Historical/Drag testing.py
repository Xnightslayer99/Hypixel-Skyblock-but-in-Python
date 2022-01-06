import random
gameworks = 1
coins = 0
eyes = 0
stats = 1001
xp = 20
zc = 0
while(gameworks==1):
   A = input("what do you want to do")
   if A == "grind eyes":
          print("you stumble upon a portal")
          if stats>1000:
             D = random.randint(420,420)
             if D == 420: 
               print("you decide to enter it, you find an enderman with a portal frame and kill it, you get a summoning eye")
               stats=stats+1
               zc=0
               B = input("do you want to sell the eye?")
               if B == "yes":
                  print("Ok I'll pay 600k coins")
                  coins=coins+600000
               if B == "no":
                  print("ok")
                  eyes=eyes+1
               xp = xp+2
             else:
                print("you find a Zealot, you kill it")
                xp = xp+1
                zc=zc+1
          else:
             print("A strange force prevents you from entering it")
   if zc == 420:
      D = random.randint(1,210)
   if zc == 840:
      D = random.randint(1,105)
   if zc == 1260:
      D = random.randint(1,52)
   if zc == 1680:
      D = random.randint(1,26)
   if zc == 2100:
      D = random.randint(1,13)
   if zc == 2520:
      D = random.randint(1,6)
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
