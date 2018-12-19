def john():
    total = 2
    a = 1
    b = 2
    while True:
        c = a + b
        if c > 4000000:
            break
        if c %2 == 0:
            total += c
        a=b
        b=c
    print(total)
        
        
    


if __name__ == '__main__':
    john()