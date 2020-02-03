import re
import csv
import glob

# find the log files to open
all_logs = glob.glob('*.txt')
# log_list = list()        

# open the log files as read only
with open (all_logs[0], 'rt') as log_file:
    log_reader = log_file.readlines()
    # log_reader = list(filter(None, log_reader))



    for line in log_reader:
        # log_reader = list(filter(None, log_reader))
        clean_line = line.split('\n')

        # remove everything before the last >
        # clean_line = re.sub(r'.*>', '', line)
        # remove additional special characters
        clean_line = re.sub('[-=<>]', '', line)
        # split at line breaks
        # a_line = clean_line.split('\n')
        # a_line = clean_line.split(':')

        # remove empty lines
        # a_line.split(':')
        print(clean_line)

        # clean_line = re.sub(r'.*>', '', line)


    # for line_count, line in enumerate(log_file[3:-5]):
        # print("Line {}: {}".format(line_count, line))
    # for line in log_file:
        # list(enumerate(line))
        # line = re.sub(r'.*>', '', line)

        # remove everything before the last >
        # clean_line = re.sub(r'.*>', '', line)
        # learn to combine regex    
        # line = re.sub('[-=<>]', '', line)

        # clean_line = clean_line.split('\n')

        # log_list.append(line.strip()) 

        # print(line)



filename = 'log-file' + '.csv'
new_csv = open(filename, 'w')
# needs string not list
new_csv.writelines(line)
new_csv.close()

# Get the all the lines in file in a list 
# log_list = list()        
# with open ("data.txt", "r") as myfile:
# for line in myfile:
# log_list.append(line.strip()) 
