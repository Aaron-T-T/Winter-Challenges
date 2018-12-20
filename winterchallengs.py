
    
def firstproblem():
    total = 0
    for i in range(1,1000):
        if i % 5 == 0 or i % 3 == 0:
            total += i 
    print(total)
def secondproblem():
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

def thirdproblem():
    num = 2520
    total=0
    a = 0
    while True:
        num += 20
        total = 0
        for i in range(20,10,-1):
            if num % i != 0:
                break
            if i == 11:
                print(num)
                a =  1
        if a == 1:
            break
        
def fourthproblem():
    greatest = 0
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            a = i *j
            if str(a) == str(a)[::-1]:
                if greatest < a:
                    greatest = a
    print(greatest)
    
        
        
    


if __name__ == '__main__':
#    firstproblem()
##    secondproblem()
#    thirdproble()
