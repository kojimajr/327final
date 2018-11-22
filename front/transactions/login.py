import sys
from objects.Session import Session
'''
Runs the login transaction

Takes an input user type from the command line and verifies that it is user or planner. Then creates
a Session object for that user type with the program inputs.

@Param servicesValid: List of valid services for this session
@Param filenameTransactions: Name of transaction summary file that will be written to on logout
@return: A Session object for the new session 
'''
def login(servicesValid, filenameTransactions):
    # print('enter user type')
    for line in sys.stdin:
        line = line.rstrip()
        if(line != 'agent' and line != 'planner'):
            print('Invalid Login')
        else:
            return Session( (line == 'planner') , servicesValid, filenameTransactions)
    