import random
print("Hi Some of the features are still in the WIP phase, meaning that if something says '(WIP)' it means that it is not implemented into the game yet. Have fun, stay safe, and remember to update!")
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
c1perks = "None"
aatroxperks = ["1. Slayer XP Buff: Earn 25% more Slayer XP.", "2. Pathfinder: Gain rare drops 20% more often.", "3. SLASHED Pricing: Starting Slayer quests is half price."]
barryperks = ["1. Magic XP Boost: Gain 15% more Enchanting and  Alchemy XP.", "2. Arcane Catalyst: Spells deal 15% increased damage.", "3. Astral Negotiator: Enchanting and anvils costs -15% less experience."]
coleperks = ["1. Mining XP Buff: Earn 1.5x Mining experience", "2. Prospection: Mining minions work 25% faster.(minions are a WIP)", "3. Mining Fiesta: Starts a special event in Early Autumn. Earn 1.5x Mining exp, 2x drops and Unique Loot. Active only on public islands.(WIP, when added it should compound with perk no.1)"]
scorpiusperks = ["1.Bribe: If Scorpius wins and you voted for him, Mayor Scorpius will offer you 1,000,000 coins as a token of grattitude.\n2. Darker Auctions: Scorpius will intrude in Dark Auctions, increasing the number of rounds to 7 and offering special items.(WIP)"]
dianaperks = ["Pet XP Buff: Gain 35% more pet XP.", "Lucky!: Gain +25 Pet Luck(Pets are WIP)", "Mythological Ritual: Mayor Diana will sell the Griffin Pet, which lets you find Mythological Creatures and tons of unique items.(WIP)"]
diazperks = ["Barrier Street: Gain 25% more bank interest.(WIP)", "Shopping Spree: Increase daily NPC buy limits by 10x.(WIP)"]
foxyperks = ["Sweet Tooth: Grants +20% chance to get candy from mobs during the Spooky Festival.(WIP)", "Benevolence: Gain 2.5x gifts from the attack on Jerry's Workshop.(WIP)", "Extra Event: Schedules an extra event during the year.(WIP)"]
marinaperks = ["Fishing XP Buff: Gain 50% more fishing XP", "Luck of the Sea 2.0: Gain +15 Sea creature chance icon.png Sea Creature Chance.", "Fishing Festival: Start a special fishing event during the first 3 days of each month! Fish and fight dangerous Sharks and earn unique Shark loot."]
paulperks = ["EZPZ: Gain 10 extra bonus score in Dungeons.(WIP)", "Marauder: Dungeon reward chests are 20% cheaper.(WIP)", "Benediction: Blessings are 25% stronger.(WIP)"]
derpyperks = ["1. TURBO MINIONS!!!: Minions have double the output! \n2. AH CLOSED!!!: The Auction House will be closed while Derpy is elected!\n3. DOUBLE MOBS HP!!!: ALL monsters have double health!\n 4. MOAR SKILLZ!!!: Gain +50% more skill experience!(All of derpy's perks are a WIP)"]
jerryperks = ["1. Perkpocalypse: Activates all perks of another mayor every 18 SkyBlock days (6 hours).\n2. Statspocalypse: Increases all stats by 10%.\n3. Jerrypocalypse: Reveal hidden Jerries from logging, farming, mining, and killing mobs.(Perks 1 and 3 are a WIP)"]
def mayorElectionReset():
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
    aa = 0
    aaa = 0
    aaaa = 0
    cml = 0
    voteNow = False
    c1perks = "None"
