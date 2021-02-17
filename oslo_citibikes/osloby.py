import json
import requests
from geopy import distance
import sys
from mapbox import Geocoder

def check_availiability( station_id ):

    for i in range(len(stations)):

        check_station = availability[i] 
        
        if(check_station['station_id'] == station_id):

            if(check_station["is_renting"] and check_station["is_returning"]):
                print("Free space: {}".format(check_station['num_docks_available']))
                print("Number of bikes: {}".format(check_station['num_bikes_available']))
                



def check_api_status(request_status):
    """ Make sure that the api works"""

    if(request_status > 499):
        print("Server resonsible for fault\nError code: {}".format(request_status))
        exit()
    elif(request_status > 399 and request_status < 500):
        print("Client responsible for fault\nError code: {}".format(request_status))
        exit()
    elif(request_status > 299 and request_status < 400):
        print("Client need to feed additional info to complete request\nError code:{}".format(request_status))
        exit()



def calculate_nearest_station( coord_address ):
    """This function takes in a longitude and latitude
    and returns the station that is closest to that
    position"""
    
    shortest_dist = sys.maxsize
    station_id = -1
    
    for i in range(len(stations)):
        coord_station = (stations[i]["lat"], stations[i]["lon"])
        
        dist = distance.distance(coord_address, coord_station).m
        
        if(dist < shortest_dist):
            shortest_dist = dist
            station_id = i

    return stations[station_id], shortest_dist



def address_to_lat_lon(address):
    """ Get the address as a input, check if it is a valid address
    inside Oslo. If not get the user to give a valid data.
    then return the latitude and longitude.
    """
    
    collect = geocoder.forward(address, limit=1, bbox = (10.477751, 59.809311, 10.95139, 60.135107))
    collect = collect.json()
    while(len(collect['features']) == 0):
        print("No result in Oslo with that keyword")
        address = input("Write a new address: \n")
        collect = geocoder.forward(address, limit=1, bbox = (10.477751, 59.809311, 10.95139, 60.135107))
        collect = collect.json()
    
    degres = tuple(collect['features'][0]['center'][::-1])
    
    return degres


# Request different api and set up data    
headers = {
    'Client-Identifier':'privat-reiseplanlegger',
}

stations = requests.get('https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json', headers=headers)
availability = requests.get('https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json', headers=headers)

check_api_status(stations.status_code)
check_api_status(availability.status_code)
    
stations = stations.json()["data"]["stations"]
availability = availability.json()["data"]["stations"]

#geocoder = REMOVED 


scanner = input("Write address: \n")

stat, dist = calculate_nearest_station(address_to_lat_lon(scanner))
print("Distance to station: {}".format(dist))
check_availiability(stat['station_id'])



