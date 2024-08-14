
absender = input("Wer ist der Absender? ")


def generate_newsletter(absender):
    name = input ("An wen geht die Nachricht? ")
    print("Hallo " + name )
    print("") #Leerzeile
    print("Mit dieser E-Mail möchte ich dich über meiner neue Adresse informieren")
    print("") #Leerzeile
    print("Musterstraße 12")
    print("12345 Musterhausen")
    print("Viele Grüße")
    print("") #Leerzeile
    print("" + absender)

generate_newsletter(absender)    