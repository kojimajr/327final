'''
Class containing legality and validity of user input against
defined requirements and logical restrictions.
'''

'''
Checks if a given service number is legally correct according to specification.  
@Param service: given service number
'''
def isLegalServiceNumber(service):
    return (service[0] != '0'
        and len(service) == 5
        and service.isdigit())

'''
Checks if a given service number is valid for use in a transaction.  
@Param service: given service number
'''
def isValidServiceNumber(service, currentSession):
    return (service in currentSession.servicesValid
        and service not in currentSession.servicesDeleted)

'''
Checks if a given service name is legally correct according to specification.
@Param service: given service name
'''
def isLegalServiceName(name):
    return (len(name) >= 3
        and len(name) <= 39 
        and name[-1] != ' '
        and name[0] != ' '
        and name.replace(' ', '').isalnum())

'''
Checks if a given service date is logically correct and within a legal range.
@Param service: given date, in YYYYMMDD format
'''
def isLegalDate(date):
    return (len(date) == 8
        and date.isdigit()
        and int(date[0:4]) <= 2999 
        and int(date[0:4]) >= 1980
        and int(date[4:6]) <= 12 
        and int(date[4:6]) >= 1
        and int(date[6:]) <= 31 
        and int(date[6:]) >= 1)

'''
Checks if a given ticket amount is a real number within a legal range for use in transactions. 
@Param service: given number of tickets
'''
def isLegalTicketAmount(number):
    return (number.isdigit()
        and int(number) > 0 
        and int(number) <= 1000)