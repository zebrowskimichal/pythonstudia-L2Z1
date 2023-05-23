import math


class Funkcja:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def rozwiaz(self):
        if self.a == 0:
            if self.b == 0:
                if self.c == 0:
                    print("Funkcja ma nieskonczenie wiele rozwiazan")
                else:
                    print("Funkcja nie ma rozwiazan")
            else:
                print("Funkcja jest liniowa")
                ##Zmiana- byl błąd w klasie, wcześniejsza funkcja źle liczyła miejsca zerowe funkcji liniowej
                miejsce = ((-1) * self.c) / self.b
                print("Miejsce zerowe: " + str(miejsce))
        else:
            print("Funkcja kwadratowa")
            delta = (self.b**2) - (4 * self.a * self.c)
            if delta < 0:
                print("Funkcja nie ma miejsc zerowych!")
            if delta == 0:
                print("Funkcja ma jedno miejsce zerowe")
                miejsce = (-self.b) / 2 * self.a
                print("Miejsce zerowe, to: " + miejsce)
            if delta > 0:
                print("Funkcja ma dwa miejsca zerowe")
                pierwiastek = math.sqrt(delta)
                miejsce1 = float(((-self.b) - pierwiastek) / 2 * self.a)
                miejsce2 = float(((-self.b) + pierwiastek) / 2 * self.a)
                print(
                    "Pierwsze miejsce zerowe, to: "
                    + str(miejsce1)
                    + ", a drugie miejsce zerowe, to: "
                    + str(miejsce2)
                )


class FunkcjaKwadratowa(Funkcja):
    pass


class FunkcjaLiniowa(Funkcja):
    pass


##Przykladowe testy

testL = FunkcjaLiniowa(0, 5, -15)
testL.rozwiaz()

testK = FunkcjaKwadratowa(20, 40, 15)
testK.rozwiaz()


class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik

    def pokaz(self):
        print(str(self.licznik) + ", " + str(self.mianownik))

    def skroc(self):
        wynik = math.gcd(self.licznik, self.mianownik)
        self.licznik //= wynik
        self.mianownik //= wynik
        print("Skrocony ulamek: " + str(self.licznik) + "/" + str(self.mianownik))
        print("")

    @staticmethod
    def dodaj(l1, l2):
        mianownikWynik = l1.mianownik * l2.mianownik
        licznikWynik = (l1.licznik * l2.mianownik) + (l2.licznik * l1.mianownik)
        wynik = UlamekZ(licznikWynik, mianownikWynik)
        print(
            "Wynik dodawania ulamkow: "
            + str(l1.licznik)
            + "/"
            + str(l1.mianownik)
            + " i "
            + str(l2.licznik)
            + "/"
            + str(l2.mianownik)
            + " daje wynik: "
        )
        print(str(licznikWynik) + "/" + str(mianownikWynik))
        wynik.skroc()

    @staticmethod
    def odejmij(l1, l2):
        mianownikWynik = l1.mianownik * l2.mianownik
        licznikWynik = (l1.licznik * l2.mianownik) - (l2.licznik * l1.mianownik)
        wynik = UlamekZ(licznikWynik, mianownikWynik)
        print(
            "Wynik odejmowania ulamkow: "
            + str(l1.licznik)
            + "/"
            + str(l1.mianownik)
            + " i "
            + str(l2.licznik)
            + "/"
            + str(l2.mianownik)
            + " daje wynik: "
        )
        print(str(licznikWynik) + "/" + str(mianownikWynik))
        wynik.skroc()

    @staticmethod
    def mnoz(l1, l2):
        mianownikWynik = l1.mianownik * l2.mianownik
        licznikWynik = l1.licznik * l2.licznik
        wynik = UlamekZ(licznikWynik, mianownikWynik)
        print(
            "Wynik mnozenia ulamkow: "
            + str(l1.licznik)
            + "/"
            + str(l1.mianownik)
            + " i "
            + str(l2.licznik)
            + "/"
            + str(l2.mianownik)
            + " daje wynik: "
        )
        print(str(licznikWynik) + "/" + str(mianownikWynik))
        wynik.skroc()

    @staticmethod
    def dziel(l1, l2):
        mianownikWynik = l1.mianownik * l2.licznik
        licznikWynik = l1.licznik * l2.mianownik
        wynik = UlamekZ(licznikWynik, mianownikWynik)
        print(
            "Wynik mnozenia ulamkow: "
            + str(l1.licznik)
            + "/"
            + str(l1.mianownik)
            + " i "
            + str(l2.licznik)
            + "/"
            + str(l2.mianownik)
            + " daje wynik: "
        )
        print(str(licznikWynik) + "/" + str(mianownikWynik))
        wynik.skroc()


class UlamekZ(Ulamek):
    pass


class UlamekD(Ulamek):
    def __init__(self, liczba):
        mianownik = 10**4
        if 10 <= mianownik <= 10**4:
            licznik = int(liczba * mianownik)
            super().__init__(licznik, mianownik)
        else:
            print("Błąd: Mianownik powinien być liczbą z przedziału od 10 do 10^4.")


##Przykladowe testy
print("")
test = UlamekD(0.35)
test.pokaz()
test2 = UlamekD(0.5)
UlamekZ.dodaj(test, test2)

test3 = UlamekZ(5, 8)
test4 = UlamekZ(6, 4)
UlamekZ.dodaj(test3, test4)
