import random
import time
import os
import getpass
import pickle
cheatCodes = ["SK!ULT", "SQTQQTXVX", "monika", "Monika", "1NF5UM3Y35", "A1WAY5CR17", "1NF-CR17"]
global badNames
badNames = ["mon-ika", "Mon-ika"]
global chooseName
chooseName = True
def nameChoose(z):
  global sethp
  global infhp
  global pname
  global spname
  while chooseName == True:
    pname = str(input("What do you wish to be called?(This cannot be changed later)"))
    spname = pname
    if z == 0:
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
        if pname == cheatCodes[4]:
          def infeyes():
            global seed
            seed = 487
        if pname == cheatCodes[5]:
          def alwayscrit():
            global seed
            seed = 9924
        if pname == cheatCodes[6]:
          def alwayscrit():
            pass
          def infeyes():
            pass
          def infcrit():
            global seed
            seed = 83546
        if pname == cheatCodes[2] or pname == cheatCodes[3]:
          infhp = True
          global monika
          global minika
          minika = 1
          def monika():
            global pname
            pname = getpass.getuser()
            global stre
            global hp
            global maxhp
            global chosenClass
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
            chosenClass = 100
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
            global minika
            minika = 0
            global stre
            global hp
            global maxhp
            global chosenClass
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
            chosenClass = 1
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
    if z == 1:
      print("Alright Your name is now "+spname)
    if pname not in cheatCodes or (pname in cheatCodes and z != 0):
      break
    if pname == "exit":
      GameRunAllow = False
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
nameChoose(0)
try:
  if minika == 1:
    monika()
except:
  try:
    if bname == True:
      badName()
  except:
    pass
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
stre = 0
global cc
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
# armor = ["none"]
# equipedHelm = "none"
# equipedCp = "none"
# equipedLeg = "none"
# equipedBoots = "none"
# equipedWeapon = "fist"
dammul = 0
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
chosenClass = "none"
ts = "blank"
em = 0
mc1 = 0
mc2 = 0
mc3 = 0
mc4 = 0
mc5 = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
smc1 = 0
smc2 = 0
smc3 = 0
cml = 0
voteNow = False
slayerXpMod = 1
c1perks = "None"
perksc1 = "french_bread_gud"
c2perks = "None"
perksc2 = "french_bread_gud"
c3perks = "None"
perksc3 = "french_bread_gud"
c4perks = "None"
perksc4 = "french_bread_gud"
c5perks = "None"
perksc5 = "french_bread_gud"
perksm = "french_bread_gud"
tempperksm = "french_bread_gud"
aatroxperks = ["1. Slayer XP Buff: Earn 25% more Slayer XP.", "2. Pathfinder: Gain rare drops 20% more often.", "3. SLASHED Pricing: Starting Slayer quests is half price."]
barryperks = ["1. Magic XP Boost: Gain 15% more Enchanting and  Alchemy XP.", "2. Arcane Catalyst: Spells deal 15% increased damage.", "3. Astral Negotiator: Enchanting and anvils costs -15% less experience."]
coleperks = ["1. Mining XP Buff: Earn 1.5x Mining experience", "2. Prospection: Mining minions work 25% faster.(minions are a WIP)", "3. Mining Fiesta: Starts a special event in Early Autumn. Earn 1.5x Mining exp, 2x drops and Unique Loot. Active only on public islands.(WIP, when added it should compound with perk no.1)"]
scorpiusperks = "1.Bribe: If Scorpius wins and you voted for him, Mayor Scorpius will offer you 1,000,000 coins as a token of grattitude.\n2. Darker Auctions: Scorpius will intrude in Dark Auctions, increasing the number of rounds to 7 and offering special items.(WIP)"
dianaperks = ["1. Pet XP Buff: Gain 35% more pet XP.", "2. Lucky!: Gain +25 Pet Luck(Pets are WIP)", "3. Mythological Ritual: Mayor Diana will sell the Griffin Pet, which lets you find Mythological Creatures and tons of unique items.(WIP)"]
diazperks = ["1. Barrier Street: Gain 25% more bank interest.(WIP)", "2. Shopping Spree: Increase daily NPC buy limits by 10x.(WIP)"]
foxyperks = ["1. Sweet Tooth: Grants +20% chance to get candy from mobs during the Spooky Festival.(WIP)", "2. Benevolence: Gain 2.5x gifts from the attack on Jerry's Workshop.(WIP)", "3. Extra Event: Schedules an extra event during the year.(WIP)"]
marinaperks = ["1. Fishing XP Buff: Gain 50% more fishing XP", "2. Luck of the Sea 2.0: Gain +15 Sea Creature Chance.", "3. Fishing Festival: Start a special fishing event during the first 3 days of each month! Fish and fight dangerous Sharks and earn unique Shark loot."]
paulperks = ["1. EZPZ: Gain 10 extra bonus score in Dungeons.(WIP)", "2. Marauder: Dungeon reward chests are 20% cheaper.(WIP)", "3. Benediction: Blessings are 25% stronger.(WIP)"]
derpyperks = "1. TURBO MINIONS!!!: Minions have double the output! \n2. AH CLOSED!!!: The Auction House will be closed while Derpy is elected!\n3. DOUBLE MOBS HP!!!: ALL monsters have double health!\n 4. MOAR SKILLZ!!!: Gain +50% more skill experience!(All of derpy's perks are a WIP)"
jerryperks = "1. Perkpocalypse: Activates all perks of another mayor every 18 SkyBlock days (6 hours).\n2. Statspocalypse: Increases all stats by 10%.\n3. Jerrypocalypse: Reveal hidden Jerries from logging, farming, mining, and killing mobs.(Perks 1 and 3 are a WIP)"
def mayorElectionReset():
  global mc1
  mc1 = 0
  global mc2
  mc2 = 0
  global mc3
  mc3 = 0
  global mc4
  mc4 = 0
  global mc5
  mc5 = 0
  global c1
  c1 = 0
  global c2
  c2 = 0
  global c3
  c3 = 0
  global c4
  c4 = 0
  global c5
  c5 = 0
  global smc1
  smc1 = 0
  global smc2
  smc2 = 0
  global smc3
  smc3 = 0
  global aa
  aa = 0
  global aaa
  aaa = 0
  global aaaa
  aaaa = 0
  global cml
  cml = 0
  global voteNow
  voteNow = False
  global c1perks
  c1perks = "None"
  global perksc1
  perksc1 = "french_bread_gud"
  global c2perks
  c2perks = "None"
  global perksc2
  perksc2 = "french_bread_gud"
  global c3perks
  c3perks = "None"
  global perksc3
  perksc3 = "french_bread_gud"
  global c4perks
  c4perks = "None"
  global perksc4
  perksc4 = "french_bread_gud"
  global c5perks
  c5perks = "None"
  global perksc5
  perksc5 = "french_bread_gud"
  global tempperksm
  tempperksm = "french_bread_gud"
  global slayerXpMod
  slayerXpMod = 1
