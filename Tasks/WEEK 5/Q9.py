for i in range(20):
    for j in range(20):
        if i * j > 10:
            print(i, j)
            break
    else:
        continue
    break
