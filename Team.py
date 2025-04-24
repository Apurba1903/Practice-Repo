n = int(input())

if 1 <= n <= 1000:
    
    sum = 0
    for i in range(n):
        P , V , T = input().split()
        
        x = int(P)
        y = int(V)
        z = int(T)
        
        if x + y + z >= 2:
            sum += 1
    
    print(sum)