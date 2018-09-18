#Ashley Wohlrab
#CMPT 120
#27 September 2018

n = int(input("\nWhat is n?:"))

total = 0.0
sgn = 1.0   
for denom in range(1, 2*n, 2):
    total = total + sgn * 4.0/denom
    sgn = -sgn 

    print(total)
    
