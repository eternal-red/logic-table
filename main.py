from itertools import combinations
import pandas as pd
def main(argument):
    #prepare data for table
    formulas=setupFormulas(argument,',')
    varsList=setupVarslist(argument)
    tableColumnNames=varsList+formulas #for table
    truthValues=setupTruthValues(varsList)#for table
    
    #formula code
    formula=formulasCode(formulas)
    howtostore=calculateFormulaValues(formulas,truthValues)
    makeTable(tableColumnNames,truthValues,howtostore)
    checkValidity()
    return 
    
def setupFormulas(argument,seperator=','): #breaks the argument into a list of formulas (each premise/conclusion)
    #replace conclusion seperator with common seperator
    argument=argument.replace('∴',seperator)
    argument=argument.replace('⊢',seperator)
    argument=argument.replace('/','')
    #splits formulas into list
    formulaList=argument.split(seperator)
    return formulaList
def setupVarslist(argument):
#make list of all unique variables (lowercase letters) in argument
    varsList=[]
    for i in range(len(argument)):
        if ord(argument[i])>=97 and ord(argument[i])<=122: 
            if argument[i] not in varsList:
                varsList.append(argument[i])
    return varsList
def setupTruthValues(varsList):
    #all ways to choose x variables 
    allCombinations = list() 
    for numOfTrue in range(len(varsList) + 1):
        allCombinations += list(combinations(varsList, numOfTrue))
    #assign truth values 
    allTruthvalues=[]
    for combination in allCombinations:
        valuesList= [None]*len(varsList)  
        #seeing if variable is in combination tuple or not
        for i in range(len(varsList)):
            if varsList[i] in combination:
                valuesList[i]=1
            else:
                valuesList[i]=0
        tupleList=tuple(valuesList) #prevents aliasing
        allTruthvalues.append(tupleList) 
    #make list into dictionary   
    Truthvaluedics=[]
    for truthValues in allTruthvalues:
        dictionary=dict(zip(varsList,truthValues))
        Truthvaluedics.append(dictionary)
    return Truthvaluedics
def formulasCode(formula):
    pass
def calculateFormulaValues(formulas,truthValues):
    pass
def makeTable(tableColumnNames,truthValues,howtostore):
    pass
def checkValidity():
    pass

#main
formula="p ∨ q, p → r, q → s / ∴ r ∨ s"
print(main(formula))
