import random
outcomes = list()
outcomes.append('H')
outcomes.append('T')
count = 0
a = input("enter a 3 toss sequence (eg: HTT)").upper()
series = list()

while True:
    toss = random.choice(outcomes)
    series.append(toss)
    count += 1

    if len(series) >= 3:
        last_three = ''.join(series[-3:])
        if last_three == a:
            break

print(f"Sequence {series} appeared after {count} tosses")
