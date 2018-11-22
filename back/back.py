'''
Back Office Script

Takes 4 arguments as the Central Services File filename, the Merged Transaction Summary Filename,
the new Central Services File filename,  and the new Valid Services File filename.

Runs automatically once started and will output files when successfull.
Logs a fatal error and exits immediately on invalid input.
'''
import sys

CSF_filename = sys.argv[1]
MTSF_filename = sys.argv[2]
new_CSF_filename = sys.argv[3]
VSF_filename = sys.argv[4]

# Represents a row of the Central Services File and holds/validates data. 
# Used in dictionary where service numbers are dictionary keys 
class ServiceData:
    def __init__(self, ticketCapacity, ticketsSold, serviceName, serviceDate):
        self.capacity = int(ticketCapacity)
        self.sold = int(ticketsSold)
        self.name = serviceName
        self.date = int(serviceDate)        
    
'''
Checks if a given service number is legally correct according to specification.  
@Param service: given service number
'''
def isLegalServiceNumber(service):
    return (service[0] != '0'
        and len(service) == 5
        and service.isdigit())

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


        
# Read existing central services file and make central services dictionary using dictionary of custom data class
csf = open(CSF_filename, 'r')
centralServices = dict()
for line in csf:
    params = line.strip('\n').split(' ')
    serviceNum = params[0]
    capacity = params[1]
    ticketsSold = params[2]
    name = params[3]
    date = params[4]
    # check the the service number is legal
    if(not isLegalServiceNumber(serviceNum)
           or not isLegalTicketAmount(capacity)
           or int(ticketsSold) > int(capacity)
           or not isLegalServiceName(name)
           or not isLegalDate(date)):
            print("Invalid input")
            sys.exit()
   
    centralServices[int(serviceNum)] = ServiceData(
        params[1],
        params[2],
        params[3],
        params[4]
    )
    
# Loop through and parse merged tsf and update central services dictionary using switch case for each transaction
mtsf = open(MTSF_filename, 'r')
for line in mtsf:
    params = line.strip('\n').split(' ')
    code = params[0]
    sourceNum = int(params[1])
    numTickets = int(params[2])
    destNum = int(params[3])
    name = params[4]
    date = params[5]

    # exit if the source service number is not legal
    if not code == 'EOS' and not isLegalServiceNumber(str(sourceNum)):
        print("Invalid input")
        sys.exit()

    if code == 'CRE':
        if (not isLegalServiceName(name)
            or not isLegalDate(date)):
            print("Invalid input")
            sys.exit()
        # Created service needs new service number and  will have 0 sold tickets
        if sourceNum not in centralServices and numTickets == 0:
            centralServices[sourceNum] = ServiceData('30', str(numTickets), name, date)
        else:
            print('Transaction error')
    elif code == 'DEL':
        # Service can only be deleted if it exists and if no tickets have been sold
        if sourceNum in centralServices and centralServices[sourceNum].sold == 0:
            del centralServices[sourceNum]
        else:
            print('Transaction error')
    elif code == 'SEL':
        if not isLegalTicketAmount(str(numTickets)):
            print("Invalid input")
            sys.exit()
        amountSold = centralServices[sourceNum].sold + numTickets
        # New amount can't exceed the capacity
        if amountSold <= centralServices[sourceNum].capacity:
            centralServices[sourceNum].sold = amountSold
        else:
            print('Transaction error')
    elif code == 'CAN':
        if not isLegalTicketAmount(str(numTickets)):
            print("Invalid input")
            sys.exit()
        amountSold = centralServices[sourceNum].sold - numTickets
        # New amount can't exceed the capacity
        if amountSold >= 0:
            centralServices[sourceNum].sold = amountSold
        else:
            print('Transaction error')    
    elif code == 'CHG':
        if (not isLegalTicketAmount(str(numTickets))
            or not isLegalServiceNumber(str(destNum))):
            print("Invalid input")
            sys.exit()
        sourceSold = centralServices[sourceNum].sold - numTickets
        destSold = centralServices[destNum].sold + numTickets
        # Source tickets sold can't be negative, and destination tickets sold can't exceed capacity
        if sourceSold >= 0 and destSold <= centralServices[destNum].sold:
            centralServices[sourceNum].sold = sourceSold
            centralServices[destNum].sold = destSold
        else:
            print('Transaction error')
               

#Write new Central Services File to given filename, sorted in ascending order of service number
fileWriter = open(new_CSF_filename, 'w')
for key in sorted(centralServices):
        fileWriter.write(str(key) + " "
                + str(centralServices[key].capacity) + " "
                + str(centralServices[key].sold) + " "
                + str(centralServices[key].name) + " "
                + str(centralServices[key].date) + " " 
                + '\n')
fileWriter.close()

#Write new Valid Services File to given filename, sorted in ascending order of service number
fileWriter = open(VSF_filename, 'w')
for key in sorted(centralServices):
        fileWriter.write(str(key) + " " + '\n')
fileWriter.write(str("00000\n"))
fileWriter.close()