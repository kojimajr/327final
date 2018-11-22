from objects.Session import Session
'''
Runs the logout transaction

Adds the end of session line to the transaction list and then prints the list to the transaction summary file.

@Param currentSession: valid Session object with informtaion on the current session 
'''
def logout(currentSession):
    currentSession.transactions.append("EOS 00000 0 00000 **** 0")
    fileWriter = open(currentSession.filenameTransactions, 'a')
    for line in currentSession.transactions:
        fileWriter.write(line + '\n')
    return
