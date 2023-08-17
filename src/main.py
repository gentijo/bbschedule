from typing import List

# Import required module
import random
import array

#
# TOURNEMENT
#   ROUND (multiple)
#    MATCH (MatchesPerRound)
#     Team A (Team Size)
#     Team B (Team Size)
#    BuyPlayers len(allPlayers) - (matchesPerRound * (team size *2))

allPlayerNames= {
    "Rob",
    "Ron",
    "John",
    "Debbie",
    "Matt",
    "Patti",
    "Shelia",
    "Mary",
    "Joe",
    "Hunter",
    "Gerry",
    "Blaine",
    "Brent",
    "Jill",
    "Chuck",
    "Roseanne",
    "Maddox",
    "Griffen",
}

allGamePlayers:['gamePlayer'] = list('gamePlayer')
teamSize = 3
maxMatchesPerRound = 2


class gamePlayer:

    def __init__(self, name:str):
        self.toPlayWith:{gamePlayer} = {}
        self.toPlayAginst:{gamePlayer} = {}
        self.name = name


    def addOtherGamePlayers(self, gamePlayers:{'gamePlayer'}):
        for name in gamePlayers:
            if not name == self.name:
                player = gamePlayers[name]
                self.toPlayWith[name]=player
                self.toPlayAginst[name]=player

    def removeToPlayWith(self, players:{'gamePlayer'}):
        for name in players:
            try:
                del self.toPlayWith[name]
            except:
                pass
            
    def removeToPlayAgainst(self, players:[]):
        for name in players:
            try:
                del self.toPlayAgainst[name]
            except:
                pass


class gameMatch:
    def __init__(self, round:'gameRound', team_a:{gamePlayer}, team_b:{gamePlayer}):
        self.team_a = team_a
        self.team_b = team_b

        player:gamePlayer
        for name in team_a:
            player:gamePlayer = team_a[name]

            player.removeToPlayWith(team_a)
            player.removeToPlayAgainst(team_b)
            round.hasPlayedInRound[player.name] = player

        for name in team_b:
            player:gamePlayer = team_b[name]

            player.removeToPlayWith(team_b)
            player.removeToPlayAgainst(team_a)
            round.hasPlayedInRound[player.name] = player


    def display(self):
        print("\tMatch")
        print("\t\t'Team A'")
        for name in self.team_a:
            print(f"\t\t\tPlayer: {name}")

        print("\t\t'Team B'")
        for name in self.team_b:
            print(f"\t\t\tPlayer: {name}")

class gameRound:
    def __init__(self):
        self.gameMatches:[] = list()
        self.buyPlayers:{gamePlayer} = dict()
        self.hasPlayedInRound:{gamePlayer} = dict()

    def addMatch(self, match:gameMatch):
        self.gameMatches.append(match)

    def addBuyPlayer(self, player ):
        self.buyPlayers[player.name] = player

    def display(self):
        print("Round: \r\n")
        for match in self.gameMatches:
            match.display()

        if (len(self.buyPlayers)):
            print("\tBuy Round Players:")
            for name in self.buyPlayers:
                print(f"\t\t{name}")



class tournementBuilder:

    #
    #
    #
    def __init__(self, allPlayers:[]):

        self.gamePlayers:{gamePlayer} = {}
        self.matchesPerRound = 2
        self.gameRounds:List[gameRound] = list()

        #
        # Init Game Players, allPlayers is a simple list of names
        for name in allPlayers:
            self.gamePlayers[name] = gamePlayer(name)

        #
        # Loop through game players, add in toPlayWith and toPlayAgainst
        #
        for name in self.gamePlayers:
            player = self.gamePlayers[name]
            player.addOtherGamePlayers(self.gamePlayers)

    #
    #
    #
    def calculateTeamA(self, round:gameRound) -> dict:
        # calculate team_a

        team:{gamePlayer} = {}

        names:[] = list(self.gamePlayers.keys())
        random.shuffle(names)

        for name in names:
            player:gamePlayer = self.gamePlayers[name]
            if (len(player.toPlayWith) < teamSize):
                continue
            
            if (name in round.hasPlayedInRound): continue

            team[player.name] = player
            for team_a_idx in range(teamSize-1):
                team[player.name]=player

            if len(team) >= teamSize:
                break

        return team
    
    #
    #
    #
    def calculateTeamB(self, team_a:{gamePlayer}, round:gameRound) -> dict:
        # calculate team b

        team:{gamePlayer} = {}

        names:[] = list(self.gamePlayers.keys())
        random.shuffle(names)


        for name in names:
            
            if len(team) >= teamSize:
                break

            player:gamePlayer = self.gamePlayers[name]

            if (player.name in round.hasPlayedInRound): continue

            #
            # If a player does not have enought ppl to play against
            # or the player is currently listed in Team A, movr on
            # to the next player.
            #
            if ((len(player.toPlayAginst) < teamSize-1) or player.name in team_a):
                continue

            team[player.name] = player

            for team_b_idx in range(teamSize-1):
                if len(team) >= teamSize:
                    break

                for name2 in player.toPlayAginst:
                    player2:gamePlayer = player.toPlayAginst[name2]
                    if player2.name in team_a:
                        continue
                    
                    if (player2.name in round.hasPlayedInRound):
                        continue

                    team[player2.name] = player2

                    if len(team) >= teamSize:
                        break


        return team
    
    #
    #
    #
    def buildRounds(self):   
        numRounds:int = int(len(self.gamePlayers) / (teamSize*2))

        for i in range(0, numRounds-1):
            round = gameRound()     
            for x in range(self.matchesPerRound):
                player:gamePlayer

                team_a:{gamePlayer} = self.calculateTeamA(round)
                team_b:{gamePlayer} = self.calculateTeamB(team_a, round)
                
                match = gameMatch(round, team_a, team_b)
                round.addMatch(match)

            for name in self.gamePlayers:
                if (name in round.hasPlayedInRound):
                    continue
                round.addBuyPlayer(self.gamePlayers[name])

            self.gameRounds.append(round)         

        print("\r\nRound Building complete")

    def display(self):
        print("\r\nTournement\r\n")
        for round in self.gameRounds:
            round.display()

if __name__ == '__main__':
    tournement = tournementBuilder(allPlayerNames)
    tournement.buildRounds()
    tournement.display()
