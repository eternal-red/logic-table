from itertools import combinations
import pandas as pd
def main(input):
    formulas=setupFormulas(input)
    uniqVars=setupVars(input)
    columnNames=formulas+uniqVars
    truthValues=setupTruthvalues(uniqVars)
    return truthValues
    
def setupFormulas(input):
    #take out all spaces in input
    nospaces=''
    for i in range(len(input)):
        if input[i]!=' ':
            nospaces+=input[i]
    nospaces=nospaces.replace('∴',',')
    nospaces=nospaces.replace('⊢',',')
    nospaces=nospaces.replace('/','')

    #be able to split formulas into their own formulas by comma
    formulaList=nospaces.split(',')
    return formulaList
def setupVars(input):
#find all unique variables
    uniqVars=[]
    for i in range(len(input)):
        if ord(input[i])>=97 and ord(input[i])<=122:
            if input[i] not in uniqVars:
                uniqVars.append(input[i])
    return uniqVars


def setupTruthvalues(lettersList):
    # testline lettersList=['A','B','C']
    listCombinations = list()
    valuesList= [None]*len(lettersList)
    table=[]
    ### all variables choose x to be true (for all values of x and variables are unique)
    for size in range(len(lettersList) + 1):
        listCombinations += list(combinations(lettersList, size))
    ###assign true values 
    counter=0
    for permutation in listCombinations:
        
        for i in range(len(lettersList)):
            if lettersList[i] in permutation:
                valuesList[i]=1
            else:
                valuesList[i]=0
        tupleList=tuple(valuesList)
        table.append(tupleList)
    return table



#main loop
formula="p ∨ q, p → r, q → s / ∴ r ∨ s"
print(main(formula))
