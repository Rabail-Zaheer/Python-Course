import array as arr

set1 = {"apple","banana","grapes"}

set2 = {"apples","oranges","stawberry"}

add = set1.add("mango")

print(add)

add2 = set2.add("mango")

print(add2)

comman = set1.intersection(set2)

print(comman)

basket = arr.array("i",[1,2,3,4,4])

count = basket.count(4)

add3 = basket.insert(2,4)

add4 = basket.append(4)

count1 = basket.count(4)

print(count1)

reverse1 = basket.reverse()

print(reverse1)