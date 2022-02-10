import random
import string
global GameRunAllow
pname = str(input("What do you wish to be called?(This cannot be changed later)"))
if pname == "exit":
  GameRunAllow = False
damsys = input("Would you like to use the old or the new Damage system?(old = before strength nerf and new = after strength nerf [cannot be changed])")
GameRunAllow = False
name = pname
stre = 0
cc = 30
cd = 50
hp = 100
maxhp = 100
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
      a = input("What stat do you wish to change? ")
      if a == "strength":
        aa = int(input("Please choose a number to change it to: "))
        stre = aa
      if a == ""
    if A == "exit":
      GameRunAllow == False
      break
