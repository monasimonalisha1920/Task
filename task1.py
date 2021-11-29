
absnt= 0
def f(day,l,k):
    global absnt
    if k == 4:
        return 0
    if day == 0:
        if l[-1] == 0:
            absnt += 1
        return 1
    return f(day-1,l+[1],0)+f(day-1,l+[0],k+1)


def myfun(day):
    gg = f(day,[],0)
    # print(absent)
    res = [absnt,gg]
    print("for",day,"days",absnt,"/",gg)
    return res
# myfun(int(input("enter days:")))
