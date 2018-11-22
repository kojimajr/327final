from objects.Session import Session
from inputVerification import isLegalServiceNumber
from inputVerification import isValidServiceNumber
from inputVerification import isLegalTicketAmount

'''
Runs the cancelticket transaction

Takes command line inputs for the transaction. If they are valid it updates the currentSession object
with the transaction code that will later be printed to the transaction summary file. 

@Param currentSession: valid Session object with information on the current session 
'''
def cancelticket(currentSession):
    service = input()
    number = input()

    if(isLegalServiceNumber(service) and isValidServiceNumber(service, currentSession) and isLegalTicketAmount(number)):
        number = int(number)
        validNumber = True # true by default for planner
        if not currentSession.isPlanner:
            canceled = 0
            if(service in currentSession.ticketsCanceled):
                canceled = currentSession.ticketsCanceled[service]
            # check that the new amount will not exceed 10 for ther serivce or 20 for total canceled
            validNumber = canceled + number <= 10 and currentSession.totalCanceled + number <= 20
        
        if validNumber:
            # update the tickets canceled for the service
            if(service not in currentSession.ticketsCanceled):
                currentSession.ticketsCanceled[service] = number
            else:
                currentSession.ticketsCanceled[service] += number
            currentSession.totalCanceled += number # update the total canceled
            currentSession.transactions.append("CAN " + service + " " + str(number) + " " + "00000 **** 0") 
        else:
            print("Invalid Input")
   
    else:
        print("Invalid Input")
    return