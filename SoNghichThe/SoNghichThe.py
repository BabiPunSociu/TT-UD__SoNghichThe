# Đếm số nghịch thế
# Số nghịch thế là cặp số (x[i],x[j]) mà x[i]>x[j] và i<j

# Dùng cây IT


# Cách 1: dùng mảng

a= [0]*400005
res=0
def update(k,l,r,x):
    global a, res
    a[k] += 1
    if l+1 == r: return 
    if x<(l+r)//2:
        res += a[2*k+2]
        update(2*k+1,l,(l+r)//2,x)
    else: update(2*k+2,(l+r)//2,r,x)

if __name__ == "__main__":
    n= int(input())
    for x in map(int, input().split()): update(0,1,n+1,x)
    print(res)


# Cách 2: Dùng node
