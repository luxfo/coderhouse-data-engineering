import api.nbaApi as api

def etl():

    #Api Call
    pages = [1, 2, 3]

    dataTeams = []
    dataPlayers = []
    dataGames = []
    
    for p in pages:
        apiResponse = api.extractTeams({'page': p, 'per_page': 100})
        #Check if key exists and has data
        if 'data' in apiResponse and len(apiResponse['data']) > 0:
            dataTeams.append(apiResponse)

        apiResponse = api.extractPlayers({'page': p, 'per_page': 100})
        #Check if key exists and has data
        if 'data' in apiResponse and len(apiResponse['data']) > 0:
            dataPlayers.append(apiResponse)

        apiResponse = api.extractGames({'page': p, 'per_page': 100})
        #Check if key exists and has data
        if 'data' in apiResponse and len(apiResponse['data']) > 0:
            dataGames.append(apiResponse)

    print(dataTeams)
    print(dataPlayers)
    print(dataGames)
    