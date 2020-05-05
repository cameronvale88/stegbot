#!/usr/bin/python3


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
            cmd = 'steghide extract -sf {0} -xf {1} -p {2}'.format(image, output, password)
            if call(cmd.split(), stdout = DEVNULL, stderr = DEVNULL) == 0:
                print('[#] password: {}\n[ctrl + c] to stop'.format(proc_id))
                print("process {} is complete".format(num))
                totalTime = time() - start
                timeFormat = 'seconds'
                if(totalTime >= 60):
                    totalTime = totalTime/60
                    timeFormat = 'minutes'
                    if(totalTime >= 3600):
                        totalTime = totalTime/60
                        timeFormat = 'hours'
                print('[#] Finished : {0:.2f} {1}'.format(totalTime, timeFormat))
                sys.exit()
    executor.shutdown(wait=False)
    exit()            

from concurrent import futures
import subprocess
executor=futures.ProcessPoolExecutor(max_workers=47)
image, output, wordlist = parseArgs()
jobs=['xaa', 'xab', 'xac', 'xad', 'xae', 'xaf', 'xag', 'xah', 'xai', 'xaj', 'xak', 'xal', 'xam', 'xan', 'xao', 'xap', 'xaq', 'xar', 'xas', 'xat', 'xau', 'xav', 'xaw', 'xax', 'xay', 'xaz', 'xba', 'xbb', 'xbc', 'xbd', 'xbe', 'xbf', 'xbg', 'xbh', 'xbi', 'xbj', 'xbk', 'xbl', 'xbm', 'xbn', 'xbo', 'xbp', 'xbq', 'xbr', 'xbs', 'xbt', 'xbu',]
lines=subprocess.check_output(["wc", "-l", wordlist]) #will break wordlist into 45 smaller lists
num_lines=lines.decode()
num=int(num_lines[:-13])
divisor=int((num/45)+1)
out=subprocess.check_output(["split", "-l", str(divisor), wordlist])
    
for file in jobs:
    executor.submit(steghide1, file)

   
