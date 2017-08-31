def getInput(prompt):
    if (prompt == None):
        return None
    userInput = input(prompt)
    return userInput
    
def getCommand(prompt):
    if (prompt == ""):
        return None
    userInput = input(prompt)
    return userInput.split()[0]

def output(output):
    print(output)
