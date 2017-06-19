import dataparse as dp
from entry import Entry


exitflag = False

while not exitflag:
    [time, lat, lng, alt, dist] = dp.parsethedata()
    entries = [Entry(x, lat[i], lng[i],
                     alt[i], dist[i]) for i, x in enumerate(time)]
    
    prev = entries[0]
    total = 0.0
    for entry in entries:
        dx = Entry.distancecalc(prev, entry)
        dt = Entry.timecalc(prev, entry)
        total += dx
        print('Total: ' + str(total) + ', Logged Dist: ' + str(entry.dist) +
              ', dx: ' + str(dx) + ', dt: ' + str(dt), end="")
        if dt:
            print(', Speed: ' + str(dx/dt))
        else:
            print(', Speed: 0.0')
        prev = entry
    
    userinput = input('Parse another file? y/n: ')
    
    if userinput == 'n':
        exitflag = True
