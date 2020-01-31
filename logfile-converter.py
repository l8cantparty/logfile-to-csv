import re
import csv
import glob

# find the log files to open
all_logs = glob.glob('*.txt')

log_lines = []

# open the log files as read only
with open (all_logs[0], 'rt') as log_file:

    # read the files and store as "log"
    log = log_file.read()

    # for log in log_file:

    # split text at linebreaks
    log_line = log.split('\n')
    log_line = re.sub('[-=<>]', '', log)
    # log_line[4:8]

    for log in log_line:

        print(log)



filename = 'log-file' + '.csv'
new_csv = open(filename, 'w')

new_csv.write(log_line)
new_csv.close()


    # title, handle = s.split()


        # log = log_file.read()

        # header, cells = log.split(':')
        # log
        # log = re.sub('[-=<>]', '', log)
        # log.split('\n')
        # print(log)
    # the above is working to remove special characters, unclear if the split is happening, suggest writing to file to check

    # for log in log_file:

        # log_lines.append(log)
    # for log_line in log_file:

        # first, let's remove characters we don't need
        # line_clean = re.sub('[-=<>]', '', log_line)
        # str.lower(line_clean)

        # log_lines.append(line_clean)
        
# only print the lines we need - we will use this later
# print(log_lines[1:-1])
    


