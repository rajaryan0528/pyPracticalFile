def maxCost(cost, labels, dailyCount):
    count = 0
    price = 0
    data = []
    traversed = 0
    for i in range(0, len(labels)):
        if labels[i] == "legal":
            count += 1
            price += cost[i]
        if i == "illegal":
            price += cost[i]
        if count >= dailyCount:
            data.append(price)
            traversed = i
    print(data)
    return max(data)

print(maxCost([2,3,5,11,1],["legal","illegal","legal","illegal","legal"],2))
