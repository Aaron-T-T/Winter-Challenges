def john():
    num = 2520
    while True:
        num += 20
        for i in range(11,21):
            if num % i == 0:
                print(num)
        break
    
    
        
        
    


if __name__ == '__main__':
    john()