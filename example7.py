from itertools import permutations,combinations
L =[4, 3, 2, 5, 7, 2, 9, 1]
s = 6
output=[]
'''
#method1
while L:
    pick = L.pop()
    diff = s-pick
    if diff in L:
         output.append((pick,diff))
print(output)
'''

#method2
for i in combinations(L,2):
    if sum(i)==s:
        output.append(i)
print(output)