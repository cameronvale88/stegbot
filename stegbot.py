#!/usr/bin/python3

num_processes=45 #change this number the number of processes desired. Then remove appropriate files from jobs list start
                 #from the end to match the num_processes variable


def parseArgs():
    import argparse
    from sys import argv
    import sys

    parser = argparse.ArgumentParser(epilog='Example: {} -i steg.jpg -o output.txt -w wordlist.txt'.format(argv[0]))
    parser._optionals.title = 'OPTIONS'
    parser.add_argument('-i', '--image', help='image', required=True)
    parser.add_argument('-o', '--output', help='output', required=True)
    parser.add_argument('-w', '--wordlist', help='wordlist', required=True)
    return parser.parse_args().image, parser.parse_args().output, parser.parse_args().wordlist 

def steghide1(file):
    from subprocess import call, DEVNULL
    from time import time
    import os
    import sys
    # print("process {} is runniing".format(num))
    proc_id=os.getpid()
    print("Executing our Task on Process: {}".format(proc_id))
    start=time()
    with open(file) as passwords:
        lines=passwords.readlines()
        for password in lines:
            cmd = 'steghide extract -sf {} -xf {} -p {}'.format(image, output, password)
            if call(cmd.split(), stdout = DEVNULL, stderr = DEVNULL) == 0:
                totalTime = time() - start
                timeFormat = 'seconds'
                if(totalTime >= 60):
                    totalTime = totalTime/60
                    timeFormat = 'minutes'
                    if(totalTime >= 3600):
                        totalTime = totalTime/60
                        timeFormat = 'hours'
                print("process {} is complete".format(num))
                print('[#] password: {}\n[ctrl + c] to stop'.format(password))
                print('[#] Finished : {0:.2f} {1}'.format(totalTime, timeFormat))
            


from concurrent import futures
import subprocess
import os
import signal
import time
pids=[]
executor=futures.ProcessPoolExecutor(max_workers=47)
image, output, wordlist = parseArgs()
#processes
#      1       2       3     4      5      6      7     8       9     10      11    12      13     14    15     16     17      18    19     20      21     22     23     24     25     26    27      28     29    30      31     32     33     34    35      36   37      38      39     40    41      42     43     44     45
jobs=['xaa', 'xab', 'xac', 'xad', 'xae', 'xaf', 'xag', 'xah', 'xai', 'xaj', 'xak', 'xal', 'xam', 'xan', 'xao', 'xap', 'xaq', 'xar', 'xas', 'xat', 'xau', 'xav', 'xaw', 'xax', 'xay', 'xaz', 'xba', 'xbb', 'xbc', 'xbd', 'xbe', 'xbf', 'xbg', 'xbh', 'xbi', 'xbj', 'xbk', 'xbl', 'xbm', 'xbn', 'xbo', 'xbp', 'xbq', 'xbr', 'xbs']
#will break wordlist into 45 smaller lists
lines=subprocess.check_output(["wc", "-l", wordlist]) 
num_lines=lines.decode()
num=int(num_lines[:-13])
divisor=int((num/num_processes)+1)
out=subprocess.check_output(["split", "-l", str(divisor), wordlist])
    
for file in jobs:
    pids.append(os.getpid())
    executor.submit(steghide1, file)
    os.system("rm {}".format(file))


while True:
    if os.path.exists(output):
        os.system("pidof python3 | xargs kill 2>/dev/null")
