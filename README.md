## stegbot
An expriment to use multiprocessing from the concurrent library to attack ctf stegonagraphy dictionary attacks.

The idea is to split a wordlist into smaller wordlists and create a separate process for dictionary attacking each portion of the list.

Requirements: argparse, sys, concurrent, subprocess. Steghide must also be installed.

To use this program, open a terminal and run: python3 stegbot.py -i inputfile.jpg -o outputfile.jpg -w wordlist

When or if the password is found, the output will be printed to the screen. To stop the program press Ctrl+c. The other processes will run till completion unless the program is terminated with a Ctrl+c. 

### WARNING: This can be very resource intensive!!!

By default this program will create 45 child processes.
To change the number of processes there comments on which variables must be changed.


If you have any questions or suggestions please feel free to comment.
