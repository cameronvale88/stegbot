## stegbot
An expriment to use multiprocessing from the concurrent library to attack ctf stegonagraphy challenges.

The goal is to split a wordlist into multiple smaller wordlists and create a dictionary attack for each list. This approach should 

unocver the password sooner, since we are not reading the wordlist in a purely linear approach.

Requirements: argparse, sys, concurrent, subprocess. Steghide must also be installed. Also, this will only run in a linux envrionment.

To use this program, open a terminal and run: python3 stegbot.py -i inputfile.jpg -o outputfile.jpg -w wordlist

When or if the password is found, the output will be printed to the screen. To stop the program press Ctrl+c. 

### WARNING: This can be very resource intensive!!! Please run in a virtual envionrment to test out first!!!

By default this program will create 45 child processes.
To change the number of processes there comments on which variables must be changed.


If you have any questions or suggestions please feel free to comment.
