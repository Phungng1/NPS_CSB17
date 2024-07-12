# Bai 1
high_score = [78, 56, 67]
new = int(input("Input new high score: "))
high_score.append(new)
high_score.sort(reverse=True)
for count, item in enumerate(high_score, 1):
    print(count,". ", item)
# Bai 2
high_score = [78, 56, 67, 80, 45, 32]
new = int(input("Input new high score: "))
high_score.append(new)
high_score.sort(reverse=True)
for i in range(0,5,1):
    j = i+1
    print(i,". ", high_score[i])
