def formulasCode(formulas):
    formulaCodes=[]
    #put parentheses around not
    charToreplace={'∧': ' and ', '&': ' and ', '⋅': ' and ',
                   '∨':' or ','|':' or ',
                   '¬':' not ', '!':' not ', '~':' not ',
                   '↔':'==', '≡':'=='}
    for formula in formulas:
        for key, value in charToreplace.items():
            formula = formula.replace(key, value)
        #translate if statement
        for i in range(len(formula)):
            if formula[i] in {'⇒','→','⊃'}:   
                formula=f'{formula[i+1:]} if {formula[:i]} else 1'
                
        #check again, keep on going until you see if, then do same thing again, make a while loop?
        formulaCodes.append(formula)
    return formulaCodes

formulas=['(p∨q)→c→d','¬(a∧p)','a≡¬b∧c']
print(formulasCode(formulas))
