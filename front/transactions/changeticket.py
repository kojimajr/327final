from objects.Session import Session
from inputVerification import isLegalServiceNumber, isValidServiceNumber, isLegalTicketAmount

'''
Runs the changeticket transaction

Takes command line inputs for the transaction. If they are valid it updates the currentSession object
with the transaction code that will later be printed to the stransaction summary file. 

@Param currentSession: valid Session object with informtaion on the current session 
'''
def changeticket(currentSession):
    currentService = input()
    newService = input()
    number = input()

    validCurrentService = isLegalServiceNumber(currentService) and isValidServiceNumber(currentService, currentSession)

    validNewService = isLegalServiceNumber(newService) and isValidServiceNumber(newService, currentSession)

    validNumber = (isLegalTicketAmount(number)
    and (currentSession.isPlanner or (currentSession.totalChanged + int(number)) <= 20))

    if validCurrentService and validNewService and validNumber:
        currentSession.transactions.append("CNG " + currentService + " " + number + " " + newService + " **** 0")
        if(not currentSession.isPlanner):
            currentSession.totalChanged += int(number)
    else:
        print("Invalid Input")

    return
