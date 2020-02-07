import re
import csv
import glob

# find the log files to open
all_logs = glob.glob('*.txt')

# content = []

# open the log files as read only
with open (all_logs[0], 'r') as log_file:

    log_list = log_file.readlines()

    log_list = re.sub(r'.*>', '', log_list)

    clean_string = str.maketrans("", "", "=-<>")

    log_list = [s.translate(clean_string) for s in log_list]

    # log_list = list(filter('MSDKDecoderWithMCDemux', log_list)) 
    # remove lines with uneeded content
    # figure out how to combine these

    # consider using filter

    log_list = [x for x in log_list if "MSDKDecoderWithMCDemux" not in x]
    log_list = [x for x in log_list if "Dump" not in x]
    # log_list = log_list.lsplit('0')

# >>> stringlist[:] = [x for x in stringlist if "Two" not in x]
# >>> stringlist
# ['elementOne', 'elementThree']
# s = "this    is my long     sentence"
# print ' '.join(s.split(' ')[3:])
   
    print(log_list[3:-5])

# match name of log file
filename = 'log-file' + '.csv'
new_csv = open(filename, 'w')

# double check that this is always the same distance
new_csv.writelines(log_list[3:-5])
new_csv.close()