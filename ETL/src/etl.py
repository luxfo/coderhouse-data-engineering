import api.nbaApi as api

def etl():
    dataTeams = api.extractTeams()
    dataPlayers = api.extractPlayers()
    dataGames = api.extractGames()

    print(dataTeams)
    print(dataPlayers)
    print(dataGames)
    