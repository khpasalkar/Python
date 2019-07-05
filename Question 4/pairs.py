n=int(input("Enter the no of pairs: "))
list1 = []
list2 = []
for x in range(n):
    s = input("Enter the pairs of employees: ")
    list1.append(set(s.split()))

for set1 in list1:
    for set2 in list1:
        if set1 != set2 and not set1.isdisjoint(set2):
            list1.append(set1.union(set2))
            list1.remove(set1)
            list1.remove(set2)
            break

print("The groups are: " + str(list1))

s2=input("Enter the pair: ")
list2 = s2.split()
flag = False
for set1 in list1:
    if (list2[1]) in set1 and (list2[0]) in set1:
        flag = True


if flag:
    print("Yes")
else:
    print("No")
