from objects.Session import Session
from inputVerification import isLegalServiceNumber
from inputVerification import isValidServiceNumber
from inputVerification import isLegalDate
from inputVerification import isLegalServiceName

'''
Runs the deleteservice transaction
Takes command line inputs for the transaction. If they are valid, legal and the user has
sufficient permission, the function  updates the currentSession object with the transaction 
code that will later be printed to the transaction summary file. 
@Param currentSession: valid Session object with informtaion on the current session
'''
def deleteservice(currentSession):
    number = input()
    name = input()
    
    isValidNumber = isLegalServiceNumber(number) and isValidServiceNumber(number, currentSession)
    isValidName = isLegalServiceName(name)   
    
    #We now check validity of all input, as well as user permission
    if isValidNumber and isValidName and currentSession.isPlanner:
        currentSession.transactions.append("DEL " + number + " 0 00000 " + name + " 0")
        currentSession.servicesDeleted.append(number)
    else:
        print("Invalid Input")