mayors = ["Aatrox", "Barry the Wizard", "Cole the Miner", "Diana", "Diaz", "Foxy", "Marina", " Paul"]
smayors = ["Jerry", "Derpy", "Scorpius"]
smayor = "Nancy"
cmayor = "None"
cls()
print("Use windowed fullscreen for the best viewing!")
print("Join the testing discord server for updates and some info!https://discord.gg/Sn2A36M")
print("Most Mayors currently have no function this is because they are most likely still being worked on.")
while True:
  try:
    if minika == 1:
      cls()
      print(f"Monika: Ehehe~ You remembered me, thank you, {pname}.")
    if bname == True:
      cls()
      print(f"Monika: {getpass.getuser()} I can't believe you!\nMonika: I've told you I dont like to be called that!")
  except:
    pass
  AA = input("Which game do you want to play(skyblock or wynncraft) ")
  try:
    if AA == "skyblock":
      game = "skyblock"
    if AA == "wynncraft":
      game = "wynncraft"
    break
  except:
    pass
if game == "skyblock":
  cls()
  print("Skyblock has been chosen.")
while(game == "skyblock"):
  #saved = [cheatCodes, badNames, chooseName, pname, spname, hp, maxhp, infhp, monika, minika, stre, chosenClass, cd, defence, fero, scc, petluck, mfortune, ffortune, fofortune, magicFind, intee, abildam, bdam, ewdam, dammul, gameworks, coins, stats, haswatch, xp, fibsh, gtime, ggtime, eyes, souls, cxp, csl, cm, sm, cslxp, fslxp, fcm, fsm, fsl, fxp, fslm,fasl, faxp, faslxp, facm, fasm, faddc, IC, ts, em, mc1, mc2, mc3, mc4, mc5, c1, c2, c3, c4, c5, smc1, smc2, smc3, cml, voteNow, slayerXpMod, c1perks, perksc1, c2perks, perksc2, c3perks, perksc3, c4perks, perksc4, c5perks, perksc5, perksm]
  fxpg = (12*fslm)
  if fasl == 26:
      DD=random.randint(100,100)
  A = input("What action do you want to do? ")
  # if A == "save":
  #   file = open('save.txt', 'wb')
  #   pickle.dump(saved, file)
  if aatroxperks[0] in perksm:
    slayerXpMod = 1.25
    print("aatrox's first perk")
  if aatroxperks[1] in perksm:
      #magicFind = magicFind + 20
      print("aatrox's 2nd perk")
  if aatroxperks[2] in perksm:
      slayerSPM = 0.5
      print("aatrox's 3rd perk")
  if barryperks[0] in perksm:
      alchXpMod = 1.15
      enchantXpMod = 1.15
  if barryperks[1] in perksm:
      magicDamMod = 1.15
  if barryperks[2] in perksm:
      echantXpCost = 0.85 
      anvilXpCost = 0.85
  if coleperks[0] in perksm:
      #miningXpMod += 1.5
      pass
  if coleperks[1] in perksm:
      print("Whoops This feature is still a WIP!(minions might not be added)")
  if coleperks[2] in perksm:
      pass
  if scorpiusperks in perksm:
    print(f"Oh, hello {spname}, Thank you for voting for me!\nHere is your reward.")
    coins = coins+1000000
    print(f"Game: You gained 1000000 coins. You now have {coins} coins.")
  if A == "Stop" or A == "exit" or A == "Exit" or A == "stop":
    game = "stopped"
  if A == "vote":
      if smayor != 0:
          print("The current mayor is", smayor)
      else:
          print("The current mayor is", cmayor)
      aa = random.randint(0, 8)
      mc1 = aa
      if aa == 8:
          aaa = random.randint(0, 2)
          smc1 = aaa
          c1 = smayors[smc1]
      else:
          c1 = mayors[mc1]
      aa = random.randint(0, 8)
      if aa == 8:
          aaa = random.randint(0, 2)
          if aaa == smc1:
              while aaa == smc1:
                  aaa = random.randint(0, 2)
          smc2 = aaa
          c2 = smayors[smc2]
      else:
          if aa == mc1:
              while aa == mc1:
                  aa = random.randint(0, 7)
          mc2 = aa
          c2 = mayors[mc2]
      aa = random.randint(0, 8)
      if aa == 8:
          aaa = random.randint(0, 2)
          if aaa == smc1 or aaa == smc2:
              while(aaa == smc1 or aaa == smc2):
                  aaa = random.randint(0, 2)
          smc3 = aaa
          c3 = smayors[aaa]
      else:
          if aa == mc1 or aa == mc2:
              while aa == mc1 or aa == mc2:
                  aa = random.randint(0, 7)
          mc3 = aa
          c3 = mayors[mc3]
      aa = random.randint(0, 8)
      if aa == 8:
          aaa = random.randint(0, 2)
          if aaa == smc1 or aaa == smc2 or smc3:
              while(aaa == smc1 or aaa == smc2 or aaa == smc3):
                  if (smc1 != 0 & smc2 != 0 & smc3 != 0):
                      continue
          c4 = smayors[aaa]
      else:
          if aa == mc1 or aa == mc2 or aa == mc3:
              while aa == mc1 or aa == mc2 or aa == mc3:
                  aa = random.randint(0, 7)
          mc4 = aa
          c4 = mayors[mc4]
      aa = random.randint(0, 8)
      if aa == 8:
          aaa = random.randint(0, 2)
          if aaa == smc1 or aaa == smc2 or smc3:
              while(aaa == smc1 or aaa == smc2 or aaa == smc3):
                  if (smc1 != 0 & smc2 != 0 & smc3 != 0):
                      continue
          c5 = smayors[aaa]
      else:
          if aa == mc1 or aa == mc2 or aa == mc3 or aa == mc4:
              while aa == mc1 or aa == mc2 or aa == mc3 or aa == mc4:
                  aa = random.randint(0, 7)
          mc5 = aa
          c5 = mayors[mc5]
      print("The current candidates are:", c1+",", c2+",", c3+",", c4+",", "and "+c5)
      candidates = c1 + c2 + c3 + c4 + c5
      pVoteConfirm = True
      while (pVoteConfirm == True):
          AA = input("What will you do in the election.(valid responses are: 'vote', 'see perks', and 'candidates' if you choose 'vote' you will be forced to vote) ")
          if AA == "vote":
              voteNow = True
              break
          if AA == "see perks":
              AAA = input("Whos perks do you wish to see?(enter number corresponding to the candidate that you wish to see)")
              if AAA == "1":
                  if c1 == "Aatrox":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c1perks = aatroxperks[0]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 1:
                          c1perks = aatroxperks[1]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 2:
                          c1perks = aatroxperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 3:
                          c1perks = aatroxperks[0]+"\n"+aatroxperks[1]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 4:
                          c1perks = aatroxperks[0]+"\n"+aatroxperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 5:
                          c1perks = aatroxperks[1]+"\n"+aatroxperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 6:
                          c1perks = aatroxperks[0]+"\n"+aatroxperks[1]+"\n"+aatroxperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if perksc1 == "french_bread_gud":
                          perksc1 = c1perks
                      if c1perks != perksc1:
                          c1perks = perksc1
                  if c1 == "Barry the Wizard":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c1perks = barryperks[0]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 1:
                          c1perks = barryperks[1]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 2:
                          c1perks = barryperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 3:
                          c1perks = barryperks[0]+"\n"+barryperks[1]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 4:
                          c1perks = barryperks[0]+"\n"+barryperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 5:
                          c1perks = barryperks[1]+"\n"+barryperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 6:
                          c1perks = barryperks[0]+"\n"+barryperks[1]+"\n"+barryperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if perksc1 == "french_bread_gud":
                          perksc1 = c1perks
                      if c1perks != perksc1:
                          c1perks = perksc1
                  if c1 == "Diana":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c1perks = dianaperks[0]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 1:
                          c1perks = dianaperks[1]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 2:
                          c1perks = dianaperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 3:
                          c1perks = dianaperks[0]+"\n"+dianaperks[1]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 4:
                          c1perks = dianaperks[0]+"\n"+dianaperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 5:
                          c1perks = dianaperks[1]+"\n"+dianaperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 6:
                          c1perks = dianaperks[0]+"\n"+dianaperks[1]+"\n"+dianaperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if perksc1 == "french_bread_gud":
                          perksc1 = c1perks
                      if c1perks != perksc1:
                          c1perks = perksc1
                  if c1 == "Diaz":
                      AAAA = random.randint(0, 2)
                      if AAAA == 0:
                          c1perks = diazperks[0]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 1:
                          c1perks = diazperks[1]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 2:
                          c1perks = diazperks[0]+"\n"+diazperks[1]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                  if c1 == "Cole the Miner":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c1perks = coleperks[0]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 1:
                          c1perks = coleperks[1]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 2:
                          c1perks = coleperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 3:
                          c1perks = coleperks[0]+"\n"+coleperks[1]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 4:
                          c1perks = coleperks[0]+"\n"+coleperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 5:
                          c1perks = coleperks[1]+"\n"+coleperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 6:
                          c1perks =  coleperks[0]+"\n"+coleperks[1]+"\n"+coleperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if perksc1 == "french_bread_gud":
                          perksc1 = c1perks
                      if c1perks != perksc1:
                          c1perks = perksc1
                  if c1 == "Foxy":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c1perks = foxyperks[0]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 1:
                          c1perks = foxyperks[1]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 2:
                          c1perks = foxyperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 3:
                          c1perks = foxyperks[0]+"\n"+foxyperks[1]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 4:
                          c1perks = foxyperks[0]+"\n"+foxyperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 5:
                          c1perks = foxyperks[1]+"\n"+foxyperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 6:
                          c1perks = foxyperks[0]+"\n"+foxyperks[1]+"\n"+foxyperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if perksc1 == "french_bread_gud":
                          perksc1 = c1perks
                      if c1perks != perksc1:
                          c1perks = perksc1
                  if c1 == "Marina":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c1perks = marinaperks[0]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 1:
                          c1perks = marinaperks[1]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 2:
                          c1perks = marinaperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 3:
                          c1perks = marinaperks[0]+"\n"+marinaperks[1]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 4:
                          c1perks = marinaperks[0]+"\n"+marinaperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 5:
                          c1perks = marinaperks[1]+"\n"+marinaperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 6:
                          c1perks = marinaperks[0]+"\n"+marinaperks[1]+"\n"+marinaperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if perksc1 == "french_bread_gud":
                          perksc1 = c1perks
                      if c1perks != perksc1:
                          c1perks = perksc1
                  if c1 == "Paul":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          if perksc1 != "french_bread_gud":
                            perksc1 = paulperks[0]
                          else:
                            c1perks = paulperks[0]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 1:
                          if perksc1 != "french_bread_gud":
                            perksc1 = paulperks[1]
                          else:
                            c1perks = paulperks[1]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 2:
                          if perksc1 != "french_bread_gud":
                            perksc1 = paulperks[2]
                          else:
                            c1perks = paulperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 3:
                          if perksc1 != "french_bread_gud":
                            perksc1 = paulperks[0]+"\n"+paulperks[1]
                          else:
                            c1perks = paulperks[0]+"\n"+paulperks[1]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 4:
                          if perksc1 != "french_bread_gud":
                            perksc1 = paulperks[0]+"\n"+paulperks[2]
                          else:
                            c1perks = paulperks[0]+"\n"+paulperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 5:
                          if perksc1 != "french_bread_gud":
                            perksc1 = paulperks[1]+"\n"+paulperks[2]
                          else:
                            c1perks = paulperks[1]+"\n"+paulperks[2]
                          if perksc1 != "french_bread_gud":
                              print(perksc1)
                          else:
                              print(c1perks)
                      if AAAA == 6:
                        if perksc1 != "french_bread_gud":
                          perksc1 = paulperks[0]+"\n"+paulperks[1]+"\n"+paulperks[2]
                        else:
                          c1perks = paulperks[0]+"\n"+paulperks[1]+"\n"+paulperks[2]
                        if perksc1 != "french_bread_gud":
                            print(perksc1)
                        else:
                            print(c1perks)
                      if perksc1 == "french_bread_gud":
                          perksc1 = c1perks
                      if c1perks != perksc1:
                          c1perks = perksc1
                  if c1 == "Scorpius":
                    if perksc1 != "french_bread_gud":
                      perksc1 = scorpiusperks
                    else:
                      c1perks = scorpiusperks
                    if perksc1 != "french_bread_gud":
                            print(perksc1)
                    else:
                      print(c1perks)
                    if perksc1 == "french_bread_gud":
                        perksc1 = c1perks
                    if c1perks != perksc1:
                        c1perks = perksc1
                  if c1 == "Derpy":
                    if perksc1 != "french_bread_gud":
                      perksc1 = derpyperks
                    else:
                      c1perks = derpyperks
                    if perksc1 != "french_bread_gud":
                            print(perksc1)
                    else:
                            print(c1perks)
                    if perksc1 == "french_bread_gud":
                        perksc1 = c1perks
                    if c1perks != perksc1:
                        c1perks = perksc1
                  if c1 == "Jerry":
                    if perksc1 != "french_bread_gud":
                      perksc1 = jerryperks
                    else:
                      c1perks = jerryperks
                    if perksc1 != "french_bread_gud":
                            print(perksc1)
                    else:
                            print(c1perks)
                    if perksc1 == "french_bread_gud":
                        perksc1 = c1perks
                    if c1perks != perksc1:
                        c1perks = perksc1
              if AAA == "2":
                  if c2 == "Aatrox":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c2perks = aatroxperks[0]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 1:
                          c2perks = aatroxperks[1]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 2:
                          c2perks = aatroxperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 3:
                          c2perks = aatroxperks[0]+"\n"+aatroxperks[1]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 4:
                          c2perks = aatroxperks[0]+"\n"+aatroxperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 5:
                          c2perks = aatroxperks[1]+"\n"+aatroxperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 6:
                          c2perks = aatroxperks[0]+"\n"+aatroxperks[1]+"\n"+aatroxperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if perksc2 == "french_bread_gud":
                          perksc2 = c2perks
                      if c2perks != perksc2:
                          c2perks = perksc2
                  if c2 == "Barry the Wizard":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c2perks = barryperks[0]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 1:
                          c2perks = barryperks[1]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 2:
                          c2perks = barryperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 3:
                          c2perks = barryperks[0]+"\n"+barryperks[1]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 4:
                          c2perks = barryperks[0]+"\n"+barryperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 5:
                          c2perks = barryperks[1]+"\n"+barryperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 6:
                          c2perks = barryperks[0]+"\n"+barryperks[1]+"\n"+barryperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if perksc2 == "french_bread_gud":
                          perksc2 = c2perks
                      if c2perks != perksc2:
                          c2perks = perksc2
                  if c2 == "Diana":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c2perks = dianaperks[0]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 1:
                          c2perks = dianaperks[1]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 2:
                          c2perks = dianaperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 3:
                          c2perks = dianaperks[0]+"\n"+dianaperks[1]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 4:
                          c2perks = dianaperks[0]+"\n"+dianaperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 5:
                          c2perks = dianaperks[1]+"\n"+dianaperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 6:
                          c2perks = dianaperks[0]+"\n"+dianaperks[1]+"\n"+dianaperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if perksc2 == "french_bread_gud":
                          perksc2 = c2perks
                      if c2perks != perksc2:
                          c2perks = perksc2
                  if c2 == "Diaz":
                      AAAA = random.randint(0, 2)
                      if AAAA == 0:
                          c2perks = diazperks[0]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 1:
                          c2perks = diazperks[1]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 2:
                          c2perks = diazperks[0]+"\n"+diazperks[1]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                  if c2 == "Cole the Miner":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c2perks = coleperks[0]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 1:
                          c2perks = coleperks[1]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 2:
                          c2perks = coleperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 3:
                          c2perks = coleperks[0]+"\n"+coleperks[1]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 4:
                          c2perks = coleperks[0]+"\n"+coleperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 5:
                          c2perks = coleperks[1]+"\n"+coleperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 6:
                          c2perks =  coleperks[0]+"\n"+coleperks[1]+"\n"+coleperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if perksc2 == "french_bread_gud":
                          perksc2 = c2perks
                      if c2perks != perksc2:
                          c2perks = perksc2
                  if c2 == "Foxy":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c2perks = foxyperks[0]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 1:
                          c2perks = foxyperks[1]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 2:
                          c2perks = foxyperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 3:
                          c2perks = foxyperks[0]+"\n"+foxyperks[1]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 4:
                          c2perks = foxyperks[0]+"\n"+foxyperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 5:
                          c2perks = foxyperks[1]+"\n"+foxyperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 6:
                          c2perks = foxyperks[0]+"\n"+foxyperks[1]+"\n"+foxyperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if perksc2 == "french_bread_gud":
                          perksc2 = c2perks
                      if c2perks != perksc2:
                          c2perks = perksc2
                  if c2 == "Marina":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c2perks = marinaperks[0]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 1:
                          c2perks = marinaperks[1]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 2:
                          c2perks = marinaperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 3:
                          c2perks = marinaperks[0]+"\n"+marinaperks[1]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 4:
                          c2perks = marinaperks[0]+"\n"+marinaperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 5:
                          c2perks = marinaperks[1]+"\n"+marinaperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 6:
                          c2perks = marinaperks[0]+"\n"+marinaperks[1]+"\n"+marinaperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if perksc2 == "french_bread_gud":
                          perksc2 = c2perks
                      if c2perks != perksc2:
                          c2perks = perksc2
                  if c2 == "Paul":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c2perks = paulperks[0]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 1:
                          c2perks = paulperks[1]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 2:
                          c2perks = paulperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 3:
                          c2perks = paulperks[0]+"\n"+paulperks[1]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 4:
                          c2perks = paulperks[0]+"\n"+paulperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 5:
                          c2perks = paulperks[1]+"\n"+paulperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if AAAA == 6:
                          c2perks = paulperks[0]+"\n"+paulperks[1]+"\n"+paulperks[2]
                          if perksc2 != "french_bread_gud":
                              print(perksc2)
                          else:
                              print(c2perks)
                      if perksc2 == "french_bread_gud":
                          perksc2 = c2perks
                      if c2perks != perksc2:
                          c2perks = perksc2
                  if c2 == "Scorpius":
                      c2perks = scorpiusperks
                  if c2 == "Derpy":
                      c2perks = derpyperks
                  if c2 == "Jerry":
                      c2perks = jerryperks
              if AAA == "3":
                  if c3 == "Aatrox":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c3perks = aatroxperks[0]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 1:
                          c3perks = aatroxperks[1]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 2:
                          c3perks = aatroxperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 3:
                          c3perks = aatroxperks[0]+"\n"+aatroxperks[1]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 4:
                          c3perks = aatroxperks[0]+"\n"+aatroxperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 5:
                          c3perks = aatroxperks[1]+"\n"+aatroxperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 6:
                          c3perks = aatroxperks[0]+"\n"+aatroxperks[1]+"\n"+aatroxperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if perksc3 == "french_bread_gud":
                          perksc3 = c3perks
                      if c3perks != perksc3:
                          c3perks = perksc3
                  if c3 == "Barry the Wizard":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c3perks = barryperks[0]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 1:
                          c3perks = barryperks[1]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 2:
                          c3perks = barryperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 3:
                          c3perks = barryperks[0]+"\n"+barryperks[1]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 4:
                          c3perks = barryperks[0]+"\n"+barryperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 5:
                          c3perks = barryperks[1]+"\n"+barryperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 6:
                          c3perks = barryperks[0]+"\n"+barryperks[1]+"\n"+barryperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if perksc3 == "french_bread_gud":
                          perksc3 = c3perks
                      if c3perks != perksc3:
                          c3perks = perksc3
                  if c3 == "Diana":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c3perks = dianaperks[0]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 1:
                          c3perks = dianaperks[1]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 2:
                          c3perks = dianaperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 3:
                          c3perks = dianaperks[0]+"\n"+dianaperks[1]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 4:
                          c3perks = dianaperks[0]+"\n"+dianaperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 5:
                          c3perks = dianaperks[1]+"\n"+dianaperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 6:
                          c3perks = dianaperks[0]+"\n"+dianaperks[1]+"\n"+dianaperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if perksc3 == "french_bread_gud":
                          perksc3 = c3perks
                      if c3perks != perksc3:
                          c3perks = perksc3
                  if c3 == "Diaz":
                      AAAA = random.randint(0, 2)
                      if AAAA == 0:
                          c3perks = diazperks[0]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 1:
                          c3perks = diazperks[1]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 2:
                          c3perks = diazperks[0]+"\n"+diazperks[1]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                  if c3 == "Cole the Miner":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c3perks = coleperks[0]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 1:
                          c3perks = coleperks[1]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 2:
                          c3perks = coleperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 3:
                          c3perks = coleperks[0]+"\n"+coleperks[1]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 4:
                          c3perks = coleperks[0]+"\n"+coleperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 5:
                          c3perks = coleperks[1]+"\n"+coleperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 6:
                          c3perks =  coleperks[0]+"\n"+coleperks[1]+"\n"+coleperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if perksc3 == "french_bread_gud":
                          perksc3 = c3perks
                      if c3perks != perksc3:
                          c3perks = perksc3
                  if c3 == "Foxy":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c3perks = foxyperks[0]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 1:
                          c3perks = foxyperks[1]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 2:
                          c3perks = foxyperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 3:
                          c3perks = foxyperks[0]+"\n"+foxyperks[1]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 4:
                          c3perks = foxyperks[0]+"\n"+foxyperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 5:
                          c3perks = foxyperks[1]+"\n"+foxyperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 6:
                          c3perks = foxyperks[0]+"\n"+foxyperks[1]+"\n"+foxyperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if perksc3 == "french_bread_gud":
                          perksc3 = c3perks
                      if c3perks != perksc3:
                          c3perks = perksc3
                  if c3 == "Marina":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c3perks = marinaperks[0]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 1:
                          c3perks = marinaperks[1]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 2:
                          c3perks = marinaperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 3:
                          c3perks = marinaperks[0]+"\n"+marinaperks[1]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 4:
                          c3perks = marinaperks[0]+"\n"+marinaperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 5:
                          c3perks = marinaperks[1]+"\n"+marinaperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 6:
                          c3perks = marinaperks[0]+"\n"+marinaperks[1]+"\n"+marinaperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if perksc3 == "french_bread_gud":
                          perksc3 = c3perks
                      if c3perks != perksc3:
                          c3perks = perksc3
                  if c3 == "Paul":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c3perks = paulperks[0]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 1:
                          c3perks = paulperks[1]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 2:
                          c3perks = paulperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 3:
                          c3perks = paulperks[0]+"\n"+paulperks[1]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 4:
                          c3perks = paulperks[0]+"\n"+paulperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 5:
                          c3perks = paulperks[1]+"\n"+paulperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if AAAA == 6:
                          c3perks = paulperks[0]+"\n"+paulperks[1]+"\n"+paulperks[2]
                          if perksc3 != "french_bread_gud":
                              print(perksc3)
                          else:
                              print(c3perks)
                      if perksc3 == "french_bread_gud":
                          perksc3 = c3perks
                      if c3perks != perksc3:
                          c3perks = perksc3
                  if c3 == "Scorpius":
                      c3perks = scorpiusperks
                  if c3 == "Derpy":
                      c3perks = derpyperks
                  if c3 == "Jerry":
                      c3perks = jerryperks
              if AAA == "4":
                  if c4 == "Aatrox":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c4perks = aatroxperks[0]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 1:
                          c4perks = aatroxperks[1]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 2:
                          c4perks = aatroxperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 3:
                          c4perks = aatroxperks[0]+"\n"+aatroxperks[1]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 4:
                          c4perks = aatroxperks[0]+"\n"+aatroxperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 5:
                          c4perks = aatroxperks[1]+"\n"+aatroxperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 6:
                          c4perks = aatroxperks[0]+"\n"+aatroxperks[1]+"\n"+aatroxperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if perksc4 == "french_bread_gud":
                          perksc4 = c4perks
                      if c4perks != perksc4:
                          c4perks = perksc4
                  if c4 == "Barry the Wizard":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c4perks = barryperks[0]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 1:
                          c4perks = barryperks[1]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 2:
                          c4perks = barryperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 3:
                          c4perks = barryperks[0]+"\n"+barryperks[1]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 4:
                          c4perks = barryperks[0]+"\n"+barryperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 5:
                          c4perks = barryperks[1]+"\n"+barryperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 6:
                          c4perks = barryperks[0]+"\n"+barryperks[1]+"\n"+barryperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if perksc4 == "french_bread_gud":
                          perksc4 = c4perks
                      if c4perks != perksc4:
                          c4perks = perksc4
                  if c4 == "Diana":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c4perks = dianaperks[0]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 1:
                          c4perks = dianaperks[1]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 2:
                          c4perks = dianaperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 3:
                          c4perks = dianaperks[0]+"\n"+dianaperks[1]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 4:
                          c4perks = dianaperks[0]+"\n"+dianaperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 5:
                          c4perks = dianaperks[1]+"\n"+dianaperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 6:
                          c4perks = dianaperks[0]+"\n"+dianaperks[1]+"\n"+dianaperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if perksc4 == "french_bread_gud":
                          perksc4 = c4perks
                      if c4perks != perksc4:
                          c4perks = perksc4
                  if c4 == "Diaz":
                      AAAA = random.randint(0, 2)
                      if AAAA == 0:
                          c4perks = diazperks[0]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 1:
                          c4perks = diazperks[1]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 2:
                          c4perks = diazperks[0]+"\n"+diazperks[1]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                  if c4 == "Cole the Miner":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c4perks = coleperks[0]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 1:
                          c4perks = coleperks[1]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 2:
                          c4perks = coleperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 3:
                          c4perks = coleperks[0]+"\n"+coleperks[1]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 4:
                          c4perks = coleperks[0]+"\n"+coleperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 5:
                          c4perks = coleperks[1]+"\n"+coleperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 6:
                          c4perks =  coleperks[0]+"\n"+coleperks[1]+"\n"+coleperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if perksc4 == "french_bread_gud":
                          perksc4 = c4perks
                      if c4perks != perksc4:
                          c4perks = perksc4
                  if c4 == "Foxy":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c4perks = foxyperks[0]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 1:
                          c4perks = foxyperks[1]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 2:
                          c4perks = foxyperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 3:
                          c4perks = foxyperks[0]+"\n"+foxyperks[1]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 4:
                          c4perks = foxyperks[0]+"\n"+foxyperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 5:
                          c4perks = foxyperks[1]+"\n"+foxyperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 6:
                          c4perks = foxyperks[0]+"\n"+foxyperks[1]+"\n"+foxyperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if perksc4 == "french_bread_gud":
                          perksc4 = c4perks
                      if c4perks != perksc4:
                          c4perks = perksc4
                  if c4 == "Marina":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c4perks = marinaperks[0]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 1:
                          c4perks = marinaperks[1]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 2:
                          c4perks = marinaperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 3:
                          c4perks = marinaperks[0]+"\n"+marinaperks[1]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 4:
                          c4perks = marinaperks[0]+"\n"+marinaperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 5:
                          c4perks = marinaperks[1]+"\n"+marinaperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 6:
                          c4perks = marinaperks[0]+"\n"+marinaperks[1]+"\n"+marinaperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if perksc4 == "french_bread_gud":
                          perksc4 = c4perks
                      if c4perks != perksc4:
                          c4perks = perksc4
                  if c4 == "Paul":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c4perks = paulperks[0]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 1:
                          c4perks = paulperks[1]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 2:
                          c4perks = paulperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 3:
                          c4perks = paulperks[0]+"\n"+paulperks[1]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 4:
                          c4perks = paulperks[0]+"\n"+paulperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 5:
                          c4perks = paulperks[1]+"\n"+paulperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if AAAA == 6:
                          c4perks = paulperks[0]+"\n"+paulperks[1]+"\n"+paulperks[2]
                          if perksc4 != "french_bread_gud":
                              print(perksc4)
                          else:
                              print(c4perks)
                      if perksc4 == "french_bread_gud":
                          perksc4 = c4perks
                      if c4perks != perksc4:
                          c4perks = perksc4
                  if c4 == "Scorpius":
                      c4perks = scorpiusperks
                  if c4 == "Derpy":
                      c4perks = derpyperks
                  if c4 == "Jerry":
                      c4perks = jerryperks
              if AAA == "5":
                  if c5 == "Aatrox":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c5perks = aatroxperks[0]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 1:
                          c5perks = aatroxperks[1]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 2:
                          c5perks = aatroxperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 3:
                          c5perks = aatroxperks[0]+"\n"+aatroxperks[1]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 4:
                          c5perks = aatroxperks[0]+"\n"+aatroxperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 5:
                          c5perks = aatroxperks[1]+"\n"+aatroxperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 6:
                          c5perks = aatroxperks[0]+"\n"+aatroxperks[1]+"\n"+aatroxperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if perksc5 == "french_bread_gud":
                          perksc5 = c5perks
                      if c5perks != perksc5:
                          c5perks = perksc5
                  if c5 == "Barry the Wizard":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c5perks = barryperks[0]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 1:
                          c5perks = barryperks[1]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 2:
                          c5perks = barryperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 3:
                          c5perks = barryperks[0]+"\n"+barryperks[1]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 4:
                          c5perks = barryperks[0]+"\n"+barryperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 5:
                          c5perks = barryperks[1]+"\n"+barryperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 6:
                          c5perks = barryperks[0]+"\n"+barryperks[1]+"\n"+barryperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if perksc5 == "french_bread_gud":
                          perksc5 = c5perks
                      if c5perks != perksc5:
                          c5perks = perksc5
                  if c5 == "Diana":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c5perks = dianaperks[0]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 1:
                          c5perks = dianaperks[1]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 2:
                          c5perks = dianaperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 3:
                          c5perks = dianaperks[0]+"\n"+dianaperks[1]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 4:
                          c5perks = dianaperks[0]+"\n"+dianaperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 5:
                          c5perks = dianaperks[1]+"\n"+dianaperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 6:
                          c5perks = dianaperks[0]+"\n"+dianaperks[1]+"\n"+dianaperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if perksc5 == "french_bread_gud":
                          perksc5 = c5perks
                      if c5perks != perksc5:
                          c5perks = perksc5
                  if c5 == "Diaz":
                      AAAA = random.randint(0, 2)
                      if AAAA == 0:
                          c5perks = diazperks[0]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 1:
                          c5perks = diazperks[1]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 2:
                          c5perks = diazperks[0]+"\n"+diazperks[1]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                  if c5 == "Cole the Miner":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c5perks = coleperks[0]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 1:
                          c5perks = coleperks[1]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 2:
                          c5perks = coleperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 3:
                          c5perks = coleperks[0]+"\n"+coleperks[1]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 4:
                          c5perks = coleperks[0]+"\n"+coleperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 5:
                          c5perks = coleperks[1]+"\n"+coleperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 6:
                          c5perks =  coleperks[0]+"\n"+coleperks[1]+"\n"+coleperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if perksc5 == "french_bread_gud":
                          perksc5 = c5perks
                      if c5perks != perksc5:
                          c5perks = perksc5
                  if c5 == "Foxy":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c5perks = foxyperks[0]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 1:
                          c5perks = foxyperks[1]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 2:
                          c5perks = foxyperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 3:
                          c5perks = foxyperks[0]+"\n"+foxyperks[1]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 4:
                          c5perks = foxyperks[0]+"\n"+foxyperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 5:
                          c5perks = foxyperks[1]+"\n"+foxyperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 6:
                          c5perks = foxyperks[0]+"\n"+foxyperks[1]+"\n"+foxyperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if perksc5 == "french_bread_gud":
                          perksc5 = c5perks
                      if c5perks != perksc5:
                          c5perks = perksc5
                  if c5 == "Marina":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c5perks = marinaperks[0]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 1:
                          c5perks = marinaperks[1]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 2:
                          c5perks = marinaperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 3:
                          c5perks = marinaperks[0]+"\n"+marinaperks[1]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 4:
                          c5perks = marinaperks[0]+"\n"+marinaperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 5:
                          c5perks = marinaperks[1]+"\n"+marinaperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 6:
                          c5perks = marinaperks[0]+"\n"+marinaperks[1]+"\n"+marinaperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if perksc5 == "french_bread_gud":
                          perksc5 = c5perks
                      if c5perks != perksc5:
                          c5perks = perksc5
                  if c5 == "Paul":
                      AAAA = random.randint(0, 6)
                      if AAAA == 0:
                          c5perks = paulperks[0]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 1:
                          c5perks = paulperks[1]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 2:
                          c5perks = paulperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 3:
                          c5perks = paulperks[0]+"\n"+paulperks[1]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 4:
                          c5perks = paulperks[0]+"\n"+paulperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 5:
                          c5perks = paulperks[1]+"\n"+paulperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if AAAA == 6:
                          c5perks = paulperks[0]+"\n"+paulperks[1]+"\n"+paulperks[2]
                          if perksc5 != "french_bread_gud":
                              print(perksc5)
                          else:
                              print(c5perks)
                      if perksc5 == "french_bread_gud":
                          perksc5 = c5perks
                      if c5perks != perksc5:
                          c5perks = perksc5
                  if c5 == "Scorpius":
                      c5perks = scorpiusperks
                  if c5 == "Derpy":
                      c5perks = derpyperks
                  if c5 == "Jerry":
                      c5perks = jerryperks
          if AA == "candidates":
              print("The current candidates are:", c1+",", c2+",", c3+",", c4+",", "and "+c5)
      while voteNow == 1:
          aaaa = input("Who would you like to vote for? (just use a number from 1 to 5 corresponding to the mayor you want to vote for) ")
          if aaaa == "1":
              A = input("Are you sure you wish to vote for "+c1+"?")
              if A == "yes":
                  print("The Mayor is now "+c1)
                  cmayor = c1
                  if smayor != 0:
                      smayor = 0
                  cml = 1
                  voteNow = False
                  if perksc1 != "french_bread_gud":
                      tempperksm = perksc1
                  else:
                      tempperksm = c1perks
                  perksm = tempperksm
                  mayorElectionReset()
              if A == "no":
                  print("Please choose a mayor to vote for.")
          if aaaa == "2":
              A = input("Are you sure you wish to vote for "+c2+"?")
              if A == "yes":
                  print("The Mayor is now "+c2)
                  cmayor = c2
                  if smayor != 0:
                      smayor = 0
                  cml = 1
                  voteNow = False
                  if perksc2 != "french_bread_gud":
                      tempperksm = perksc2
                  else:
                      tempperksm = c2perks
                  perksm = tempperksm
                  mayorElectionReset()
              if A == "no":
                  print("Please choose a mayor to vote for.")
          if aaaa == "3":
              A = input("Are you sure you wish to vote for "+c3+"?")
              if A == "yes":
                  print("The Mayor is now "+c3)
                  cmayor = c3
                  if smayor != 0:
                      smayor = 0
                  cml = 1
                  voteNow = False
                  if perksc3 != "french_bread_gud":
                      tempperksm = perksc3
                  else:
                      tempperksm = c3perks
                  perksm = tempperksm
                  mayorElectionReset()
              if A == "no":
                  print("Please choose a mayor to vote for.")
          if aaaa == "4":
              A = input("Are you sure you wish to vote for "+c4+"?")
              if A == "yes":
                  print("The Mayor is now "+c4)
                  cmayor = c4
                  if smayor != 0:
                      smayor = 0
                  cml = 1
                  voteNow = False
                  if perksc4 != "french_bread_gud":
                      tempperksm = perksc4
                  else:
                      tempperksm = c4perks
                  perksm = tempperksm
                  mayorElectionReset()
              elif A == "no":
                  print("Please choose a mayor to vote for.")
          if aaaa == "5":
              A = input("Are you sure you wish to vote for "+c5+"?")
              if A == "yes":
                  print("The Mayor is now "+c5)
                  cmayor = c5
                  if smayor != 0:
                      smayor = 0
                  cml = 1
                  voteNow = False
                  if perksc5 != "french_bread_gud":
                      tempperksm = perksc5
                  else:
                      tempperksm = c5perks
                  perksm = tempperksm
                  mayorElectionReset()
              elif A == "no":
                  print("Please choose a mayor to vote for.")
          if (aaaa != "1" or aaaa != "2" or aaaa != "3" or aaaa != "4" or aaaa != "5" & cml != 0 & voteNow != False):
                  print("Im sorry i didn't get that can you please say it again?")
      mayorElectionReset()
  if A == "check mayor":
      if smayor != 0:
          print("The current mayor is "+smayor)
      else:
          print("The current mayor is "+cmayor)
  if A == "see perks":
      print(perksm)
      print("This is the tempperksm variable speaking tempperksm is equal to "+tempperksm)
  DD = random.randint(faddc,100)
  J = random.randint(1,1000)
  if A == "cl":
    print("commands are: \ncheck balance, play among us\nforage, catch fibsh, check stats\nsell fibsh, check gtime, explore\nfight, check coin multiplier, check stat multiplier\ncheck combat lvl, check combat xp left, check fibsh coin multiplier\ncheck fibsh stat multiplier\nckeck fibsh lvl, check fibsh xp left\ncheck farming coin multiplier, check farming stat multiplier, check farming lvl\ncheck farming xp left, farm, grind eyes\nsummon drag, dark auction, and tia")
  if A == "check balance":
    print(coins)
    gtime=gtime+1
  if A == "gib me coin":
    PP = input("how many coins do you want?")
    print(PP,"coins have been added to your bank account")
    coins=coins+int(PP)
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
                  print("you have completed your first task poggers")
          if Y == 4:
            print("your task is to align the engine output")
            TK = input("will you go do it or watch the cams?")
            if TK == "I will do it":
                TK2 = input("you complete the first part of this task will you do the seccond?")
                if TK2 == "yes":
                  print("you have completed your first task poggers")
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
    print("you break a tree")
    if C == 7:
      print("+1 strength")
      stats = stats+1
      gtime=gtime+1
  elif A == "catch fibsh":
    print("you catch fibsh")
    fibsh = fibsh+(10*fslm)
    gtime=gtime+1
    fxp=fxp+fxpg
  elif A == "sell fibsh":
    print("you ate", fibsh, "fibsh")
    coins = fibsh*100
    fibsh = 0
    gtime=gtime+1
    print("you now have", coins, "coin(s)")
  elif A == "+100 gtime":
    gtime=gtime+100
  elif A == "check gtime":
    print(gtime)
  elif A == "explore":
      X = random.randint(1,5)
      if X == 1:
          print("you stumble upon wheat and get 7 coins")
          coins = coins+7
          gtime=gtime+1
      if X == 2:
          if stats>1:
              print("you found a zombie and killed it, you got 9 coins")
              coins = coins+9
              stats = stats+1
              gtime=gtime+1
              cxp=cxp+5
          else:
              print("""you found and zombie and it killed you, you die, L
you also lose half of your coins, what a noob""")
              coins = coins/2
              gtime=gtime+1    
      if X == 3:
          print("you stumble upon a tree and break it, +1 stats and +2 coins")
          stats = stats+1
          coins = coins+1
          gtime=gtime+1
      if X == 4:
          if stats>20:
              print("you fight an enderman and kill it, +70 coins and +5 strength")
              stats=stats+5
              coins=coins+70
              gtime=gtime+1
          else:
              print("you find an enderman and try to fight it")
              print("you are not strong enough and almost die but you get lucky")
              print("someone comes and kills it so you survive")
              gtime=gtime+1
      if X == 5:
        print("you find a mine and collect ores, then some weird enemy appears")
        if stats>100:
            print("you kill it and it drops a weird watch, you decide to keep it")
            haswatch=haswatch+1
            gtime=gtime+1
            cxp=cxp+20
        else:
            print("you quickly realize that you can't fight it and decide to run away")
            gtime=gtime+1
  elif A == "fight":
          G = random.randint(1,2)
          if G == 1:
            print("you find a random zombie")
            if stats>=150:
                print("you kill it and gain some coins, +5 coins, +5 strength")
                coins=coins+5
                stats=stats+5
                gtime=gtime+1
                cxp=cxp+35
            if stats<150:
                  print("you died and lost half your coins")
                  coins=coins/2
                  gtime=gtime+1
          if G == 2:
              print("you find a spider and fight it")
              if stats>=160:
                print("you kill it, +6 coins, +6 strength")
                coins=coins+6
                stats=stats+6
                gtime=gtime+1
                cxp=cxp+12
              if stats<160:
                print("you died L you lost half your coins")
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
  if A == "check combat xp left":
    print(((csl+1)*1000)-cxp)
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
  if A == "check fibsh xp left":
    print(((fsl+1)*1000)-fxp)
  if fcm == 3:
    if (fxp*fslxp) == (10000*fslxp):
        fcm=fcm-2
  if faxp == 1000:
    print("you leveled up your farming to lvl 1 gratz and gained 10k coins")
    coins=coins+10000
    stats=stats+100
    fasl=fasl+1
    print("Next farming level is at 2000 farming xp")
  if faxp == (fasl+1)*1000:
    fasl=fasl+1
    faddc=faddc+4
    print("you leveled up your farming to lvl", fasl, "gratz and gained", 10*facm, "k coins")
    coins=coins+(10000*facm)
    stats=stats+(100*fasm)
    print("Next farming level is at", (fasl+1)*1000, "farming xp")
    print("your farming double drop chance is now", faddc, "dev note: later ill work on triple drop chance rn there is only double drop chance")
  if (fasl*faslxp) == (10*faslxp):
    faslxp=faslxp+1
    fasm=fasm+1
    facm=facm+1
    if fasl == 26:
      DD=random.randint(100,100)
  if A == "check farming coin multiplier":
    cls()
    print(f"Farming coin multiplier is {facm}")
  if A == "check farming stat multiplier":
    cls()
    print(f"Farming stat multiplier is {fasm}")
  if A == "check farming lvl":
    cls()
    print(faslxp)
  if A == "check farming xp left":
    cls()
    print(((fasl+1)*1000)-faxp)
  if cm == 3:
    if (cxp*cslxp) == (10000*cslxp):
        cm=cm-2
  if A == "farm":
    L = random.randint(1,1)
    if L == 1:
        if DD == 100:
          print("you farmed 2 pumpkin")
          faxp=faxp+2.4
          gtime=gtime+1
          coins=coins+4
        else:
          print("you farmed 1 pumpkins")
          faxp=faxp+1.2
          gtime=gtime+1
          coins=coins+2
  if A == "grind eyes":
        print("you stumble upon a portal")
        if csl>=12:
            D = random.randint(1,100)
            if D == 100:
              print("you decide to enter it, you find an enderman with a portal frame and kill it, you get a summoning eye")
              stats=stats+1
              coins=coins+15
              B = input("do you want to sell the eye?")
              if B == "yes" or B == "Yes":
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
              gtime=gtime+1
        else:
            print("A strange force prevents you from entering it")
  elif A == "summon drag":
    if eyes>=8:
        C = input("Are you sure?")
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
if(game == "wynncraft"):
   AC = input("What class do you choose(Archer, Warrior, Mage, Assassin, or Shaman)[this is case sensitive, or alternatively you can use numbers corresponding to the class ie 1 for archer, 2 for warrior ect ect.]")
   if AC == "Archer" or AC == 1:
         print("Archer class has been selected")
         chosenClass = "Archer"
   if AC == "Warrior" or AC == 2:
         print("Warrior class has been selected")
         chosenClass = "warrior"
   if AC == "Mage" or AC == 3:
         print("Mage class has been selected")
         chosenClass = "Mage"
   if AC == "Assassin" or AC == 4:
         print("Assassin class has been selected")
         chosenClass = "Assassin"
   if AC == "Shaman" or AC == 5:
         print("Shaman class has been selected")
         chosenClass = "Shaman"
   AB = input("Do you wish to skip the tutorial?")
   if AB == "yes":
      gameRun = True
      ts = "yes"
   if AB == "no":
      gameRun= True
      ts = "no"
   while(gameRun == True):
         if(ts=="no"):
               if(tR==0):
                     print("Caracan Driver: Agh!")
                     print("Tasim: Hey,", spname,"! You alright in there? Looks like we hit something.")
                     time.sleep(2)
                     print("Caravan Driver: I swear I hit this same dang boulder every\n time I make this trip.")
                     time.sleep(2)
                     print("Tasim: Does this mean we have to walk all the way to Ragni from here?")
                     time.sleep(2)
                     print("Caravan Driver: It's not that far, it's just a straight path from here. Here,\n take these as a partial refund for the journey.")
                     print("[+8 Emeralds]")
                     em=em+8
                     time.sleep(2)
                     print("Aledar: "+spname+", if you're ready, let's get moving")
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
                           print("Soldier: There's a cave right there. Those often contain useful loot, \nI'd give it a try if I were you.\n[Enter the cave and find some armor]")
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
                     print("Tasim: That could work..."+spname+", use command break on the rock to break it!")
                     AAA = input("Enter a command.")
                     if AAA=="break":
                           time.sleep(2)
                           print("*CRACK*")
                           print("*CRASH*")
                           print("Aledar It worked! Now we can reach that chest.")
                     if chosenClass == "Warrior":
                           print("[+1 Unitentified helmet]\n[+2 Copper Ingot]")
                           uh=1
                           ci=2
                           time.sleep(3)
                           print("Aledar: I think that's all we needed , let's get out")
                           print("Go through the exit to leave the cave")
                     if chosenClass == "Mage":
                           print("[+1 Unitentified helmet]\n[+2 Copper Ingot]")
                           uh=1
                           time.sleep(3)
                           print("Aledar: I think that's all we needed , let's get out")
                           print("Go through the exit to leave the cave")
                     if chosenClass == "Warrior":
                           print("[+1 Unitentified helmet]\n[+2 Wheat String]")
                           uh=1
                           ws=2
                           time.sleep(3)
                           print("Aledar: I think that's all we needed , let's get out")
                           print("Go through the exit to leave the cave")
                     if chosenClass == "Archer":
                           print("[+1 Unitentified helmet]\n[+2 Wheat String]")
                           uh=1
                           ws=2
                           time.sleep(3)
                           print("Aledar: I think that's all we needed , let's get out")
                           print("Go through the exit to leave the cave")
                     if chosenClass == "Assassin":
                           print("[+1 Unitentified helmet]\n[+2 Copper Ingot]")
                           uh=1
                           ci=2
                           time.sleep(3)
                           print("Aledar: I think that's all we needed , let's get out")
                           print("Go through the exit to leave the cave")
                     if chosenClass == "Shaman":
                           print("[+1 Unitentified helmet]\n[+2 Gudgeon Oil]")
                           uh=1
                           go=2
                           time.sleep(3)
                           print("Aledar: I think that's all we needed , let's get out")
                           print("Go through the exit to leave the cave")
                     time.sleep(2)
                     print("Soldier: That looks like the stuff.")
                     time.sleep(2)
                     print("Soldier: Normally this place is pretty safe\nbut somehow a few corrupted clipped through.")
                     tR=1
         if(ts=="yes"):
               if (tR==0):
                     print("tutorial has been skipped")
                     print("[You are now entering Ragni]")
                     tR=1