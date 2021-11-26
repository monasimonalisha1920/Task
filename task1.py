
absent= 0
def f(day,l,k):
    global absent
    if k == 4:
        return 0
    if day == 0:
        if l[-1] == 0:
            absent += 1
        return 1
    return f(day-1,l+[1],0)+f(day-1,l+[0],k+1)

day = int(input())

ways = f(day,[],0)
print("for",day,"days",absent,"/",ways)


