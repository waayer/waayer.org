#importing and loading
import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()

#grabs the url and api key from .env and sets them as variables
#uses the JF_API variable to add the api key to JF_HEADERS so the api will accept the requests
JELLYFIN_URL = os.getenv("JELLYFIN_URL")
JELLYFIN_KEY = os.getenv("JELLYFIN_KEY")
JF_HEADERS = {
    "Authorization": f'MediaBrowser Token="{JELLYFIN_KEY}"'
}

#grabs the url and api key from .env and sets them as variables
#uses the SEERR_KEY variable to add the api key to SEERR_HEADERS so the api will accept the requests
SEERR_URL = os.getenv("SEERR_URL")
SEERR_KEY = os.getenv("SEERR_KEY")
SEERR_HEADERS = {
    "X-API-Key": SEERR_KEY
}

IMMICH_URL = os.getenv("IMMICH_URL")
IMMICH_KEY = os.getenv("IMMICH_KEY")
IMMICH_HEADERS = {
    "X-API-Key": IMMICH_KEY
}

TRACEARR_URL = os.getenv("TRACEARR_URL")
TRACEARR_KEY = os.getenv("TRACEARR_KEY")
TRACEARR_HEADERS = {
    "Authorization": f"Bearer {TRACEARR_KEY}"
}

#SONARR_URL = os.getenv("SONARR_URL")
#SONARR_KEY = os.getenv("SONARR_KEY")
#SONARR_HEADERS = {
#    "Authorization": f"Bearer {SONARR_KEY}"
#}

#jellyfin function that grabs the url from variable and uses headers to insert the api key into the http/api request and then filters the data only keeping MovieCount EpisodeCount and SongCount
def jellyfin():
    response = requests.get(f"{JELLYFIN_URL}/Items/Counts", headers=JF_HEADERS, timeout=5)
    data = response.json()
    return {
        "MovieCount": data["MovieCount"],
        "EpisodeCount": data["EpisodeCount"],
        "SongCount": data["SongCount"]
    }

#seerr function that when run querys the api and filters out results only keeping total, pending and approved
def seerr():
    response = requests.get(f"{SEERR_URL}/api/v1/request/count", headers=SEERR_HEADERS, timeout=5)
    data = response.json()
    return {
        "RequestsTotal": data["total"],
        "RequestsPending": data["pending"],
        "RequestsApproved": data["approved"],
    }

#immich function that grabs photo/video counts from /statistics and disk usage from /storage, then merges both into one dict
def immich():
    response = requests.get(f"{IMMICH_URL}/api/server/statistics", headers=IMMICH_HEADERS, timeout=5) #this calls the immich api to get the server stats (photos and videos)
    data = response.json()

    response2 = requests.get(f"{IMMICH_URL}/api/server/storage", headers=IMMICH_HEADERS, timeout=5)  # This calls the Immich API to get system storage info.
    data2 = response2.json()

    return {
        "Photos": data["photos"],
        "Videos": data["videos"],
        "Disk": data2["diskUse"],
        "DiskAv": data2["diskAvailable"]
    }

def tracearr():
    response = requests.get(f"{TRACEARR_URL}/api/v1/public/stats", headers=TRACEARR_HEADERS, timeout=5)
    data = response.json()

    return {
        "ActiveStreams": data["activeStreams"],
        "TotalSessions": data["totalSessions"],
        "TotalUsers": data["totalUsers"]
    }

#if you want to use this you need sonarr v5 which is currently in beta
#def sonarr():
#    response = requests.get(f"{SONARR_URL}/api/v5/statistics", headers=SONARR_HEADERS, timeout=5)
#    data = response.json()
#
#    return {
#        "SeriesCount": data["seriesCount"],
#    }

#function that grabs the data from the service functions and sets it in stats{}
def results():
    stats = {}
    stats.update(jellyfin())
    stats.update(seerr())
    stats.update(immich())
    stats.update(tracearr())
    #stats.update(sonarr())
    #sends the data in stats{} to a .json file at ./website/stats.json
    #the reason it sends the data to ./website/stats.json is so caddy can serv the file as the root folder for caddy is ./website because it it was this folder the .env would be exposed
    with open("./website/stats.json", "w") as f:
        json.dump(stats, f)
        print(stats) #debugging will remove at some point

    return stats

#runs everything
results()