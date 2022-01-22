import re
sum = 0
hand = open("regex_sum_1339448.txt")

for line in hand:
    line = line.rstrip()
    number = re.findall('[0-9]+', line)
    print(number)
    for num in number:
        num = int(num)
        sum = sum + num

print(sum)
