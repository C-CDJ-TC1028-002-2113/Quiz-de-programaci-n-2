
def main():
    peso = float(input())
    zona = int(input())
    if peso>0 and peso<=5000:    
        if zona == 1:
            print(peso*24)
        elif zona == 2:
            print(peso*20)
        elif zona == 3:
            print(peso*21)
        elif zona == 4:
            print(peso*12)
        elif zona == 5:
            print(peso*16)
        else:
            print("INCORRECTO")
    else:
        print("INCORRECTO")



if __name__ == '__main__':
    main()
