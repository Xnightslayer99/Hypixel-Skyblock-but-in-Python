import random
import string
global GameRunAllow
global cheatCodes
cheatCodes = ["SK!ULT", "SQTQQTXVX", "monika", "Monika"]
global badNames
badNames = ["mon-ika", "Mon-ika"]
global chooseName
chooseName = True
def nameChoose():
  global sethp
  global infhp
  global pname
  while chooseName == True:
    pname = str(input("What do you wish to be called?(This cannot be changed later)"))
    if pname in cheatCodes:
      print("Cheat Code discovered!")
      if pname == cheatCodes[0] or pname == cheatCodes[1]:
        infhp = True
        def sethp():
          global hp
          global maxhp
          if infhp == True:
            hp = -1
            maxhp = -1
          else:
            hp = 100
            maxhp = 100
      if pname == cheatCodes[2] or pname == cheatCodes[3]:
        infhp = True
        global monika
        def monika():
          global stre
          global hp
          global maxhp
          global cc
          global cd
          global defence
          global fero
          global scc
          global petluck
          global mfortune
          global ffortune
          global fofortune
          global magicFind
          global intee
          global abildam
          global bdam
          global ewdam
          global dammul
          stre = 999999
          hp = -1
          maxhp = -1
          cc = 100
          cd = 999999
          defence = 999999
          fero = 999999
          scc = 100
          petluck = 100
          mfortune = 1000
          ffortune = 1000
          fofortune = 1000
          magicFind = 999999
          intee = 999999
          abildam = 999999
          bdam = 999999
          ewdam = 9999999
          dammul = 999999
    else:
      def sethp():
        global hp
        global maxhp
        if infhp == True:
          hp = -1
          maxhp = -1
        else:
          hp = 100
          maxhp = 100
    if pname in badNames:
      if pname == badNames[0] or pname == badNames[1]:
        global bname
        bname = True
        try:
          if infhp == True:
            print("Oh no... You lost your infinite hp how sad... Now go spell Monika's name correctly 15 times")
        except:
          pass
        global badName
        def badName():
          global stre
          global hp
          global maxhp
          global cc
          global cd
          global defence
          global fero
          global scc
          global petluck
          global mfortune
          global ffortune
          global fofortune
          global magicFind
          global intee
          global abildam
          global bdam
          global ewdam
          global dammul
          stre = 1
          hp = 1
          maxhp = 1
          cc = 1
          cd = 1
          defence = 0
          fero = 0
          scc = 1
          petluck = 0
          mfortune = 0
          ffortune = 0
          fofortune = 0
          magicFind = 0
          intee = 0
          abildam = 0
          bdam = 1
          ewdam = 0
          dammul = -50
    if pname not in cheatCodes:
      break
    if pname == "exit":
      GameRunAllow = False
nameChoose()
damsys = input("Would you like to use the old or the new Damage system?(old = before strength nerf and new = after strength nerf [cannot be changed])")
GameRunAllow = False
name = pname
stre = 0
cc = 30
cd = 50
hp = 100
maxhp = 100
try:
  if infhp == True:
    sethp()
except:
  pass
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
try:
  monika()
except:
  pass
try:
  if bname == True:
    badName()
except:
  pass
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
    if hp == 0 or (hp < 0 and infhp is not True):
      print("OOF, You died and lost half your coins!")
    A = input("What do you want to do? ")
    if A == "test damage":
      damcalc()
      print("You did "+str(damage)+" damage!")
    elif A == "uuddlrlrba":
      try:
        if bname == True:
          print("Im sorry Dave. Im afraid I cannot alow you to do that. You spelled Monika's name wrong.")
      except:
        pass
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
          if a == "exit cheat mode" or a == "exit" or a == "none":
            b = input("Are you sure you wish to exit cheat mode? ")
            if b == "yes" or b == "Yes":
              break
            else:
              print("continue on then...")
          if a == "name":
            nameChoose()
    if A == "exit":
      GameRunAllow == False
      break