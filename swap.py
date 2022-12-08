P = 1200
T = 3 
R = 4
#Process
Si = (int(P) * float(T) * float(R) ) /100
Ci = int(P) * (((1 + float(R)/100) ** int(T)) - 1)
#Output
print("\n Simple Interest = ",Si)
print("\n Compound Interest = ",Ci)