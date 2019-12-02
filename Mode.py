from collections import Counter

def Mode(data):
    c = Counter(data)
    Mode = c.most_common(1)
    return Mode[0][0]

data = [7,8,9,2,10,9,9,9,9,4,5,6,1,5,6,7,8,6,1,10]

print(Mode(data))