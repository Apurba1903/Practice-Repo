
# My Answer

var = input("")

try:
    check = int(var)
    print("")
except:
    if len(var) <= 10:
        print(var)
    else:
        first = var[0]
        last = var[-1]
        middle = len(var[1:-1])
        print(f"{first}{middle}{last}")



# Correct Answer

# n = int(input())
# for _ in range(n):
#     word = input().strip()
#     if len(word) > 10:
#         print(f"{word[0]}{len(word)-2}{word[-1]}")
#     else:
#         print(word)
