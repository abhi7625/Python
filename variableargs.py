def variablenumberofargumentsdemo(*args):
    print(type(args))
    for x in args:
        print (x)
def main():
    variablenumberofargumentsdemo(2,3,4,5)
    variablenumberofargumentsdemo(2,3,4,5,100,200,"hi","bye")
if __name__ == '__main__':
    main()

