str1 = "1234"
str2 = "4433"
c = 0
for i in str1:
    for j in str2:
        if i == j:
            c += 1
            str1 = str1.replace(i, "_", 1)
            str2 = str2.replace(j, "_", 1)
            print(f"{str1}, {str2}, {c}")
            break
        print(f"{str1}, {str2}, {c}")
