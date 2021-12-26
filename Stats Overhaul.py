import random
import string
global pname
pname = str(input("What do you wish to be called?(This cannot be changed later)"))
damsys = input("Would you like to use the old or the new Damage system?(old = before strength nerf and new = after strength nerf [cannot be changed])")
class player(object):
    def _init_(self, name):
        self.name = pname
        self.str = 0
        self.cc = 30
        self.cd = 50
        self.hp = 100
        self.maxhp = 100
        self.defence = 0
        self.fero = 0
        self.scc = 20
        self.petluck = 0
        self.mfortune = 0
        self.ffortune = 0
        self.fofortune = 0
        self.magicFind = 0
        self.int = 0
        self.abildam = 0
        self.bdam = 1
        self.ewdam = 0
        self.armor = ["none"]
        self.equipedHelm = "none"
        self.equipedCp = "none"
        self.equipedLeg = "none"
        self.equipedBoots = "none"
        self.equipedWeapon = "fist"
        self.dammul = 0
        self.inv = ["nothing"]
        self.damsys = damsys
        if self.damsys == "old" or self.damsys == "Old":
            def damcalc():
                damage = (5 + self.ewdam + self.str/5) * (1 + self.str/100) * (1+self.cd/100) * (1+self.dammul/100)
            GameRunAllow = True
        if self.damsys == "new" or self.damsys == "New":
            def damcalc():
                damage = (5 + self.ewdam) * (1 + self.str/100) * (1 + self.cd / 100) * (1 + self.dammul / 100)
            GameRunAllow = True
print ("Hello, "+pname)
while(GameRunAllow == True):
    A = input
