# US Cities data acquired from https://simplemaps.com/data/us-cities
# Distance formulas acquired from https://simplemaps.com/resources/location-distance

import numpy as np
import pandas as pd
import os
from math import radians, cos, sin, asin, sqrt


# Distance between two lat/lng coordinates in km using the Haversine formula
def getDistanceFromLatLng(lat1, lng1, lat2, lng2, miles=False):  # use decimal degrees
    r = 6371  # radius of the earth in km
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    lat_dif = lat2-lat1
    lng_dif = radians(lng2-lng1)
    a = sin(lat_dif/2.0)**2+cos(lat1)*cos(lat2)*sin(lng_dif/2.0)**2
    d = 2*r*asin(sqrt(a))
    if miles:
        return d * 0.621371  # return miles
    else:
        return d  # return km


file_dir = os.path.dirname(__file__)  # defines the cur directory

uscities_fields = ['city_ascii', 'county_fips', 'state_id', 'lat', 'lng']  # define fields to read in
uscities = pd.read_csv("uscities.csv", usecols=uscities_fields)  # read the cities csv
uscities = uscities.rename(columns={'city_ascii': 'city'})  # rename column for brevity
uscities['city'] = uscities['city'].str.replace(' ', '')  # replace spaces
uscities['cityfips'] = [c + str(f) for c, f in zip(uscities['city'], uscities['county_fips'])]  # new field
micities = uscities[uscities.state_id == 'MI'].copy()  # subset US cities to MI cities, use a copy not view
micities['region'] = [cf + '_' + str(lg) + '_' + str(lt) for cf, lg, lt in
                           zip(micities['cityfips'], micities['lng'], micities['lat'])]  # format for RegionCenters

regioncenters = micities.filter(['region']).copy()  # copy for lookup of RegionCenters
# regioncenters.to_csv(file_dir + "/regioncenters.csv", header=False, index=False)  # write RegionCenters.csv

# duplicate cities into origin destination copies
micitiesorig = micities.filter(['cityfips', 'lat', 'lng']).copy()
micitiesdest = micitiesorig.copy()

# cross join the cities for every combination
micitiesorig['key'] = 1
micitiesdest['key'] = 1
odcities = pd.merge(micitiesorig.copy(), micitiesdest.copy(), on=['key'], suffixes=('_o', '_d'))
odcities = odcities.drop(columns=['key'])

# Calculate the distance between each region
odcities['dist'] = [getDistanceFromLatLng(lato, lngo, latd, lngd, True) for
                    lato, lngo, latd, lngd in
                    zip(odcities['lat_o'], odcities['lng_o'], odcities['lat_d'], odcities['lng_d'])]

# save only those within 50 miles of one another
odcities = odcities[odcities['dist'] <= 50]

odcities['latlong_o'] = [str(lato) + '_' + str(lngo) for
                         lato, lngo in
                           zip(odcities['lat_o'], odcities['lng_o'])]
odcities['latlong_d'] = [str(latd) + '_' + str(lngd) for
                         latd, lngd in
                           zip(odcities['lat_d'], odcities['lng_d'])]
# odcities = odcities.drop(columns=['lat_o', 'lng_o', 'lat_d', 'lng_d'])

# write file for use in simulation script
odcities.to_csv(file_dir + "/odcities.csv", header=True, index=True)

pd.set_option("max_columns", None)
# # print(micities)
# print(odcities)
print(file_dir)
