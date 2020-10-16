# 1.打印9行小星星
row = 1

while row <= 9:

    col = 1

    while col <= row:
        print("*",end = "")
        col += 1

    print("")
    row += 1