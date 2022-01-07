from tkinter import *


#zdefiniowanie funkcji przycisków

#zdefiniowanie obliczeń
def calculate():
    try:                        #obsługa błędów
        PV = float(e_PV.get())
        a = float(e_a.get())
        i = float(e_i.get())/100
        n = float(e_n.get())

        if typ.get() == 0:          #na koniec okresu
                wynik = a * (((1+i)**n) - 1)/i + PV*((1+i)**n)
        else:                         #z góry/ na początek okresu
                wynik = a * (1+i)*((1+i)**n-1)/i + PV*((1+i)**(n))

        wynik = round(wynik, 2)
        e_FV.delete(0, END)
        e_FV.insert(0, str(wynik))

    except ZeroDivisionError: #stworzenie wyjąków
        e_FV.delete(0, END)
        e_FV.insert(0, "i nie może się równać 0")
    except ValueError:
        e_FV.delete(0, END)
        e_FV.insert(0, "podaj liczby")


#wyczyszczenie pól
def clear():
    for _ in [e_PV, e_a, e_i, e_n, e_FV]:
        _.delete(0, END)
    r2.select()

#zdefiniowanie kopiowania do schowka
def copyFV():
    a1 = e_FV.get()
    root.clipboard_clear()
    root.clipboard_append(a1)
    root.update()

#stworzenie okna
root = Tk()
root.title("Obliczenie wartości przyszłej kapitału FV")
root.geometry("550x215")

#stworzenie zmiennej typu kapitalizacji i fontu
typ = IntVar()
font = ("arialblack", 11)


#stworzenie interface
l2 = Label(root, text = "Podaj dane do obliczeń:", font = font)
e_PV = Entry(root, width=10, font = font)
e_a = Entry(root, width=10, font = font)
e_i = Entry(root, width=10, font = font)
e_n = Entry(root, width=10, font = font)

l_PV1 = Label(root, text = "PV", font = font)
l_a1 = Label(root, text = "a", font = font)
l_i1 = Label(root, text = "i", font = font)
l_n1 = Label(root, text = "n", font = font)

l_PV2 = Label(root, text =" - wartość początkowa", font = font)
l_a2 = Label(root, text = " - wpłacana rata", font = font)
l_i2 = Label(root, text = " - oprocentowanie dla okresu [%]", font = font)
l_n2 = Label(root, text = " - liczba wszystkich okresów płaności", font = font)


#frame na FV + FV
f1 = Frame(root)
l_FV = Label(f1, text = "FV to: ", font = font)
e_FV = Entry(f1, font = font)

#frame na przyciski + przyciski
f2 = Frame(root)
b1 = Button(f2, text = "Oblicz", padx = 5, pady = 5, width = 10, font = font, command = calculate)
b2 = Button(f2, text = "Wyczyść", padx = 5, pady = 5, width = 10, font = font, command = clear)
b3 = Button(f2, text = "Kopiuj Wynik", padx = 5, pady = 5, width = 10, font = font, command = copyFV)

#frame na radiobuttony
f3 = Frame(root)
l3 = Label(f3, text = "Rata wpłacana:", font = font)
r1 = Radiobutton(f3, text = "na koniec okresu", variable = typ, value = 0, font = font)
r2 = Radiobutton(f3, text = "na początek okresu", variable = typ, value = 1, font = font)
r2.select() #domyślnie wybierz na początek okresu

#zapakowanie
l2.grid(row = 1, column = 0, columnspan = 3, sticky = "W", padx = 5, pady = 2)
e_PV.grid(row = 2,column = 0, sticky = "W", padx = 5, pady = 3)
e_a.grid(row = 3,column = 0, sticky = "W", padx = 5, pady = 3)
e_i.grid(row = 4,column = 0, sticky = "W", padx = 5, pady = 3)
e_n.grid(row = 5,column = 0, sticky = "W", padx = 5, pady = 3)
l_PV1.grid(row = 2,column = 1)
l_a1.grid(row = 3,column = 1)
l_i1.grid(row = 4,column = 1)
l_n1.grid(row = 5,column = 1)

l_PV2.grid(row = 2,column = 2, sticky = "W")
l_a2.grid(row = 3,column = 2, sticky = "W")
l_i2.grid(row = 4,column = 2, sticky = "W")
l_n2.grid(row = 5,column = 2, sticky = "W")

#zapakowanie FV
l_FV.grid(row= 0, column = 0, sticky = "W")
e_FV.grid(row = 0, column = 1, columnspan = 1)
f1.grid(row = 6, column = 0, columnspan = 10, sticky = "W", padx = 5, pady = 3)

#zapakowanie przycisków
b1.grid(row = 0, column = 0, ipadx = 5, ipady = 5)
b2.grid(row = 0, column = 2, ipadx = 5, ipady = 5)
b3.grid(row = 0, column = 1, ipadx = 5, ipady = 5)
f2.grid(row = 7, column = 0, columnspan = 4)

#zapakowanie radiobuttonów
f3.grid(row = 1, column =  3, rowspan = 4, sticky = N, padx = 20, pady = 3)
l3.grid(row = 0, column = 0, sticky = "W")
r1.grid(row = 2, column = 0, sticky = "W")
r2.grid(row =1, column = 0, sticky = "W")

#główna pętla
root.mainloop()



