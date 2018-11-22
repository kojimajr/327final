from objects.Session import Session
from inputVerification import isLegalServiceNumber
from inputVerification import isLegalDate
from inputVerification import isLegalServiceName
'''
Runs the createservice transaction
Takes command line inputs for the transaction. If they are valid, legal and the user has
sufficient permission, the function  updates the currentSession object with the transaction 
code that will later be printed to the transaction summary file. 
@Param currentSession: valid Session object with informtaion on the current session
'''
def createservice(currentSession):
    number = input()
    date = input()
    name = input()
    
    isValidNumber = isLegalServiceNumber(number) and number not in currentSession.servicesValid
    isValidDate = isLegalDate(date)
    isValidName = isLegalServiceName(name)
    
    #We now check validity of all input, as well as user permission
    if isValidNumber and isValidDate and isValidName and currentSession.isPlanner:
        currentSession.transactions.append("CRE " + number + " 0 00000 " + name + " " + date)
    else:
        print("Invalid Input")