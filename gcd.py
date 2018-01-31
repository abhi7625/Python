def gcd(num1,num2):
    #for i in range(2,num2+1):
        #if(num1%i==0 and num2%i==0):
            #return i
    while(num1!=num2):
        if num1>num2:
            num1=num1-num2
        else:
            num2=num2-num1
    return num1 
def main():
    num1=input("Number 1")
    num2=input("Number 2")
    result=gcd(num1,num2)
    print("GCD is {}".format(result))
if __name__ == '__main__':
    main()
