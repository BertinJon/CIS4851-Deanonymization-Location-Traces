# Work Breakdown
# 1. Define Classes & Methods Required
# 1.1 Classes
# 1.1.1 Location
# 1.1.2 Traveller
# 1.1.2.1 Move Method
# 1.1.2.2
# 2. Implement Classes & Methods
# 3. Structure data for export (pandas)

"""Example of Input:
user_000001;|163,31.7324327_120.9655657|181,31.7324327_120.9655657|
user_000010;|163,fe4c21d14228bd83d838ee6562332c0b|"""



class Geoloc:
    """Defines the size of a geography in a grid, and the number of rounds a traveler moves"""
    def __init__(self,  lat_min, lat_max, long_min, long_max, duration):
        self.lat_min = lat_min
        self.lat_max = lat_max
        self.long_min = long_min
        self.long_max = long_max
        self.start_time = 0
        self.end_time = duration


class Traveler:
    """ A person moving through the geographic location. Enters the location from the edge and moves randomly throughout
    the geography until they exit the geography"""
    TRAVELER_ID = 1

    def __init__(self, location):
        self.traveler_id = Traveler.TRAVELER_ID
        self.current_loc = ()  # A 3d tuple detailing x,y,time
        self.loc_hist = []  # an array of tuples detailing time and current coordinate
        self.location = location
        Traveler.TRAVELER_ID += 1

    def __str__(self):
        return ("Traveler ID:" + str(self.traveler_id))
        #print("Current Location:", self.current_loc)
        #print("Location Trace:", self.loc_hist)

    def startposition(self):
        pass

    def move(self):
        pass

    def postsocial(self):
        """ This is a random event where the traveler posts to a social media platform providing x/y/time at known
        points through their journey"""
        pass

# Do we need a class for geographic "zone" to simulate centroid? Or good with just each point?

print("{:05d}".format(1))

# Kansas boundaries
# 36.993073, -102.042070
# 39.887442, -94.928408

kansas = Geoloc(36.993073, 39.887442, -102.042070, -94.928408, 100)
dorthy = Traveler(kansas)

print(dorthy)


import numpy as np
point1 = (36.993073, -102.042070)
point2 = (39.887442, -94.928408)
point3 = np.add(point2, point1)

print(point3)