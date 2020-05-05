## stegbot
An expriment to use multiprocessing from the concurrent library to attack ctf stegonagraphy dictionary attacks

Requirements: argparse, sys, concurrent, subprocess. Steghide must also be installed.

To use this program, open a terminal and run: python3 stegbot.py -i inputfile.jpg -o outputfile.jpg -w wordlist

When or if the password is found, the output will be printed to the screen. To stop the program press Ctrl+c. The other processes will run till completion unless the program is terminated with a Ctrl+c. This can be very resource intensive.

If you have any questions or suggestions please feel free to comment.
