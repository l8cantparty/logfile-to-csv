
# logfile = store the content of the text file
# to do: replace explict file name with glob

# open text file as read-only
# strip_text = ['=','-']


# with open('cosnolelog.txt', 'rt') as logfile:
    # log = logfile.read()

    # strip_text = ['Dump', 'Ticks']
    # print(log.strip())
# logfile = "adsflkdjfljs===a"
    # for line in logfile:
        # print(line)
    # print (logfile.strip( 'Ticks' ))
    # for line in logfile:
    # print to see that it's working
        # print(line)
        # revline = line.strip()
        # print(revline)

loglines = []
with open ('cosnolelog.txt', 'rt') as logfile:
    for logline in logfile:
        loglines.append(logline)
print(loglines) 
