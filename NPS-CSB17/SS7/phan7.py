# Bai 1
high_score = [78, 56, 67]
# Bai 2
for count, item in enumerate(high_score, 1):
    print(count,". ", item)
# Bai 3
new = int(input("Input new high score: "))
high_score.append(new)
for count, item in enumerate(high_score, 1):
    print(count,". ", item)