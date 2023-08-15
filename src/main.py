
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

teamSize = 3
maxMatchesPerRound = 2


class gamePlayer:

    def __init__(self, name:str, allPlayers:[]):
        self.toPlayWith = []
        self.toPlayAginst = []

        for ap_name in allPlayers:
            if not ap_name == name:
                self.toPlayWith.append(ap_name)
                self.toPlayAginst.append(name)

        def removeToPlayWith(self, players:[]):
            for player in players:
                del self.toPlayWith(player)
            
        def removeToPlayAgainst(self, players[]):
            for player in players:
                del self.toPlayAgainst(player)


class gameMatch:
    def __init__(self):
        self.team_a = []
        self.team_b = []

    def setTeamA(self, team:[]):
        self.team_a=team
    
    def setTeamB(self, team[]):
        self.team_b = team

    def displayMatch(self):
        print(",,'Team A'")
        for player in self.team_a:
            print(f"Player: {player}")

        print(",,'Team B'")
        for player in self.team_b:
            print(f"Player: {player}")

class gameRound:
    def __init__(self):
        self.gameMatches:[]
        self.buyPlayers:[] 

    def addMatch(self, match:gameMatch):
        self.gameMatches = match

    def addBuyPlayer(self, player ):
        self.buyPlayers.append(player)

    def displayRound(self):
        pass



class tournementBuilder:

    def __init__(self, allPlayers:[]):
        self.gamePlayers:[]
        self.matchesPerRound = 2
        self.gameRounds:[]
    
        for name in allPlayers:
            self.gamePlayers.append(gamePlayer(name, allPlayers))

    def calculateTeamA(self):
        # calculate team_a
        for player in self.gamePlayers:
            if (len(player.toPlayWith) < teamSize):
                continue
            
            if (player in self.hasPlayedInRound): continue

            team_a.append(player)
            for team_a_idx in range(teamSize-1):
                team_a.append(player.toPlayWith[team_a_idx])
     
    def buildRounds(self):
        self.hasPlayedInRound:[]
        self.team_a:[]
        self.team_b:[]

        for x in range(self.matchesPerRound):
            player:gamePlayer


            # calculate team b
            for player in self.gamePlayers:
                team_b = []

                if (player in hasPlayedInRound): continue

                if ((len(player.toPlayWith) < teamSize-1) and player not in team_a):
                    continue

                team_b.append(player)
                for team_b_idx in range(teamSize-1):
                    for player2 in player.toPlayAginst:
                        if player2 in team_a:
                            continue
                        
                        if (player2 in hasPlayedInRound):
                            continue

                        team_b.append(player2)

                if len(team_b) == teamSize:
                    break
                
                for player in team_a:
                    player.removeToPlayWith(team_a)
                    player.removeToPlayAgainst(team_b)
                    hasPlayedInRound.append(player)

                for player in team_b
                    player.removeToPlayWith(team_b)
                    player.removeToPlayAgainst(team_a)
                    hasPlayedInRound.append(player)
                
                round = gameRound()
                match = gameMatch()
                match.setTeamA(team_a)
                match.setTeamB(team_b)
                round.addMatch(match)

                self.gameRounds.addMatch(match)

                for player in self.gamePlayers:
                    if (player in hasPlayedInRound):
                        continue
                    round.addBuyPlayer(player)

                    



