# Python3.8.16
# Coding: utf-8

# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqv" \
"gqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:
spInsulin = "malwmrllpllallalwgpdpaaa"
bcInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
acInsulin = "giveqcctsicslyqlenycn"
cpInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
insulin = bcInsulin + acInsulin

# Dicotionary
# Note: Y, C, K, H, R, D, and E are the only amino acids that contribute to the net-charge calculation.
pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

# Net charge mathematical formula
pH = 0

while (pH <= 14):
    netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))
    
    print('{0:.2f}'.format(pH), netCharge)
    pH +=1
    