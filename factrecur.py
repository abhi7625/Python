def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
    
def main():
    n=input("Enter number")
    result=fact(n)
    print "{}".format(result)
if __name__ == '__main__':
    main()
