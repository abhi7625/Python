def sort(l1):
    for i in range (len(l1)):
        for j in range (i+1,len(l1)):
            if l1[i]>l1[j]:
                temp=l1[i]
                l1[i]=l1[j]
                l1[j]=temp
    return l1
def merge(l1,l2,l3):
    i=j=0
    while(i<len(l1) and j<len(l2)):
        if (l1[i]<l2[j]):
            l3.append(l1[i])
            i+=1
        else:
            l3.append(l2[j])
            j+=1
    if(i<len(l1)):
        l3.extend(l1[i:])
    if(j<len(l2)):
        l3.extend(l2[j:])
    return l3       
def main():
    l1=[]
    l2=[]
    l3=[]
    l1=list(input("Enter 1st list"))
    l2=list(input("Enter 2nd list"))
    l1=sort(l1)
    l2=sort(l2)
    l3=merge(l1,l2,l3)
    print l3
if __name__ =='__main__':
    main()
