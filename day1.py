top3elves = [[0,0],[0,0],[0,0]]
answer = [0, 0]

def checkInventory(elfInventory, i):
    for i in range(3):
        if elfInventory > top3elves[i][0]:
            top3elves[i][0] = elfInventory
            top3elves[i][1] = i
            break

with open('day1.txt') as file:
    data = file.read().split("\n\n")
    for i in range(len(data)):
        elfInventory = list(map(int, data[i].split('\n')))
        elfInventory = sum(elfInventory)
        checkInventory(elfInventory, i)
print(top3elves)
