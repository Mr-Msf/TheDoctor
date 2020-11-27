def welcome():
    print("\nHello! My name is The Doctor. What seems to be the problem?")
    symtom = input("\nYour symtoms: ")
    return symtom

def handleData():
    database = []
    try:
        with open('data.txt') as file:
            for line in file:
                data = line.split('-->')
                datasymtom = data[0].strip()
                diagnosis = data[1].strip()
                database.append([datasymtom, diagnosis])
    except Exception as e:
        print(f"Error: {e}")
    return database
            
def compareSymtoms(symtom, database):
    found = False
    for item in database:
        datasymtom = item[0]
        diagnosis = item[1]
        if datasymtom.lower() in symtom.lower():
            found = True
            print(f"\nYou have {diagnosis.lower()}.")
    if not found:
        print("\nI could not find your symptom.")
    print("\nThank you for using the doctor.\n")

def main():
    symtom = welcome()
    database = handleData()
    compareSymtoms(symtom,database)

if __name__ == "__main__":
    main()