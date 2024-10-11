def s_largest(n1,n2,n3):
    return n1 if (n1<n2 and n1>n3) or (n1>n2 and n1<n3) else (n2 if n2<n1 and n2>n3 or n2>n1 and n2<n3 else n3)



print(s_largest(1,2,3))