def func(num,pos,bits):
    if pos >= bits:
        x=1
        x=(x<<bits)-1
        x=x<<(pos-bits)
        x=~x
        num = num & x
        return num
def main():
    num=input("Number")
    pos=input("Position")
    bits=input("Bits")
    res=func(num,pos,bits)
    print "Result is {}".format(res)
if __name__ == '__main__':
    main()
