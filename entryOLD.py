import geopy.distance
import datetime as dt


class Entry(object):
    @staticmethod
    def distancecalc(x1, x2):
        coord_1 = (x1.pos[0], x1.pos[1])
        coord_2 = (x2.pos[0], x2.pos[1])
        return geopy.distance.vincenty(coord_1, coord_2).m

    @staticmethod
    def timecalc(x1, x2):
        a, b = x1.time, x2.time
        t1 = dt.datetime(a[0], a[1], a[2], a[3], a[4], int(a[5]))
        t2 = dt.datetime(b[0], b[1], b[2], b[3], b[4], int(b[5]))
        t1_decimal = float(a[5]-int(a[5]))
        t2_decimal = float(b[5]-int(b[5]))
        return (t2 - t1).total_seconds() + (t2_decimal - t1_decimal)

    def __init__(self, time, lat, lng, alt, dist):
        self.time = time
        self.pos = [lat, lng]
        self.alt = alt
        self.dist = dist

    def __str__(self):
        ymd = ('ymd: ' + str(self.time[0]) + ', ' +
               str(self.time[1]) + ', ' + str(self.time[2]))
        hms = (' hms: ' + str(self.time[3]) + ', ' +
               str(self.time[4]) + ', ' + str(self.time[5]))
        lat = ' lat: ' + str(self.pos[0])
        lng = ' lng: ' + str(self.pos[1])
        alt = ' alt: ' + str(self.alt)
        dst = ' dst: ' + str(self.dist)
        stringrepresentation = ymd + hms + lat + lng + alt + dst
        return stringrepresentation
