#Citirea unei liste de numere float. Citirile repetate suprascriu listele precedente.
def citireLista():
    l = []
    givenString = input("Dati lista, cu elementele separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(float(x))
    return l

#Afișarea părții întregi a tuturor numerelor din listă. Definim partea întreagă a unui număr float
#ca fiind numărul obținut prin eliminarea cifrelor de după virgulă.
#Exemplu: [1.5, -3.3, 8, 9.8, 3.2] -> [1, -3, 8, 9, 3]

def parteIntreagaNumar(l):
    '''
    afiseaza partile intregi ale tuturor numerelor din lista
    :param l:lista de floaturi
    :return:partea intreaga a fiecarui numar din lista data
    '''
    rezultat=[]
    for x in l:
        y=int(x)
        rezultat.append(y)
    return rezultat

def testParteIntreagaNumar():
    assert parteIntreagaNumar([1.5, -3.3, 8, 9.8, 3.2]) == [1, -3, 8, 9, 3]
    assert parteIntreagaNumar([1.0, 9.8, 7.0]) == [1, 9, 7]


#Să se afișeze toate numerele care aparțin unui interval deschis citit de la tastatură.
#Exemplu: [1.5, -3.3, 8, 9.8, 3.2] și intervalul cu capetele -4 și 5 -> [1.5, -3.3, 3.2]

def numereInIntervalDeschis(l, a, b):
    '''
    Afiseaza toate numerele care apartin unui interval deschis citit de la tastatura
    :param l: lista de floaturi
    :return: numerele care apartin unui interval deschis citit de la tastatura (neordonate)
    '''

    rezultat = []
    for x in l:
        if x>a and x<b:
            rezultat.append(x)
    return rezultat


def testNumereInIntervalDeschis():
    assert numereInIntervalDeschis([1.5, -3.3, 8, 9.8, 3.2], -4, 5) == [1.5, -3.3, 3.2]
    assert numereInIntervalDeschis([1.0, 9.8, 7.0], 0, 11) == [1.0, 9.8, 7.0]

#Afișarea tuturor numerelor a căror parte întreagă este divizor al părții fracționare (numărul
#format din cifrele de după virgulă).
#Exemplu: [1.5, -3.3, 8, 9.8, 3.2] -> [1.5, -3.3]

def pi(x):
    xStr = str(x)
    parte = xStr.split(".")[0]
    p = float(parte)
    if p<0:
        return -p
    else:
        return p

def pf(x):
    xStr = str(x)
    parte = xStr.split(".")[1]
    p = float(parte)
    return p

def numereParteIntreagaDivizibilaParteFractionala(l):
    '''
    Afișarea tuturor numerelor a căror parte întreagă este divizor al părții fracționare
    :param l:lista de floaturi
    :return: lista numerelor a căror parte întreagă este divizor al părții fracționare
    '''
    rezultat=[]
    for j in l:
        i = float(j)
        if pf(i) % pi(i) == 0 and i != int(i):
            rezultat.append(i)
    return rezultat

def testNumereParteIntreagaDivizibilaParteFractionala():
    assert numereParteIntreagaDivizibilaParteFractionala([1.5, -3.3, 8, 9.8, 3.2]) == [1.5, -3.3]
    assert numereParteIntreagaDivizibilaParteFractionala([1.0, 9.8, 7.0]) == []

#Afișarea listei obținute din lista inițială în care numerele sunt înlocuite cu un string format din
#cuvinte care le descriu caracter cu caracter. Vezi exemplul pentru detalii.
#Exemplu: [1.5, -3.3, 8, 9.8, 3.2, 14.52] -> [‘unuvirgulacinci’, ‘minustreivirgulatrei’, ‘opt’,
#‘nouavirgulaopt’, ‘treivirguladoi’, ‘unupatruvirgulacincidoi’].

def main():
    testParteIntreagaNumar()
    testNumereInIntervalDeschis()
    testNumereParteIntreagaDivizibilaParteFractionala()
    l = []
    while True:
        print("1. Citire lista")
        print("2. Afișarea părții întregi a tuturor numerelor din listă. Definim partea întreagă a unui număr float ca fiind numărul obținut prin eliminarea cifrelor de după virgulă.")
        print("3. Să se afișeze toate numerele care aparțin unui interval deschis citit de la tastatură.")
        print("4. Afișarea tuturor numerelor a căror parte întreagă este divizor al părții fracționare (numărul format din cifrele de după virgulă).")
        print("------------------------")
        print("a. Afisare lista")
        print("x. Iesire")

        optiune = input("Dati optiunea: ")

        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(parteIntreagaNumar(l))
        elif optiune == "3":
            a = int(input("Dati capatul inferior al intervalului: "))
            b = int(input("Dati capatul superior al intervalului: "))
            print(numereInIntervalDeschis(l, a, b))
        elif optiune == "4":
            print(numereParteIntreagaDivizibilaParteFractionala(l))
        # ---------------------
        elif optiune == "a":
            print(l)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
if __name__ == '__main__':
    main()






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
