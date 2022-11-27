a = input().split()

def pow(a, n):
    if(n == 0):
        return 1
    elif(n == 1):
        return a
    else:
        res = float(a)
        for i in range(2, n+1):
            res = res * a
        return res

print(pow(float(a[0]),int(a[1])))