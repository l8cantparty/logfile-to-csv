
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
        # s = re.sub('[^0-9a-zA-Z]+', '', s)

import re
import glob

# open the log files
all_logs = glob.glob('*.txt')

log_lines = []

with open (all_logs[0], 'rt') as log_file:
    log = log_file.read()
    log = re.sub('[-=<>]', '', log)
    log.split('\n')

    # the above is working to remove special characters, unclear if the split is happening, suggest writing to file to check

    for log in log_file:

        log_lines.append(log)
    # for log_line in log_file:

        # first, let's remove characters we don't need
        # line_clean = re.sub('[-=<>]', '', log_line)
        # str.lower(line_clean)

        # log_lines.append(line_clean)
        
# only print the lines we need - we will use this later
# print(log_lines[1:-1])
print(log_lines)