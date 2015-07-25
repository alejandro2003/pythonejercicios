

# Task1 "reverse" string

def task1(string):
    new_string = string[::-1]
    print new_string


# Task2 vocals sum

def task2(string):
    new_string = string.lower()
    count = 0
    for i in new_string:
        if i in {'a', 'e', 'i', 'o', 'u'}:
            count += 1
    print count


# Task3  count substring

def task3(substring, string):
     counter = 0
     # for i in string:
     # counter = string.count(substring)
     print string.count(substring)


# Task4  type

def task4(element):
    print type(element)


# Task5  eliminate double elements
# (["a", 5, 2, 5, (1, "a"), "a"]) == [2, "a", 5, (1, "a")]

def task5(list1):
    result = []
    for i in list1:
        if not i in result:
            result.append(i)
    print result

# Task6  returning every third element of tuple


def task6(tuple1):
    print tuple1[2::3]


def task7(tuple1):
    print [i ** 2 for i in tuple1]

# "abba" >> True  mirror effect


def reverse(str):
    return str[::-1]


def task8(string):
    string2 = ""
    string2 = reverse(string[len(string)/2:])
    if string.find(string2)==0:
        print True
    else:
        print False


a = "aicnalubma"

#task1(a)

#task2("hApPyHalLOweEn!")

#task3("wow","wowhatamanwowowpalehche")

#task4(5)

#task5(["a", 5, 2, 5, (1, "a"), "a"])
T = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c')
#task6(T)

#task7([1,2,3])
#task7((6,2,3))

#task8("abba")
#task8("arbat")