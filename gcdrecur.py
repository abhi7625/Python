def gcd(no1,no2):
    if no1==no2:
        return no1
    else:
        if no1>no2:
            no1-=no2
        else:
            no2-=no1
        return gcd(no1,no2)
def main():
    no1 = input("Enter 1 number")
    no2 = input("Enter 2 number")
    result=gcd(no1,no2)
    print("GCD is {}".format(result))
if __name__ == '__main__':
    main()
