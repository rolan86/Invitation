import json

from invitation import conf

from operator import itemgetter
from math import sin, cos, acos
from math import radians as rd


class Invite(object):

    def __init__(self):
        self.OLAT = rd(conf.OLAT)
        self.OLON = rd(conf.OLON)
        self.r = conf.r

    def get_data(self, json_file):
        """Get data from the JSON source file"""
        try:
            with open(json_file) as f:
                return f.readlines()
        except IOError:
            print "Please check the JSON file path"
        except Exception as e:
            print str(e)

    def format_data(self, data):
        """Format data to get only specific data
        with respect to latitude, longitude, user_id
        and name"""
        formatted_data = []
        for line in data:
            dstr = json.loads(line)
            clat = float(dstr.get('latitude'))
            clon = float(dstr.get('longitude'))
            cid = dstr.get('user_id')
            cname = dstr.get('name')
            formatted_data.append(dict(
                zip(
                    ('latitude', 'longitude', 'user_id', 'name'),
                    (clat, clon, cid, cname)
                )
            ))
        return formatted_data

    def dist_calculation(self, lat, lon):
        """Function for radial distance calculation
        between two locations lat being latitude
        and lon being longitude"""
        lat = rd(lat)
        lon = rd(lon)
        del_phi = acos(
                    sin(lat)*sin(self.OLAT) +
                    cos(lat)*cos(self.OLAT)*cos(lon-self.OLON)
                )
        return round(del_phi*self.r, 2)

    def radius_check(self, distance, max_radius=100):
        """Function for radius check with default as 100 kms"""
        if distance <= max_radius:
            return True
        return False

    def get_invitees(self, formatted_data, max_radius=100):
        """Function to get matching invitee list within
        a specific indicated radius, 100kms being the default"""
        invitee_list = []
        for entry in formatted_data:
            clat = entry.get('latitude')
            clon = entry.get('longitude')
            cid = entry.get('user_id')
            cname = entry.get('name')
            distance = self.dist_calculation(clat, clon)
            if self.radius_check(distance, max_radius):
                invitee_list.append((cid, cname, distance))
        return sorted(invitee_list, key=itemgetter(0))
