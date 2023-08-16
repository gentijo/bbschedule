from typing import List

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
        for player in players:
            del self.toPlayWith[player.name]
            
    def removeToPlayAgainst(self, players:[]):
        for player in players:
            del self.toPlayAgainst[player.name]


class gameMatch:
    def __init__(self, round:'gameRound', team_a:{gamePlayer}, team_b:{gamePlayer}):
        self.team_a = team_a
        self.team_b = team_b

        player:gamePlayer
        for player in team_a:
            player.removeToPlayWith(team_a)
            player.removeToPlayAgainst(team_b)
            round.hasPlayedInRound.append(player)

        for player in team_b:
            player.removeToPlayWith(team_b)
            player.removeToPlayAgainst(team_a)
            round.hasPlayedInRound.append(player)


    def displayMatch(self):
        print(",,'Team A'")
        for player in self.team_a:
            print(f"Player: {player}")

        print(",,'Team B'")
        for player in self.team_b:
            print(f"Player: {player}")

class gameRound:
    def __init__(self):
        self.gameMatches:[] = list()
        self.buyPlayers:{gamePlayer} = dict()
        self.hasPlayedInRound:{gamePlayer} = dict()

    def addMatch(self, match:gameMatch):
        self.gameMatches.append(match)

    def addBuyPlayer(self, player ):
        self.buyPlayers[player.name] = player

    def displayRound(self):
        pass



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

        for name in self.gamePlayers:
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

        for name in self.gamePlayers:
            player:gamePlayer = self.gamePlayers[name]

            if (player.name in round.hasPlayedInRound): continue

            if ((len(player.toPlayWith) < teamSize-1) and player.name not in team_a):
                continue

            team[player.name] = player

            for team_b_idx in range(teamSize-1):
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

        for i in range(0, 5):
            round = gameRound()
            
            for x in range(self.matchesPerRound):
                player:gamePlayer

                team_a:{gamePlayer} = self.calculateTeamA(round)
                team_b:{gamePlayer} = self.calculateTeamB(team_a, round)
                
                match = gameMatch(round, team_a, team_b)
                round.addMatch(match)

            for player in self.gamePlayers:
                if (player in self.gamePlayershasPlayedInRound):
                    continue
                round.addBuyPlayer(player)

                    



if __name__ == '__main__':
    builder = tournementBuilder(allPlayerNames)
    builder.buildRounds()
