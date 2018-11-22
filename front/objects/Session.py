'''
Object that keeps track of current session parameters 

@Param self:
@Param isPlanner: boolean that is true if the user is a planner and false if the user is an agent
@Param servicesValid: List of valid services for this session
@Param filenameTransactions: Name of transaction summary file that will be written to on logout
'''

class Session:
    def __init__(self, isPlanner = False, servicesValid =[], filenameTransactions = "tsf.txt"):
        self.isPlanner = isPlanner
        self.filenameTransactions = filenameTransactions
        self.transactions = [] #List that will be written to the transaction summary file
        self.servicesValid = servicesValid
        self.servicesDeleted = [] #List of deleted services
        self.ticketsCanceled = {} #Dictionary containing the number of each different ticket that is canceled
        self.totalCanceled = 0 #Total number of canceled tickets for the session
        self.totalChanged = 0 #Total number of changed tickets or the session