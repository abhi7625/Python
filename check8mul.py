def check(num):
    if(num>=8):
        if(num&(2**3-1)==0):
            print ("It is multiple of 8")
        else:
            print ("It is not multiple of 8")
def main():
    num=input("Enter the number")
    check(num)
if __name__ == '__main__':
    main()
