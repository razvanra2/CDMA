a = [0, 0, 0, 1, 1, 0, 1, 1]
print(f'A is: {a}')
b = [0, 0, 1, 0, 1, 1, 1, 0]
print(f'B is: {b}')
bit_a = 0
print(f'A wants to send bit {bit_a}')
bit_b = 1
print(f'B wants to send bit {bit_b}')
######################################################

a_poz = []
a_neg = []
for bit in a:
    if bit is 0:
        a_poz.append(-1)
        a_neg.append(1)
    if bit is 1:
        a_poz.append(1)
        a_neg.append(-1)

print(f'A+: {a_poz}')
print(f'A-: {a_neg}')

b_poz = []
b_neg = []
for bit in b:
    if bit is 0:
        b_poz.append(-1)
        b_neg.append(1)
    if bit is 1:
        b_poz.append(1)
        b_neg.append(-1)

print(f'B+: {b_poz}')
print(f'B-: {b_neg}')

a_message = a_poz
b_message = b_poz

if bit_a is 0:
    a_message = a_neg
if bit_b is 0:
    b_message = b_neg

print(f'A message: {a_message}')
print(f'B message: {b_message}')

X = [sum(x) for x in zip(a_message, b_message)]
print(f'X is: {X}')

ar = sum([e1 * e2 for e1,e2 in zip(X, a_poz)])
print (f'Ar: {[e1 * e2 for e1,e2 in zip(X, a_poz)]} with sum {ar}')
br = sum([e1 * e2 for e1,e2 in zip(X, b_poz)])
print (f'Br: {[e1 * e2 for e1,e2 in zip(X, b_poz)]} with sum {br}')

a_sent_bit = None
if ar > 0:
    ar_sent_bit = 1
else:
    a_sent_bit = 0

print(f'A sent bit: {a_sent_bit}')    

b_sent_bit = None
if br > 0:
    b_sent_bit = 1
else:
    b_sent_bit = 0

print(f'B sent bit: {b_sent_bit}')    
