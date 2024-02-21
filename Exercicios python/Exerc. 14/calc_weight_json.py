import jsonFileHandler

data = jsonFileHandler.readJsonFile('Exercicios python/Exerc. 14/files/insulin.json')

if data != "" :
    bcInsulin = data['molecules']['bcInsulin']
    acInsulin = data['molecules']['acInsulin']
    insulin = bcInsulin + acInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    print('bcInsulin: ' + bcInsulin)
    print('acInsulin: ' + acInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
    print('\n')
    
    # Calculating the molecular weight of insulin

    # Getting a list of the amino acid (AA) weights
    aaWeights = data['weights']

    # Count the number of each amino acids
    aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', \
    'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})

    # Multiply the count by the weights 
    molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
    ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', \
    'S', 'T', 'V', 'W', 'Y']}.values())  
    print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
    print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual) \
    /molecularWeightInsulinActual)*100))
else:
    print("Error. Exiting program")