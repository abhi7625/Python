def checknoones(num):
    x=1
    count=0
    while(x<=num):
        if(num&x)!=0:
            count+=1
        x=x<<1
    return count
def main():
    num=input("Enter the number")
    res=checknoones(num)
    print "Ones are {}".format(res)
if __name__ == '__main__':
    main()
