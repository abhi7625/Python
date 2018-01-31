def push(l1,data):
    l1.append(data)
def pop(l1):
    return l1.pop()
def Isfull(l1):
    return len(l1)==10
def Isempty(l1):
    return len(l1)==0
def display(l1):
    print l1
def main():
    l1=[]
    data=input("Enter data")
    l1.append(data)
    push(l1,data)
    pop(l1)
    Isfull(l1)
    Isempty(l1)
    display(l1)
if __name__=='__main__':
    main()
