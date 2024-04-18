#Pyta o nazwę pliku
fname = input("Enter file: ")
#Stawia warunek dotyczący nazwy pliku w innym przypadku wybiera plik domyślny
if len(fname) < 1 : fname = "words.txt"

#Otwiera plik
fhand = open(fname)

#Włączenie słownika, który służy do przechowywania wartości danych w parach klucz:wartość.
many = dict()

#Wycięcie zbędnych znaków końcowych i podział wyrazów
for line in fhand :
    line = line.rstrip()
    wds = line.split()
    
    #Zwraca wartość elementu o określonym kluczu
    for w in wds:
        many[w] = many.get(w, 0) + 1
        

#Znajduje 5 najczęściej występującyh wyrazów i wypisuje ich częstotliwość
tmp = dict()
newlist = list()
for k,v in many.items() :
    tup = (v,k)
    # Tu dodaje elementy na końcu istniejącego obiektu listy
    newlist.append(tup)

#Tworzy listę z sortowaniem
cool = sorted(newlist, reverse=True)

#5 Elementów
for v,k in cool[:5] :
    print(k,v)