import time
dataset = []
loopbreak = time.time() + 1
def is_geometric(data):
    ratio = int(data[1]) / int(data[0])
    try:
        for k in range(0, len(data)):
            if int(data[k]) * ratio != int(data[k + 1]):
                return False
    except IndexError:
        return True

def is_quardratic(data):
    try:
        for k in range(0, len(data)):
            if int(data[k]) ** 2 != int(data[k + 1]):
                return False
    except IndexError:
        return True
        
def is_cubic(data):
    try:
        for k in range(0, len(data)):
            if int(data[k]) ** 3 != int(data[k + 1]):
                return False
    except IndexError:
        return True
    
def is_fibonacci(data):
    for k in range(0 , len(data)):
        if (int(data[0]) + int(data[1])) == int(data[2]) and (int(data[1]) + int(data[2])) == int(data[3]):
            return True
    return False
    
def is_geometricwgaps(data):
    li = []
    try:
        for k in range(0, len(data)):
            li.append(int(data[k + 1]) / int(data[k]))
    except IndexError:
        li.sort()
        ratio = li[0]
        try:
            for j in range(1, len(data) + 1):
                if int(data[0]) * (ratio ** j) == int(data[j]):
                    return True
        except IndexError:
            return False
try:
    while time.time() < loopbreak:
        dataset.append(input())
        loopbreak = loopbreak + 1
except EOFError:
    for i in range(0, len(dataset)):
        data = dataset[i].split()
        is_geometric(data)
        if is_geometric(data) == True:
            print('Geometric')
            continue
        elif is_quardratic(data) == True:
            print('X^2')
            continue
        elif is_cubic(data) == True:
            print('X^3')
            continue
        elif is_fibonacci(data) == True:
            print('Fibonacci')
            continue
        elif is_geometricwgaps(data) == True:
            print('Geometric (With Gaps)')
            continue
        else:
            string = ''
            for k in range(0, len(data)):
                string = string + data[k] + ' '
            print(string, 'is an unknown series')
            continue