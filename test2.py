def prime():
    n  = eval(input())
    arr = [int(x) for x in input().split()]
    p = [True] * 10000000
    st = dict()
    st.update({2:0})
    for i in range(3,10000000,2):
        if(p[i]==True):
            st.update({i:0})
            for j in range(i * 2,10000000,i):
                p[j] = False
    ans = 0
    for i in arr:
        if st.get(i)!=None :
            ans += 1
    return ans

print(prime())
