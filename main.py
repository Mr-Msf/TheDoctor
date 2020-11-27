def welcome():
    print("\nHello! My name is The Doctor. What seems to be the problem?")

def handleSymtoms():
    try:
        symtom = input("Your symtoms: ")
        with open('data.txt') as file:
            database = []
            for line in file:
                line = data.readline()
                datag = line.split('-->')
                print(datag)
                datasymtom = datag[0].strip()
                diagnosis = datag[1].strip()
                database.append([datasymtom, diagnosis])
            for item in database:
                if datasymtom in symtom:
                    print("Yay")
    except:
        print("Error!")
            

    
    
   

def main():
    welcome()
    handleSymtoms()


if __name__ == "__main__":
    main()