mayors = ["Aatrox", "Barry the Wizard", "Cole the Miner", "Diana", "Diaz", "Foxy", "Marina", " Paul"]
smayors = ["Jerry", "Derpy", "Scorpius"]
smayor = "Nancy"
cmayor = "None"
game = "run"
while (game == "run"):
    a = input("What u wanna do? ")
    if a == "vote":
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
        c1 = "Aatrox"
        print("The current candidates are:", c1+",", c2+",", c3+",", c4+",", "and "+c5)
        pVoteConfirm = True
        while (pVoteConfirm == True):
            AA = input("What will you do in the election.(valid responses are: 'vote', 'see perks', and 'candidates' if you choose 'vote' you will be forced to vote) ")
            if AA == "vote":
                voteNow = True
            if AA == "see perks":
                AAA = input("Whos perks do you wish to see?(enter number corresponding to the candidate that you wish to see)")
                if AAA == "1":
                    if c1 == "Aatrox":
                        AAAA = random.randint(0, 6)
                        if AAAA == 0:
                            c1perks = aatroxperks[0]
                        if AAAA == 1:
                            c1perks = aatroxperks[1]
                        if AAAA == 2:
                            c1perks = aatroxperks[2]
                        if AAAA == 3:
                            c1perks = aatroxperks[0, 1]
                        if AAAA == 4:
                            c1perks = aatroxperks[0, 3]
                        if AAAA == 5:
                            c1perks = aatroxperks[1, 2]
                        if AAAA == 6:
                            c1perks == aatroxperks
                    if c1 == "Barry the WIzard":
                        AAAA = random.randint(0, 6)
                    if c1 == "Diana":
                        AAAA = random.randint(0, 6)
                    if c1 == "Diaz":
                        AAAA = random.randint(0, 2)
                    if c1 == "Cole the Miner":
                        AAAA = random.randint(0, 6)
                    if c1 == "Foxy":
                        AAAA = random.randint(0, 6)
                    if c1 == "Marina":
                        AAAA = random.randint(0, 6)
                    if c1 == "Paul":
                        AAAA = random.randint(0, 6)
                    if c1 == "Scorpius":
                        c1perks = scorpiusperks
                    if c1 == "Derpy":
                        c1perks = derpyperks
                    if c1 == "Jerry":
                        c1perks = jerryperks
                    print(c1perks)
                if AAA == "2":
                    print(c2perks)
                if AAA == "3":
                    print(c3perks)
                if AAA == "4":
                    print(c4perks)
                if AAA == "5":
                    print(c5perks)
            if AA == "candidates":
                c1 = "Aatrox"
                print("The current candidates are:", c1+",", c2+",", c3+",", c4+",", "and "+c5)
        if voteNow == True:
            cml = 1
        while cml == 1:
            aaaa = input("Who would you like to vote for? (just use a number from 1 to 5 corresponding to the mayor you want to vote for) ")
            if aaaa == "1":
                A = input("Are you sure you wish to vote for "+c1+"?")
                if A == "yes":
                    print("The Mayor is now "+c1)
                    cmayor = c1
                    if smayor != 0:
                        smayor = 0
                    cml = 0
                    voteNow = False
                    continue
                if A == "no":
                    print("Please choose a mayor to vote for.")
            if aaaa == "2":
                A = input("Are you sure you wish to vote for "+c2+"?")
                if A == "yes":
                    print("The Mayor is now "+c2)
                    cmayor = c2
                    if smayor != 0:
                        smayor = 0
                    cml = 0
                    voteNow = False
                    continue
                if A == "no":
                    print("Please choose a mayor to vote for.")
            if aaaa == "3":
                A = input("Are you sure you wish to vote for "+c3+"?")
                if A == "yes":
                    print("The Mayor is now "+c3)
                    cmayor = c3
                    if smayor != 0:
                        smayor = 0
                    cml = 0
                    voteNow = False
                    continue
                if A == "no":
                    print("Please choose a mayor to vote for.")
            if aaaa == "4":
                A = input("Are you sure you wish to vote for "+c4+"?")
                if A == "yes":
                    print("The Mayor is now "+c4)
                    cmayor = c4
                    if smayor != 0:
                        smayor = 0
                    cml = 0
                    voteNow = False
                    continue
                if A == "no":
                    print("Please choose a mayor to vote for.")
            if aaaa == "5":
                A = input("Are you sure you wish to vote for "+c5+"?")
                if A == "yes":
                    print("The Mayor is now "+c5)
                    cmayor = c5
                    if smayor != 0:
                        smayor = 0
                    cml = 0
                    voteNow = False
                    continue
                if A == "no":
                    print("Please choose a mayor to vote for.")
            if (aaaa != "1" or aaaa != "2" or aaaa != "3" or aaaa != "4" or aaaa != "5" & cml != 0 & voteNow != false):
                    print("Im sorry i didn't get that can you please say it again?")
        mayorElectionReset()
    if a == "check mayor":
        if smayor != 0:
            print("The current mayor is "+smayor)
        else:
            print("The current mayor is "+cmayor)
