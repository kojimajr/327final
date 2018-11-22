from objects.Session import Session
from inputVerification import isLegalServiceNumber
from inputVerification import isValidServiceNumber
from inputVerification import isLegalTicketAmount

'''
Runs the sellticket transaction

Takes command line inputs for the transaction. If they are valid it updates the currentSession object
with the transaction code that will later be printed to the transaction summary file. 

@Param currentSession: valid Session object with information on the current session 
'''
def sellticket(currentSession):
    service = input()
    number = input()

    if(isLegalServiceNumber(service) and isValidServiceNumber(service, currentSession) and isLegalTicketAmount(number)):
        currentSession.transactions.append("SEL " + service + " " + number + " " + "00000 **** 0") 
    else:
        print("Invalid Input")
    return