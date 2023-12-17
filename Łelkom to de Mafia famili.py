from tkinter import *
from tkinter import messagebox

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title('Formularz mafia')
        self.geometry("600x700")
        self.resizable(0, 0)

class Przycisk(Button):
    def __init__(self, name):
        super().__init__(text=name, padx=50, pady=20, command=self.send)
    def send(self):
        plik =open('formularz.txt', 'w')
        plik.write(f'imie: {imie.get()}\nnzawisko: {nazwisko.get()}\nwiek: {wiek.get()}\nNumer telefonu: {telefon.get()}\nPseudonim: {pseudonim.get()}\nPłeć: {plec.get()}\nPraca: {praca.get()}\nDoświadczenie: {doswiadczenie.get()}\nPrawo jazdy: {PrawoJazdy.prawojazdy}\nOcena filmu: {scroll.get()}\nLubi {lista}\nPodpis: {podpis.get()}')
        plik.close()

class Input(Entry):
     def __init__(self):
        super().__init__()

class Suwak(Scale):
     def __init__(self, od, do, orient):
        super().__init__(to=do, from_=od, orient=orient)

class Licznik(Spinbox):
     def __init__(self, od, do):
        super().__init__(to=do, from_=od)

class Napis(Label):
    def __init__(self, text, rozmiar='10', pady=10):
        super().__init__(text=text, font=('Arial', rozmiar), pady=pady)

class PrawoJazdy(Radiobutton):
    prawojazdy=''
    def __init__(self, text, value):
        self.text=text
        super().__init__(text=text, value=value, command=self.wybor)
    def wybor(self):
        PrawoJazdy.prawojazdy=self.text

class Jedzenie(Checkbutton):
    def __init__(self, text, var):
        self.text=text
        self.var=var
        super().__init__(text=text, command=sprawdz, variable=self.var)
def sprawdz():
    global lista
    lista=[]
    for x in [makaron, pizza, oliwki, wino]:
        if x.var.get()==1:
            lista.append(x.text)
okno=Window()  

cP=IntVar()
cO=IntVar()
cM=IntVar()
cW=IntVar()


send=Przycisk('Wyślij')
imie=Input()
nazwisko=Input()
doswiadczenie=Input()
wiek=Licznik(1, 100)
Header=Napis('Formulattio de la mafio', 25)
Limie=Napis('Namo')
Lnazwisko=Napis('Lasto Namo')
Ldoswiadczenie=Napis("Heva u don' this alredy?")
Lwiek=Napis('Età')
telefon=Input()
Ltelefon=Napis('Numero telefono')
pseudonim=Input()
LPseudonim=Napis('Mafia Namo')
Lpraca=Napis('Where you get money from now?')
praca=Input()
Lplec=Napis('R u man or a gal?')
plec=Input()
tak=PrawoJazdy('Si', 'T')
nie=PrawoJazdy('No', 'N')
LPrawoJazdy=Napis('Do u have a car?')
Lscroll=Napis('In scalo 1 - 10 how mucho you like "God Fatha"')
scroll=Suwak(1, 10, 'horizontal')
Ljedzenie=Napis('U like:')
makaron=Jedzenie('Pasta', cM)
pizza=Jedzenie('Pizza', cP)
oliwki=Jedzenie('Olive', cO)
wino=Jedzenie('Vino', cW)
Lbenefity=Napis('Benefito from membership:', pady=3)
b1=Napis('- Nice suit', pady=2)
b2=Napis('- Moni $$$', pady=2)
Lpodpis=Napis('If u R ready to sell ur soul, then sign here')
podpis=Input()

Header.grid(column=1, row=0, columnspan=4)
Limie.grid(column=1, row=1)
imie.grid(column=2, row=1)
Lnazwisko.grid(column=3, row=1)
nazwisko.grid(column=4, row=1)
Lwiek.grid(column=1, row=3)
wiek.grid(column=2, row=3)
Ltelefon.grid(column=3, row=3)
telefon.grid(column=4, row=3)
LPseudonim.grid(column=1, row=4, columnspan=2)
pseudonim.grid(column=3, row=4)
Lplec.grid(column=1, row=5)
plec.grid(column=2, row=5)
Lpraca.grid(column=3, row=5)
praca.grid(column=4, row=5)
Ldoswiadczenie.grid(column=1, row=6, columnspan=2)
doswiadczenie.grid(column=3, row=6)
LPrawoJazdy.grid(column=1, row=7, columnspan=2)
tak.grid(column=3, row=7)
nie.grid(column=4, row=7)
Lscroll.grid(column=1, row=8, columnspan=3)
scroll.grid(column=4, row=8)
Ljedzenie.grid(column=1, row=11)
makaron.grid(column=2, row=11)
pizza.grid(column=2, row=12)
oliwki.grid(column=2, row=13)
wino.grid(column=2, row=14)
Lbenefity.grid(column=1, row=15, columnspan=2)
b1.grid(column=1, row=16)
b2.grid(column=1, row=17)
Lpodpis.grid(column=1, row=18, columnspan=4)
podpis.grid(column=3, row=19)
send.grid(column=3, row=20)

okno.mainloop()

