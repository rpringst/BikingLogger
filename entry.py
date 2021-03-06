#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  entry.py
#
#  Copyright 2017 Robert Ringstad <robert@robert-desktop>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

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
