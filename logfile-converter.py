import re
import csv
import glob

# find the log files to open
all_logs = glob.glob('*.txt')

# open the log files as read only
with open (all_logs[0], 'rt') as log_file:
    for line in log_file:

        # remove everything before the last >
        clean_line = re.sub(r'.*>', '', line)
        # remove uneeded special characters, dumps
        # learn to combine regex
        clean_line = re.sub('[-=<>]', '', clean_line)
        # clean_up = [line for log_file in line if not line.startswith('=')]

        # remove everything before the last > from the line
        # clean_line = re.sub(r'.*>', '', line).replace('=','').replace('-','').replace('Queue Dump','').replace(r'(*)','').strip()

        # clean_list = [clean_line for clean_line in line if not clean_line.startswith(('=','-'))]


        
        print(clean_line)



# filename = 'log-file' + '.csv'
# new_csv = open(filename, 'w')
# needs string not list
# new_csv.write(clean_line)
# new_csv.close()

