
STV = 800_000_000
THV = 5
LS = 0.12
TN = 45_000_000
NC = 10_000_000
CPSH = 4_000_000
SN = 3

DTI = ((STV / (THV * 12) + STV * (LS / 12)) + NC) / (TN - CPSH * SN)

print("DTI =", DTI)

if DTI < 0.7:
    print("ĐƯỢC VAY")
else:
    print("KHÔNG ĐƯỢC VAY")
