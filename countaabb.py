def countvar(str1):
    i=0
    result_str=""
    while i<len(str1):
        char_to_check=str1[i]
        count=1
        while(i+1<len(str1) and str1[i+1]==char_to_check):
            count+=1
            i+=1
        result_str+=char_to_check + str(count)
        i+=1
    return result_str
def main():
    str1=input("Enter the string")
    op=countvar(str1)
    print "Op string is {}".format(op)
if __name__=='__main__':
    main()
