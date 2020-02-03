import re
import csv
import glob

# find the log files to open
all_logs = glob.glob('*.txt')

# content = []

# open the log files as read only
with open (all_logs[0], 'r') as log_file:

    log_reader = log_file.readlines()

    # line = re.sub(r'.*>', '', line)

    clean_log = str.maketrans("", "", "=-<>")

    log_reader = [s.translate(clean_log) for s in log_reader]
   
    print(log_reader[3:-5])

# match name of log file
filename = 'log-file' + '.csv'
new_csv = open(filename, 'w')

# double check that this is always the same distance
new_csv.writelines(log_reader[3:-5])
new_csv.close()