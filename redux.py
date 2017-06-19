import geopy.distance
import dateutil.parser
import xml.etree.ElementTree as etree


class Entry(object):

    def __init__(self, time, lat, lng, alt, dist):
        self.time = time
        self.lat = lat
        self.lng = lng
        self.alt = alt
        self.dist = dist

    def __str__(self):
        return 'time: %s, lat: %.6f, lng: %.6f, alt: %.2f, dst:%.3f' % (
            self.time, self.lat, self.lng, self.alt, self.dist)

    def distance_from(self, other):
        return geopy.distance.vincenty(self.pos, other.pos).m

    def time_since(self, other):
        return (self.time - other.time).total_seconds()

    @property
    def pos(self):
        return self.lat, self.lng

    converters = dict(
        AltitudeMeters=(float, 'alt'),
        DistanceMeters=(float, 'dist'),
        LatitudeDegrees=(float, 'lat'),
        LongitudeDegrees=(float, 'lng'),
        Time=(dateutil.parser.parse, 'time'),
    )

    @classmethod
    def from_xml_node(cls, node):
        data_point = {}
        for info in node.getiterator():
            tag = info.tag.split('}')[-1]
            if tag in cls.converters:
                converter, tag_text = cls.converters[tag]
                data_point[tag_text] = converter(info.text.strip())
        return cls(**data_point)

    @classmethod
    def from_xml(cls, xml_source):
        tree = etree.parse(xml_source)
        root = tree.getroot()
        return [cls.from_xml_node(child) for child in root[0][0][1][4]]


while True:
    filename = input('The file to parse: ')

    entries = Entry.from_xml(filename)

    total = 0.0
    for prev, entry in zip(entries[:-1], entries[1:]):
        dx = entry.distance_from(prev)
        dt = entry.time_since(prev)
        total += dx
        print('Total: %.3f, Logged Dist: %.3f, dx: %.3f, dt: %.3f, '
              'Speed: %.1f' % (total, entry.dist, dx, dt, dx/dt if dt else 0))

    if 'n' != input('Parse another file? y/n: '):
        break
