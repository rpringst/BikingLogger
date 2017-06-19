#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
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
from ride import Ride
import pickle


def parsefile():
    log = []

    while True:
        filename = input('The file to parse: ')

        entries = Entry.from_xml(filename)
        
        log.append(Ride(entries))
        print(len(log))
        if 'n' == input('Parse another .bin file? y/n: '):
            savefile = input('Output filename: ')
            pickle.dump(log, open(savefile, 'wb'))
            break


def loadrides():
    savefile = input('Input filename: ')
    rides = pickle.load(open('save.p', 'rb'))

    for log in rides:
        log.printinfo()
        log.printentries()


def main(args):
    parsefile() if 'y' == input('Parse .bin file? y/n: ') else 0

    loadrides() if 'y' == input('Load rides? y/n: ') else 0

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
