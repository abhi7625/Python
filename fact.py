def fact(number):
    fact=-1
    if number>0:
        if(number<3):
            fact=number
        else:
            fact=1
            #while (number!=0):
            for x in range(2,number+1):
                fact=fact*x
                #fact=fact*number
                #number-=1
    
    
    print("fact is {}".format(fact))
def main():
    number=input("Enter number")
    fact(number)
if __name__ == "__main__":
    main()

