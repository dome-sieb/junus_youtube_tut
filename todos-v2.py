#Erstellen und Bearbeiten von Listen in Python

todos = []


for _ in range (3):

    print("Was willst du tun?")
    print("(1) To-dos anzeigen")
    print("(2) To-dos hinzufügen")

    option = input("Bitte auswählen: ")

    if int(option) == 1:
        print("Meine Liste hat folgende Elemente: ")
        for todo in todos:
            print(f"- {todos}")

    if int(option) == 2:
        newitem = input("Was möchtest du hinzufügen? ")  #Code muss für die schleife Eingerückt werden!!!!
        todos.append(newitem)

  #Anzahl in der Klammer steht für die Anzahl der Wiederholungen
   
   
print("programm Beendet")        



