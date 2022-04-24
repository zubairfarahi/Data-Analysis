
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

if __name__ == "__main__":
    print(f"fib: {fibdp(50)}")
    print(f"this: {foo(5)}")
    print(f"is {grid_travel(2,3)}")
    print(f"long grid: {grid_travel_dp(18,18)}")