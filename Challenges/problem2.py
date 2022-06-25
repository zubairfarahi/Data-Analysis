

def p1():
    """
    Ex. 2: Modificati urmatoarea bucata de cod astfel incat
    la rulare, rezultatul afisarii sa fie cele 2 liste concatenate.
    HINT: Exista mai multe moduri prin care puteti face asta.
    """
    # Ii dam variabilei l1 ca si valoare o lista cu 4 elemente (1,2,3,4)
    # si variabilei l2 ca valoare o lista cu 4 elemente (5,6,7)
    l1 = [1, 2, 3, 4]
    l2 = [5, 6, 7]

    # Afisam listele l1 si l2 separat.
    # Pentru a vedea rezultatul, rulati acest script.
    print(l1)
    print(l2)
    print(l1 + l2)
    


def p2():
    """
    Ex. 3: Modificati urmatoarea bucata de cod astfel incat
    la rulare, in loc sa ne oprim din adaugat elementele primite de la
    tastatura in lista pana sa primim 'exit', ne vom opri cand vom primi 'stop'
    """

    # Cream o variabila l1 care are ca si valoare o lista goala
    l1 = []

    # Preluam input de la tastatura si il salvam in variabila x
    x = input()

    # Cat timp de la tastatura nu primim exit ca si valoare
    while x != 'exit':
        # Adaugam la lista elementul nou primit de la tastatura
        l1.append(x)
        x = input()

    # Afisam lista l1.
    print(l1)

def p3():
    """
    Ex. 4: Modificati urmatoarea bucata de cod astfel incat
    la rulare, lista rezultata sa fie [1, 2, 2, 3, 4, 5]
    """

    # In variabila t1 vom stoca un tuplu cu 2 elemente, 1 si 2
    # iar in variabila t2 vom stoca un tuplu cu 3 element 3, 4, 5
    t1 = (1, 2)
    t2 = (3, 4, 5)

    # Vom crea variabila l1 iar ca si valoare, va avea o lista compusa din
    # concatenarea celor 2 tupluri. Primele elemente vor fi cele din l1.
    # Vom converti cele 2 tupluri in liste, inainte sa le concatenam
    l1 = list(t1) + list(t2)

    # Afisam lista
    print(l1)

def p4():
    """
    Ex. 5: Modificati urmatoarea bucata de cod astfel incat
    la rulare, sa afisati toate valorile dictionarului d1
    """

    # In variabila d1 vom salva urmatorul dictionar:
    d1 = {
        1: 'CMI',
        2: 'CMI2'
    }

    # Afisam tate cheile dictionarului d1, folosind metoda keys()
    print(d1.keys())

def p5():
    """
    Ex. 6: Modificati urmatoarea bucata de cod astfel incat
    la rulare, la a doua afisare, sa avem inca un element in dictionar,
    cu cheia 3 si valoarea 'CMI3'
    """

    # In variabila d1 vom salva urmatorul dictionar:
    d1 = {
        1: 'CMI',
        2: 'CMI2'
    }

    # Afisam dictionarul inainte de schimbare
    print(d1)

    # Schimbam valoarea de la cheia 2, din 'CMI2' in 'CMI'
    d1[2] = 'CMI'

    # Afisam dictionarul dupa schimbare
    print(d1)

def p6():
    """
    Ex. 7: Modificati urmatoarea bucata de cod astfel incat
    la rulare, la a doua afisare, in set sa existe si elementele din lista.
    Va veti folosi de lista, veti accesa elementele si le veti adauga in set.
    """

    # In variabila s1 vom salva urmatorul set
    s1 = {1, 2, 3}

    # Cream variabila l1 ca o lista cu urmatoarele elemente:
    l1 = [1, 4, 4, 5, 6]

    # Afisam setul inainte de schimbare
    print(s1)

    # Adaugam valoarea 4 setului folosind metoda add()
    s1.add(4)

    # Afisam setul dupa schimbare
    print(s1)

def p7():
    """
    Ex. 8: Modificati urmatoarea bucata de cod astfel incat
    la rulare, daca valoarea care vine de la tastatura nu este 'cmi'
    sa afisam 'NOT OK'
    """

    # In x vom salvea valoarea care vine de la tastatura
    x = input()

    # Daca valorea care vine de la tastatura este 'cmi', vom afisa 'OK'
    if x == 'da':
        print('OK')

def p8():
    """
    Ex. 9: Modificati urmatoarea bucata de cod astfel incat
    la rulare, sa afisati doar elementele pare de la 0 la x
    """

    # In x vom salvea valoarea care vine de la tastatura
    x = input()

    # Convertim valoarea care vine de la tastatura intr-un intreg
    x = int(x)

    # Vom printa toate numerele intregi de la 0 pana la x (primit de la tastatura)
    # functia range(x) ne va intoarce lista de elemente intregi [0, 1, 2, .., x]
    # Iteram prin toate elementele listei oferite de functia range()
    for i in range(x):
        print(i)

def p9():
    
    """
        Ex. 10: Modificati urmatoarea bucata de cod astfel incat
        la rulare, sa printati dictionarul d1 care va avea ca si chei elementele
        din l1 iar ca valori, elementele din l2
        Raspunsul corect la printare arata asa:
        {
            1: 'a',
            2: 'b',
            3: 'c',
            4: 'd'
        }
    """

    # In variabila l1 si l2 avem urmtoarele liste:
    l1 = [1, 2, 3, 4]
    l2 = ['a', 'b', 'c', 'd']

    # In varaibila d1 avem un dictionar gol
    d1 = {}

    # Afisam listele l1 si l2
    print(l1, l2)


def main():
    p1()


if __name__ == '__main__':
    main()