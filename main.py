

def Z1():
    a = "Python 2023"
    b = "Python 2023"
    c = "Python 2023"
    print("a==b? "+str(a==b))
    print("c==b? "+str(c==b))
    print("a")
    print(type(a))
    print(hex(id(a)))
    print("b")
    print(type(b))
    print(hex(id(b)))
    print("c")
    print(type(c))
    print(hex(id(c)))
    c = "Java 11"
    print("a==b? "+str(a==b))
    print("c==b? "+str(c==b))
    print("a")
    print(type(a))
    print(hex(id(a)))
    print("b")
    print(type(b))
    print(hex(id(b)))
    print("c")
    print(type(c))
    print(hex(id(c)))

def Z2():
    n1 = input("Wpisz pierwszą liczbę:\n")
    n2 = input("Wpisz drugą liczbę:\n")
    o = input("Wpisz operator:\n")
    try:
        exec(f"print({n1} {o} {n2})")
    except SyntaxError:
        print("Złe dane")
def Z3():
    slownik = {}
    dane = {"Jak masz na imię oraz nazwisko?":[],
            "1. Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:": '''oglądanie telewizji/filmów/seriali
czytanie książek/czasopism
słuchanie muzyki
spotkania z rodziną/przyjaciółmi
podróżowanie
uprawianie sportu
inne, jakie?'''.split("\n"),
            "2. W jakich okolicznościach czytasz książki najczęściej?":'''podczas podróży
w czasie wolnym (po pracy, na urlopie)
podczas pracy/nauki (to ich element)
w ogóle nie czytam
inne, jakie?'''.split("\n"),
            "3. Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?":'''chęć poszerzenia wiedzy
czytanie mnie relaksuje/odpręża
fakt, że czytanie jest modne
czytanie to moje hobby
konieczność nauki w związku z wykonywaną pracą/studiami
odczuwam presję rodziny/środowiska, żeby czytać
inny, jaki?'''.split("\n"),
            "4. Po książki w jakiej formie sięgasz najczęściej?":'''papierowej (tradycyjnej)
e-booki (książki elektroniczne) na komputerze
e-booki na tablecie/telefonie
e-booki na specjalnym czytniku (np. Kindle)'''.split("\n"),
            "5. Ile książek czytasz średnio w ciągu roku?":'''0
żadnej w całości - jedynie fragmenty
1
2 lub 3
4-10
powyżej 10'''.split("\n"),
            "6. Jak często średnio czytasz książki?":'''codziennie
raz w tygodniu
raz w miesiącu
raz na kilka miesięcy
raz na pół roku
raz na rok
wcale'''.split("\n"),
            "7. Po jakie gatunki książek sięgasz najczęściej?":'''kryminały/thrillery
romanse
psychologiczne
horrory
naukowe
dla dzieci i młodzieży
fantastykę
biograficzne
historyczne
science fiction
podróżnicze
hobbystyczne (gotowanie, wędkarstwo itp.)
przygodowe
poezję
inne, jakie?'''.split("\n")}
    for i in dane:
        print()
        print(i)
        odpowiedzi = dane[i]
        for j in range(len(odpowiedzi)):
            print(f"{j+1}) {odpowiedzi[j]}")
        if i != "Jak masz na imię oraz nazwisko?":
            wybrana=input("Wybierz wariant odpowiedzi: ")
            dane[i] = odpowiedzi[int(wybrana)-1]
        else: dane[i] = input()
    for pytanie in dane:
        print("pytanie: ",pytanie)
        print("odpowiedź: ",dane[pytanie])
if __name__ == '__main__':
    #Z1()
    #Z2()
    Z3()

