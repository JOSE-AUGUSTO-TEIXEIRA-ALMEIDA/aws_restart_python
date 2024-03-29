# Python 3.8.16
# Coding: utf-8

# Store the human preproinsulin sequence in a variable called preproinsulin:
prepoInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:
spInsulin = "malwmrllpllallalwgpdpaaa"
bcInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
cpInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
acInsulin = "giveqcctsicslyqlenycn"

insulin = bcInsulin + acInsulin

# Printing "the sequence of human insulin" to console using successive print() commands:
print("The sequence of human preproinsulin:\n", prepoInsulin)
print('\n')
print("The sequence of human insulin, signal peptide: " + spInsulin)
print("The sequence of human insulin, b-chain: " + bcInsulin)
print("The sequence of human insulin, a-chain: " + acInsulin)
print("The sequence of human insulin, c-peptide: " + cpInsulin)
print('\n')

# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19, \
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21, \
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12, \
'V': 117.15, 'W': 204.23, 'Y': 181.19}

# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C', \
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', \
'V', 'W', 'Y']})

# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in ['A', \
'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', \
'V', 'W', 'Y']}.values())

print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))

# Error percentage of insulin's molecular weight
molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/ \
molecularWeightInsulinActual)*100))
