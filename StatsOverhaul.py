import random
import string
global GameRunAllow
cheatCodes = ["SK!ULT", "SQTQQTXVX"]
chooseName = True
while chooseName == True:
  pname = str(input("What do you wish to be called?(This cannot be changed later)"))
  if pname in cheatCodes:
    print("Cheat Code discovered!")
    if pname == cheatCodes[0] or pname == cheatCodes[1]:
      infhp = True
      def sethp():
        if infhp == True:
          hp = -1
          maxhp = -1
        else:
          hp = 100
          maxhp = 100
  if pname not in cheatCodes:
    break
  if pname == "exit":
    GameRunAllow = False
damsys = input("Would you like to use the old or the new Damage system?(old = before strength nerf and new = after strength nerf [cannot be changed])")
GameRunAllow = False
name = pname
stre = 0
cc = 30
cd = 50
sethp()
defence = 0
fero = 0
scc = 20
petluck = 0
mfortune = 0
ffortune = 0
fofortune = 0
magicFind = 0
intee = 0
abildam = 0
bdam = 1
ewdam = 0
armor = ["none"]
equipedHelm = "none"
equipedCp = "none"
equipedLeg = "none"
equipedBoots = "none"
equipedWeapon = "fist"
dammul = 0
inv = ["nothing"]
damsys = damsys
cheatMode = False
if damsys == "old" or damsys == "Old":
  def damcalc():
    global damage
    damage = (5 + ewdam + stre/5) * (1 + stre/100) * (1+cd/100) * (1+dammul/100)
  GameRunAllow = True
elif damsys == "new" or damsys == "New":
  def damcalc():
    global damage
    damage = (5 + ewdam) * (1 + stre/100) * (1 + cd / 100) * (1 + dammul / 100)
  GameRunAllow = True
print("Hello, "+pname)
while(GameRunAllow == True):
    A = input("What do you want to do? ")
    if A == "test damage":
      damcalc()
      print("You did "+str(damage)+" damage!")
    elif A == "uuddlrlrba":
      print("Cheat Code discovered!")
      cheatMode = True
      while cheatMode == True:
        a = input("What stat do you wish to change? ")
        if a == "strength":
          b = True
          while b == True:
            try:
                aa = input("What would you like to change it to? ")
                if type(aa) == str:
                    aa = float(aa)
                if isinstance(aa, float) == True:
                    stre = aa
                    print("Damage multiplier has been "+f"changed to {stre}")
                    break
            except:
                print("That is not a valid number")
        if a == "damage multiplier":
          b = True
          while b == True:
            try:
                aa = input("What would you like to change it to? ")
                if type(aa) == str:
                    aa = float(aa)
                if isinstance(aa, float) == True:
                    dammul = aa
                    print("Damage multiplier has been "+f"changed to {dammul}")
                    break
            except:
                print("That is not a valid number")
    if A == "exit":
      GameRunAllow == False
      break