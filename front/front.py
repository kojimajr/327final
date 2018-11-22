import sys

from transactions.deleteservice import deleteservice
from transactions.cancelticket import cancelticket
from transactions.changeticket import changeticket
from transactions.createservice import createservice
from transactions.login import login
from transactions.logout import logout
from transactions.sellticket import sellticket

from objects.Session import Session

'''
Main class that controls the front-end

Takes 2 arguments as the Valid Services List filename and Transaction Summary File filename.

Waits for standard input and then calls the corresponding transaction method.

'''

# used to call the corresponding command for the standard input
commandSwitch = {
    'deleteservice': deleteservice,
    'cancelticket': cancelticket,
    'changeticket': changeticket,
    'createservice': createservice,
    'sellticket': sellticket,
}

currentSession = None

filenameTransactions = sys.argv[2] # the filename to output a Transation Summary File into

filenameServices = sys.argv[1] # the filename of the Valid Services List to read from
fileServices = open(filenameServices, 'r')
servicesValid = []
for line in fileServices:
    servicesValid.append(line.strip('\n'))

for line in sys.stdin:
    line = line.rstrip()
    # if not logged in, login is the only valid command
    if not currentSession:
        if line == 'login':
            currentSession = login(servicesValid, filenameTransactions)
        else:
            print('Invalid Command')
    # if logged in, use command switch to do a transation on the current session
    else:
        if line in commandSwitch:
            command = commandSwitch[ line ]
            command(currentSession)
        # delete the currentSession on logout
        elif line == 'logout':
            logout(currentSession)
            currentSession = None
        else:
            print('Invalid Command')
