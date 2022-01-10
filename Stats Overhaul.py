import random
import string
pname = str(input("What do you wish to be called?(This cannot be changed later)"))
damsys = input("Would you like to use the old or the new Damage system?(old = before strength nerf and new = after strength nerf [cannot be changed])")
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
if damsys == "old" or damsys == "Old":
    def damcalc():
        damage = (5 + ewdam + stre/5) * (1 + stre/100) * (1+cd/100) * (1+dammul/100)
    GameRunAllow = True
if damsys == "new" or damsys == "New":
    def damcalc():
        damage = (5 + ewdam) * (1 + stre/100) * (1 + cd / 100) * (1 + dammul / 100)
    GameRunAllow = True
printe ("Hello, "+pname)
while(GameRunAllow == True):
    A = input
