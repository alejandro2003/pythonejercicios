
# [1,2,3] -> {1: False, 2: False, 3: True}


def task1(list1):
    d = {}
    for i in list1:
        d[i] = (i % 3 == 0)
    print d


# (1,4,8,6,3,7,1) >> ((1,4),(8,6),(3,7),(1,))
def task2(tuple1):
    result = []
    for i in range(0, len(tuple1),2):
        t = (tuple1[i:i+2])
        result.append(t)
    return tuple(result)


# [[1],[4,8],[6,3,7],[1,3]] -> [1,4,8,6,3,7,1,3]
def task3(list1):
    result = []
    for i in list1:
        for item in i:
            result.append(item)
    print result


# count vocals

def task4(string):
    counter = 0
    for i in string.upper():
        if i in {'A', 'E', 'I', 'O', 'U', 'Y'}:
            counter += 1

    print counter


# statistics for letters
def task4(letters,string):
    counter = 0
    dictionary1 = {}
    letters2 = letters.upper()
    for i in letters2:
        for item in string.upper():
            if i == item:
                counter += 1
            dictionary1[i] = counter
    print dictionary1


#task1([1,2,3])

#print task2((1,4,8,6,3,7,1))

#task3([[1],[4,8],[6,3,7],[1,3]])


stringP1 = "Proin eget tortor risus. Cras ultricies ligula " \
           "sed magna dictum porta. Proin eget tortor risus." \
           " Curabitur non nulla sit amet nisl tempus convallis " \
           "quis ac lectus. Donec rutrum congue leo eget malesuada."

#task4(stringP1)

stringP2 = "Proin eget tortor risus. Cras ultricies ligula sed" \
           " magna dictum porta. Donec rutrum congue leo eget malesuada."

task4("ABCda",stringP2)