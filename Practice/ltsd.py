# 1 Find the largest number in a list

# nums = [10, 45, 23, 89, 12]
# print(max(nums))

# 2 Remove duplicate elements from a list

# items = [1, 2, 2, 3, 4, 4, 5]
# x = set(items)
# print(x)

# 3️ Count even and odd numbers in a list

# nums = [1, 2, 3, 4, 5, 6]
# for i in nums:
#     if i%2==0:
#         print(f"{i} even")
#     else:
#         print(f"{i} odd")

# 4 Reverse a list without using reverse()

# nums = [10, 20, 30, 40]

# for i in nums:
#     print(nums[::-1])
#     break

# 5 Sum of all elements in a list

# nums = [5, 10, 15, 20]
# add = 0
# for i in nums:
#     add+=i
# print(f"{add} is sum of all element values")

# TUPLE PRACTICAL QUESTIONS
# 6 Convert tuple to list and add an element

# tup = (1, 2, 3, 4)
# tup = list(tup)
# tup.append(5)
# tup = tuple(tup)
# print(tup)

# 7 Count how many times an element appears in a tuple

# tup = (1, 2, 2, 3, 2, 4)
# for t in tup:
#     print(t,':', tup.count(t))

# 8 Find maximum and minimum value in a tuple

# tup = (45, 12, 78, 34)
# print(max(tup))
# print(min(tup))

# 9 Check if an element exists in a tuple

# tup = ("apple", "banana", "cherry")

# if "cherry" in tup:
#     print("Yes")
# else:
#     print("No")

# STRING PRACTICAL QUESTIONS

# 10 Reverse a string

# s = "python"
# print(s[::-1])

# 11 Count vowels in a string

# s = "education"

# for i in s:
#     if i in ('a','e','i','o','u'):
#         print(f"{i} yes vowel")
#     else:
#         print(f"{i} no it not vowel")

# 12 Check if a string is palindrome

# s = "madam"
# x = s[::-1]

# if s not in '':
#     if s == x:
#         print("Palindrome")
#     else:
#         print("not palindrome")

# 13 Count frequency of each character

# s = "programming"

# for i in s:
#     print(i,':',s.count(i))

# 14 Convert string to title case

# s = "python is easy"
# x = s.title()
# print(x)

# DICTIONARY PRACTICAL QUESTIONS
# 15 Print key and value from dictionary

# student = {"name": "Amit", "age": 20, "marks": 85}
# x = student.keys()
# print(x)

# y = student.values()
# print(y)

# 16 Find sum of dictionary values

# marks = {"math": 80, "science": 70, "english": 75}
# add = 0

# for m in marks.values():
#     add+=m
# print(f"sum of dict value is: {add}")

# 1️7 Find the key with maximum value

# scores = {"A": 90, "B": 85, "C": 95}
# max_val = 0
# max_key = None

# for a,b in scores.items():
    
#    if b > max_val:
#        max_key = a
#        max_val = b
# print(f"max key and value is {max_key, max_val}")

# 18 Count word frequency in a sentence

# sentence = "python is easy and python is powerful"
# record = sentence.split()

# for j in record:
#     print(j + ':', sentence.count(j))

# 1️9️ Merge two dictionaries

# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4}



