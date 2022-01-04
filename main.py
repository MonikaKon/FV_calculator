from tkinter import *

#stworzenie okna
root = Tk()
root.title("Obliczenie wartości przyszłej kapitału FV")
root.geometry("475x215")

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
l_a2 = Label(root, text = " - wpłacona rata na koniec okresu", font = font)
l_i2 = Label(root, text = " - oprocentowanie dla okresu [%]", font = font)
l_n2 = Label(root, text = " - liczba okresów kapitalizacji", font = font)


#frame na FV + FV
f1 = Frame(root)
l_FV = Label(f1, text = "FV to: ", font = font)
e_FV = Entry(f1, font = font)

#frame na przyciski + przyciski
f2 = Frame(root)
b1 = Button(f2, text = "Oblicz", padx = 5, pady = 5, width = 10, font = font)
b2 = Button(f2, text = "Wyczyść", padx = 5, pady = 5, width = 10, font = font)
b3 = Button(f2, text = "Kopiuj Wynik", padx = 5, pady = 5, width = 10, font = font)

#frame na radiobuttony
f3 = Frame(root)
l3 = Label(f3, text = "Typ kapitalizacji:", font = font)
r1 = Radiobutton(f3, text = "z dołu", variable = typ, value = 0, font = font)
r2 = Radiobutton(f3, text = "z góry", variable = typ, value = 1, font = font)

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
r1.grid(row = 1, column = 0, sticky = "E")
r2.grid(row =2, column = 0, sticky = "E")

#główna pętla
root.mainloop()



