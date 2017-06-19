#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ride.py
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

from entry import Entry

def initializationhelper(entries):
        info = []
        total = 0.0
        for prev, entry in zip(entries[:-1], entries[1:]):
            dx = entry.distance_from(prev)
            dt = entry.time_since(prev)
            total += dx
            print('Total: %.3f, Logged Dist: %.3f, dx: %.3f, dt: %.3f, '
                  'Speed: %.1f' % (total, entry.dist, dx, dt,
                                   dx/dt if dt else 0))
            info.append((total, entry.dist, dx, dt,
                                   dx/dt if dt else 0))
        return info

class Ride(object):
    def __init__(self, entries):
        self.entries = entries
        self.info = initializationhelper(self.entries)
        
    def printinfo(self):
        for line in self.info:
            print('Total: %.3f, Logged Dist: %.3f, dx: %.3f, dt: %.3f, '
                  'Speed: %.1f' % line)
    
    def printentries(self):
        for entry in self.entries:
            print(str(entry))
