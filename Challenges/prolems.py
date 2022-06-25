
import imp


str1 = "string1"
str2 = "I love this World"
str3 = "I like this number "+'2'
my_list = [["string"], [23,5,6,7]]
new_list = list(enumerate(my_list))
n = dict(new_list)
s = ["h","e","l","l","o"]

def reverseString(s):
    for i in range(len(s) // 2):
        s[i], s[len(s) - i -1] = s[len(s) - i - 1], s[i]
 
    print(s)
# o,l,l,e,h

#reverseString(s)

def shift(s, i):
    arr = list(s)
    idf = arr.pop(i)
    arr.insert(i + 1, idf)
    return "".join(arr)

def rotateString(s, goal):
    """
    :type s: str
    :type goal: str
    :rtype: bool
    """
    for i in range(len(s)):
        if s[i:] + s[:i] == goal:
            return True
        print(s[i:] + s[:i])
    return False
print(rotateString("abcde", "abced"))


def fib(n):
    if n <= 2: return 1
    else:
        return fib(n - 1) + fib(n - 2)

def foo(n):
    if n <= 1: return 1
    else: return foo(n - 1) + n 


def fibdp(n, memo = {}):
    if n in memo: return memo[n]
    if n <= 2: return 1
    memo[n] = fibdp(n - 1, memo) + fibdp(n - 2, memo)
    return memo[n]

def grid_travel(n,m):
    if n == 1 and m == 1: return 1
    if n == 0 or m == 0: return 0
    else: return grid_travel(n - 1, m) + grid_travel(n, m - 1)

def grid_travel_dp(n, m, memo={}):
    key = str(n) + ',' + str(m)
    if key in memo: return memo[key]
    if n == 1 and m == 1: return 1
    if n == 0 or m == 0: return 0
    memo[key] = grid_travel_dp(n - 1, m, memo) + grid_travel_dp(n, m - 1, memo)
    return memo[key]


# def convert()
# def solve(names):
#   mapped = []
#   for raw in names:
#     name, num = raw.split()
#     num = convert(num) # this is from leetcode
#     mapped.append((name, num, raw))

#   names.sort(lambda x: [x[0], x[1]])
#   return list(map(names, lambda x: x[2]))

from  collections import Counter

def roman_to_int(string):
                        
    result, mapped = 0, {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    for i, val in Counter(string).items():
        result += mapped[i]*val
    for i in ["IV", "IX", "XL", "XC", "CD", "CM"]:
        print(string.count(i))
        print(mapped[i[0]])
        result -= string.count(i)*2*mapped[i[0]]        
            
    return result
def sortRoman(names):
    result = []
    mapped = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for name in names:
        n, num = name.split()
        num = roman_to_int(num)
        result.append((n,num,name))
    result.sort(key=lambda x: [x[0], x[1]])
    return list(map(lambda x: x[2], result))



if __name__ == "__main__":
    names = ['Steven XL', 'Steven XVI', 'David IX', 'Mary XV', 'Mary XIII', 'Mary XX']
    print(sortRoman(names))