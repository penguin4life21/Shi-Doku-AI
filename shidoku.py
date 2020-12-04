#Use 0 to signify an empty cell
#Only use the numbers [0,1,2,3,4]
r1 = [0,0,0,0]
r2 = [0,0,0,0]
r3 = [0,0,0,0]
r4 = [0,0,0,0]

c1 = [r1[0],r2[0],r3[0],r4[0]]
c2 = [r1[1],r2[1],r3[1],r4[1]]
c3 = [r1[2],r2[2],r3[2],r4[2]]
c4 = [r1[3],r2[3],r3[3],r4[3]]
b1 = [r1[0],r1[1],r2[0],r2[1]]
b2 = [r1[2],r1[3],r2[2],r2[3]]
b3 = [r3[0],r3[1],r4[0],r4[1]]
b4 = [r3[2],r3[3],r4[2],r4[3]]
sq11 = r1[0]
sq12 = r1[1]
sq13 = r1[2]
sq14 = r1[3]
sq21 = r2[0]
sq22 = r2[1]
sq23 = r2[2]
sq24 = r2[3]
sq31 = r3[0]
sq32 = r3[1]
sq33 = r3[2]
sq34 = r3[3]
sq41 = r4[0]
sq42 = r4[1]
sq43 = r4[2]
sq44 = r4[3]
sq =[sq11,sq12,sq13,sq14,sq21,sq22,sq23,sq24,sq31,sq32,sq33,sq34,sq41,sq42,sq43,sq44]
sp11 = []
sp12 = []
sp13 = []
sp14 = []
sp21 = []
sp22 = []
sp23 = []
sp24 = []
sp31 = []
sp32 = []
sp33 = []
sp34 = []
sp41 = []
sp42 = []
sp43 = []
sp44 = []
s1 = []
s2 = []
s3 = []
s4 = []
print(r1)
print(r2)
print(r3)
print(r4)
print("----------------------------")
for i in range(6):
    for a in range(4):
        if sq11 == 0 and not(sq12 == a + 1 or sq13 == a + 1 or sq14 == a + 1 or sq21 == a + 1 or sq22 == a + 1 or sq31 == a + 1 or sq41 == a + 1):
            sp11.append(a + 1)
    for a in range(4):
        if sq12 == 0 and not(sq11 == a + 1 or sq13 == a + 1 or sq14 == a + 1 or sq21 == a + 1 or sq22 == a + 1 or sq32 == a + 1 or sq42 == a + 1):
            sp12.append(a + 1)
    for a in range(4):
        if sq13 == 0 and not(sq11 == a + 1 or sq12 == a + 1 or sq14 == a + 1 or sq23 == a + 1 or sq24 == a + 1 or sq33 == a + 1 or sq43 == a + 1):
            sp13.append(a + 1)
    for a in range(4):
        if sq14 == 0 and not(sq11 == a + 1 or sq12 == a + 1 or sq13 == a + 1 or sq23 == a + 1 or sq24 == a + 1 or sq34 == a + 1 or sq44 == a + 1):
            sp14.append(a + 1)
    for a in range(4):
        if sq21 == 0 and not(sq11 == a + 1 or sq12 == a + 1 or sq22 == a + 1 or sq23 == a + 1 or sq24 == a + 1 or sq31 == a + 1 or sq41 == a + 1):
            sp21.append(a + 1)
    for a in range(4):
        if sq22 == 0 and not(sq11 == a + 1 or sq12 == a + 1 or sq21 == a + 1 or sq23 == a + 1 or sq24 == a + 1 or sq32 == a + 1 or sq42 == a + 1):
            sp22.append(a + 1)
    for a in range(4):
        if sq23 == 0 and not(sq13 == a + 1 or sq14 == a + 1 or sq21 == a + 1 or sq22 == a + 1 or sq24 == a + 1 or sq32 == a + 1 or sq43 == a + 1):
         sp23.append(a + 1)
    for a in range(4):
        if sq24 == 0 and not(sq13 == a + 1 or sq14 == a + 1 or sq21 == a + 1 or sq22 == a + 1 or sq23 == a + 1 or sq34 == a + 1 or sq44 == a + 1):
            sp24.append(a + 1)
    for a in range(4):
       if sq31 == 0 and not(sq11 == a + 1 or sq21 == a + 1 or sq32 == a + 1 or sq33 == a + 1 or sq34 == a + 1 or sq41 == a + 1 or sq42 == a + 1):
           sp31.append(a + 1)
    for a in range(4):
        if sq32 == 0 and not(sq12 == a + 1 or sq22 == a + 1 or sq31 == a + 1 or sq33 == a + 1 or sq34 == a + 1 or sq41 == a + 1 or sq42 == a + 1):
            sp32.append(a + 1)
    for a in range(4):
        if sq33 == 0 and not(sq13 == a + 1 or sq23 == a + 1 or sq31 == a + 1 or sq32 == a + 1 or sq34 == a + 1 or sq43 == a + 1 or sq44 == a + 1):
            sp33.append(a + 1)
    for a in range(4):
        if sq34 == 0 and not(sq14 == a + 1 or sq24 == a + 1 or sq31 == a + 1 or sq32 == a + 1 or sq33 == a + 1 or sq43 == a + 1 or sq44 == a + 1):
            sp34.append(a + 1)
    for a in range(4):
        if sq41 == 0 and not(sq11 == a + 1 or sq21 == a + 1 or sq31 == a + 1 or sq32 == a + 1 or sq42 == a + 1 or sq43 == a + 1 or sq44 == a + 1):
            sp41.append(a + 1)
    for a in range(4):
        if sq42 == 0 and not(sq12 == a + 1 or sq22 == a + 1 or sq31 == a + 1 or sq32 == a + 1 or sq41 == a + 1 or sq43 == a + 1 or sq44 == a + 1):
            sp42.append(a + 1)
    for a in range(4):
        if sq43 == 0 and not(sq13 == a + 1 or sq23 == a + 1 or sq33 == a + 1 or sq34 == a + 1 or sq41 == a + 1 or sq42 == a + 1 or sq44 == a + 1):
            sp43.append(a + 1)
    for a in range(4):
        if sq44 == 0 and not(sq14 == a + 1 or sq24 == a + 1 or sq33 == a + 1 or sq34 == a + 1 or sq41 == a + 1 or sq42 == a + 1 or sq43 == a + 1):
            sp44.append(a + 1)
    if len(sp11) == 1:
        sq11 = sp11[0]
    if len(sp12) == 1:
        sq12 = sp12[0]
    if len(sp13) == 1:
        sq13 = sp13[0]
    if len(sp14) == 1:
        sq14 = sp14[0]
    if len(sp21) == 1:
        sq21 = sp21[0]
    if len(sp22) == 1:
        sq22 = sp22[0]
    if len(sp23) == 1:
        sq23 = sp23[0]
    if len(sp24) == 1:
        sq24 = sp24[0]
    if len(sp31) == 1:
        sq31 = sp31[0]
    if len(sp32) == 1:
        sq32 = sp32[0]
    if len(sp33) == 1:
        sq33 = sp33[0]
    if len(sp34) == 1:
        sq34 = sp34[0]
    if len(sp41) == 1:
        sq41 = sp41[0]
    if len(sp42) == 1:
        sq42 = sp42[0]
    if len(sp43) == 1:
        sq43 = sp43[0]
    if len(sp44) == 1:
        sq44 = sp44[0]
    sp11 = []
    sp12 = []
    sp13 = []
    sp14 = []
    sp21 = []
    sp22 = []
    sp23 = []
    sp24 = []
    sp31 = []
    sp32 = []
    sp33 = []
    sp34 = []
    sp41 = []
    sp42 = []
    sp43 = []
    sp44 = []
s1 = [sq11, sq12, sq13, sq14]
s2 = [sq21, sq22, sq23, sq24]
s3 = [sq31, sq32, sq33, sq34]
s4 = [sq41, sq42, sq43, sq44]
print(s1)
print(s2)
print(s3)
print(s4)