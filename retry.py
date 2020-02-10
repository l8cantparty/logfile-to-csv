# import regex, glob, csv modules
import re
import csv
import glob

# find the log files to open
all_logs = glob.glob('*.txt')

# open the log files as read only
with open (all_logs[0], 'r') as log_file:
    
    log_list = log_file.readlines()

    clean_string = str.maketrans('', '', '=-<>')

    log_list = [s.translate(clean_string) for s in log_list]

    # remove lines with uneeded content
    # figure out how to combine these
    log_list = [x for x in log_list if 'MSDKDecoderWithMCDemux' not in x]
    log_list = [x for x in log_list if 'Dump' not in x]

    # remove "Ticks = 216485[...]" from the beginning of each line 
    log_list = [x[52:] for x in log_list]

    # remove the extra space before every other line
    log_list = [x.lstrip() for x in log_list]
    log_list = [x.strip() for x in log_list]

    # a v janky way to fix line breaks and commas
    log_list = [x.replace('Frames dropped','\n Frames dropped') for x in log_list]
    log_list = [x.replace('Avg Prefetch',', Avg Prefetch') for x in log_list]

    # log_list = [x.split(':')[0] for x in log_list]
    # log_list = [x.split(':')[1] for x in log_list if ':' in x]


    print(log_list[3:])


header = ['Frames dropped during playback,','Preroll(ms),','Avg Prefetch(ms),','Avg Render(ms),','Avg Display FPS,\n']
# how to move header items to top

# works, but not ideal:

# match name of log file

filename = 'log-file' + '.csv'
new_csv = open(filename, 'w')

# double check that this is always the same distance
new_csv.writelines(header)
new_csv.writelines(log_list[3:])
new_csv.close()

# filename = 'log-file' + '.csv'

# # new_csv = open(filename, 'w')
# with open('filename','w') as new_csv:
#     csv_file_reader = csv.DictReader(new_csv)
#     # print(row['Frames'])
#         # print(row['speaker'])

#     # double check that this is always the same distance
#     new_csv.writeline(log_list[3:-5])