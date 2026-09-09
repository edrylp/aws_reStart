# Python3.11  
# Coding: utf-8  

# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  

# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}

float(insulin.count("Y"))
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})
print(seqCount)

pH = 0
while (pH <= 14): 
    netCharge = (
        +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
        for x in ['k','h','r']}.values()))
        -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
        for x in ['y','c','d','e']}.values()))
        )
    print('{0:.2f}'.format(pH), netCharge)
    pH +=1

"""
This code estimates the net electric charge of human insulin at pH values 0 through 14.
It stores protein sequences as strings:
preproInsulin is the full preproinsulin sequence.
bInsulin and aInsulin are the insulin B-chain and A-chain.
insulin = bInsulin + aInsulin combines those two chains into the mature insulin sequence.
pKR maps ionizable amino-acid letters to their approximate pKa values:
Positively charged groups: lysine (k), histidine (h), arginine (r)
Negatively charged groups: tyrosine (y), cysteine (c), aspartic acid (d), glutamic acid (e)
seqCount counts how often each of those amino acids appears in the insulin sequence.
The while loop tests every whole-number pH from 0 to 14.
At each pH, it uses pKa-based formulas to estimate:
the positive charge contributed by k, h, and r
the negative charge contributed by y, c, d, and e
It subtracts the negative charge from the positive charge and prints the result.
"""


"""
# More readable version
amino_acids = ['y', 'c', 'k', 'h', 'r', 'd', 'e']
sequenceCount = {x: insulin.count(x) for x in amino_acids}

while pH <= 14:
    # Positive
    positive_charge = sum(
        sequenceCount[x] * 10**pKR[x] / (10**pH + 10**pKR[x])
        for x in ['k', 'h', 'r']
    )
    # Negative
    negative_charge = sum(
        sequenceCount[x] * 10**pH / (10**pH + 10**pKR[x])
        for x in ['y', 'c', 'd', 'e']
    )

    netCharge = positive_charge - negative_charge
    print(f"{pH:.2f} {netCharge}")
    pH += 1
"""