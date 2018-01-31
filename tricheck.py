def tricheck(s1,s2,s3):
    if(s1+s2>=s3 and s1+s3>=s2 and s2+s3>=s1):
        print "Triangle is Possible with {} {} {}".format(s1,s2,s3)
    else:
        print "Triangle is not Possible with {} {} {}".format(s1,s2,s3)
def main():
    s1=input("1st side")
    s2=input("2nd side")
    s3=input("3rd side")
    tricheck(s1,s2,s3)
if __name__ == '__main__':
    main()
