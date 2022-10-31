def convertFormulas(formulas):
    dynamicCode=[]
    for formula in formulas:
        for i in range(len(formula)):
            if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
                continue
            
    

#(['p∨q', 'p→r', 'q→s', 'r∨s'])


experiment= '''
if (A or B):
    if C:
        print(True)
    else:
        print(False)
'''

#exec(experiment)
uniqVars=['a','b','c','d']
truths=[1,1,0,0]

def evaluateRows(uniqVars,truthvalues,formulas):
    total=0
    for i in range(len(uniqVars)):
        executionStr=f'''
{uniqVars[i]}={truthvalues[i]}'''
        exec(executionStr)
    for i in range(len(uniqVars)):
        total+=exec('uniqVars[i]')
    return total


truthValues=[(0, 0, 0, 0), (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1), (0, 1, 1, 0), (0, 1, 0, 1), (0, 0, 1, 1), (1, 
1, 1, 0), (1, 1, 0, 1), (1, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1)]
uniqVars=['a','b','c','d']
#try working with dictionaries or tuples
##put in main loop
def setupVars(uniqVars,truthValues):
    for i in truthValues:
        output=dict(zip(uniqVars,i))
        ##do formula stuff here
        ##append rows here
    return

print(setupVars(uniqVars,truthValues))