popSet = set()
popSet.add(-3)
popSet.add(-1)
popSet.add(2)
X = 1
Y = "1"
print(X.__hash__())
print(Y.__hash__())

print(popSet.__contains__(3))
print(popSet)
print(popSet.pop())
print(-3 in popSet)
popSet.add(2)
print(popSet)
print(popSet.pop())
popList = list()
popList.append(-3)
popList.append(-1)
popList.append(2)
print(popList)
print(popList.pop())
