quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'


print(quote.endswith('eet')) # czy tekst kończy się...

print(quote.islower()) #czy tekst jest zapisany małymi literami

print(quote.upper()) #format tekstu na duże litery

print(quote.upper().isupper()) #czy ten tekst jest złożony tylko z dużych liter

print(quote.find('is')) #wskazuje pierwszy indeks, tam gdzie tekst się pojawił

print(quote.find('is', 19)) #od którego znaku chcę szukać (-1 nic nie zostało znalezione)

# print(quote.replace('a', 4))- błąd/ liczba

print(quote.replace('a', "4")) #zamienia znaki

print(quote.split(' ')) #seperator, dzieli spacją- wynikiem jest tabela w której każde słowo jest oddzielnym el.




#2.Konkatenacja + znaki specjalne

drive='C:\\'
folder='scripts\\python\\'
file='myscript.py'

path = drive + folder + file
print(path)

justText = "text with\nnewline"
print(justText)

justTextR = r"text with\nnewline"
print(justTextR)




#3.Dodawanie liczby i stringów

somethingLinkeNumber = '1000'
print(somethingLinkeNumber)

#somethingLinkeNumber + 1 błąd/nie mogę dodać stringa do number

print(int(somethingLinkeNumber) + 1)#konwertuje string na number
print(somethingLinkeNumber + str(1))#konwertuje number na string

print(type(somethingLinkeNumber))#sprawdzam typ danych-string