activities = [
    ['A1',0,6],
    ['A2',3,4],
    ['A3',1,2],
    ['A4',5,8],
    ['A5',5,7],
    ['A6',8,9]]

def max_activities(activities):
    activities.sort(key = lambda x: x[2])
    total = 1
    j = 0
    print(activities[j][0])
    for i in range(len(activities)):
        if activities[i][1] > activities[j][2]:
            total += 1
            j = i
            print(activities[i][0])
    print('Max activities = {}'.format(total))


# max_activities(activities)
def coins_change(total_amount, coins):
    coins.sort()
    max_index = len(coins)-1
    while True:
        coin = coins[max_index]
        if total_amount >= coin:
            print(coin)
            total_amount -= coin
        if total_amount < coin:
            max_index -= 1
        if total_amount == 0:
            break

# coins = [1,2,5,20,50,100]

# coins_change(201, coins)

class Knapsack:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.density = value/weight


class KnapsackFraction:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def fetch(self, total_weight):
        net_weight = 0
        net_value = 0
        self.items.sort(key = lambda x : x.density, reverse=True)
        for i in self.items:
            if net_weight + i.weight <= total_weight:
                net_weight += i.weight
                net_value += i.value
            else:
                rem = total_weight - net_weight
                net_value += i.density * rem
                net_weight += rem
            if net_weight == total_weight:
                break
        return net_value

item1 = Knapsack(20,100)
item2 = Knapsack(30,120)
item3 = Knapsack(10,60)
kf = KnapsackFraction()
kf.add_item(item1)
kf.add_item(item2)
kf.add_item(item3)

print(kf.fetch(50))
    
