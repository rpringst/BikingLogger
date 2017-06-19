import xml.etree.ElementTree as ET


def processtimestring(time):
    year = int(time[:4])
    month = int(time[5:7])
    day = int(time[8:10])
    h = int(time[11:13])
    m = int(time[14:16])
    s = float(time[17:-6])
    return [year, month, day, h, m, s]

def parsethedata():
    time = []
    lat = []
    lng = []
    alt = []
    dist = []
    garbage = '{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}'
    filestring = input('The file to parse: ')
    outputstring = filestring[:-4] + '.txt'
    
    f = open(outputstring, 'w')
    
    tree = ET.parse(filestring)
    root = tree.getroot()
    
    for child in root[0][0][1][4]:
        for info in child:
            if (not info.text):
                for position in info:
                    f.write(position.tag.replace(garbage, '') + '\n')
                    f.write(position.text + '\n')
            else:
                f.write(info.tag.replace(garbage, '') + '\n')
                f.write(info.text + '\n')
    
    f.close()
    
    with open(outputstring) as f:
        for i, line in enumerate(f):
            if ((i+9) % 10 == 0):
                time.append(processtimestring(line[:-1]))
            elif ((i+7) % 10 == 0):
                lat.append(float(line[:-1]))
            elif ((i+5) % 10 == 0):
                lng.append(float(line[:-1]))
            elif ((i+3) % 10 == 0):
                alt.append(float(line[:-1]))
            elif ((i+1) % 10 == 0):
                dist.append(float(line[:-1]))
    return [time, lat, lng, alt, dist]
