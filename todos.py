#Erstellen und Bearbeiten von Listen in Python

todos = ["Apfel", "Banane"]

for _ in range (3):  #Anzahl in der Klammer steht für die Anzahl der Wiederholungen
    newitem = input("Was möchtest du hinzufügen? ")  #Code muss für die schleife Eingerückt werden!!!!
    todos.append(newitem)
    print("Meine Liste hat folgende Elemente: ")
    for todo in todos:
        print(f"- {todos}")
print("programm Beendet")        



