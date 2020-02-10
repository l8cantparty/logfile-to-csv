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

    # throw out line breaks
    log_list = [x.strip() for x in log_list]

    # a v janky way to fix line breaks and commas
    log_list = [x.replace('Frames dropped','\n Frames dropped').replace('Avg Prefetch',', Avg Prefetch').replace(' Frames dropped during playback: ','').replace(' Preroll(ms): ','').replace(' Avg Prefetch(ms): ','').replace(' Avg Render(ms): ','').replace(' Avg Display FPS: ','') for x in log_list]
    # log_list = [x.replace('Avg Prefetch',', Avg Prefetch') for x in log_list]

    print(log_list[3:])


header = ['Frames dropped during playback,','Preroll(ms),','Avg Prefetch(ms),','Avg Render(ms),','Avg Display FPS,\n']
# how to move header items to top

# improve by getting file name from the log file itself
filename = 'log-file' + '.csv'
new_csv = open(filename, 'w')

new_csv.writelines(header)
# skip the first 3 lines of the log sicne they are uneeded
new_csv.writelines(log_list[3:])
new_csv.close()
