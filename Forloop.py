    num = int(input("Enter a Number"))
    
    for i in range(num):
        if num < 0:
            i = num - 1
            break
        i = i * i
        print(i);
