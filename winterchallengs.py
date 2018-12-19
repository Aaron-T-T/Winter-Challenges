def john():
    a = 0
    for i in range(0,1000):
        c= 5
        d =3
        b = c*i
        e= d*i
        if b <1000:
            a += b
        if e <1000:
            a+=e
    print(a)
        
def main():
    john()
if __name__ == '__main__':
    main()