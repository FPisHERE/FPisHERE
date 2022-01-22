name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hourcount = dict()
for line in handle:
    words = line.split()
    if len(words) > 2 and words[0] == "From":
        hour = words[5].split(':')
        hourcount[hour[0]] = hourcount.get(hour[0], 0) + 1
    else:
        continue
# sort
hourlist = list()
for key,value in hourcount.items():
    hourlist.append((key,value))  
hourlist.sort()
for key,value in hourlist:
    print(key,value)
                 
