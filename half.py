def half(n):
    for i in range(0,4):
        half(n/2)
        print(n)
half(4)
