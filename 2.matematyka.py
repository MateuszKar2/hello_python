# Python obsługuje działania matematyczne jak kalkulator
# Jest oparty na zasadach matematyki (kolejność działań, potęgowanie itd.)

# --- PODSTAWOWE OPERACJE ---

print(5 / 2)     # Dzielenie (wynik zmiennoprzecinkowy): 2.5
print(5 // 2)    # Dzielenie całkowite (zaokrągla w dół): 2
print(5 % 2)     # Reszta z dzielenia (modulo): 1
print(2 ** 3)    # Potęgowanie: 8 (czyli 2 * 2 * 2)

# --- SKRÓCONA SKŁADNIA DLA OPERACJI NA ZMIENNYCH ---

x = 5
x += 1           # To samo co: x = x + 1
print(x)         # Wynik: 6

# Można też używać innych skrótów:
x -= 2           # Odejmowanie: x = x - 2 → teraz x = 4
print(x)

x *= 3           # Mnożenie: x = x * 3 → teraz x = 12
print(x)

x //= 2          # Dzielenie całkowite: x = x // 2 → teraz x = 6
print(x)

x **= 2          # Potęgowanie: x = x ** 2 → teraz x = 36
print(x)




print("Konwersja:")

# Pobieranie danych (zawsze jako tekst - string)
a = input("Podaj 1 liczbę: ")
b = input("Podaj 2 liczbę: ")

# Konkatenacja (łączenie tekstów) - np. 5 + 5 = "55"
print(a + b)  # wynik: 55 (jeśli podasz 5 i 5)

# Konwersja na liczby całkowite (int)
print(int(a) + int(b))  # wynik: 10

# Konwersja na liczby zmiennoprzecinkowe (float)
# UWAGA: używamy kropki, np. 5.5 – nie przecinka!
print(float(a) + float(b))  # np. 5.5 + 2.5 = 8.0





#Konwersja liczby na tekst i odwrotnie
y = 2
z = 2

print(y + z)  # wynik: 4 (działanie matematyczne)

# Konwersja liczb na tekst i ich łączenie
print(str(y) + str(z))  # wynik: "22" (konkatenacja stringów)





#Usuwanie zmiennej
del y  # Usuwa zmienną y z pamięci

# print(y)  # Błąd! Zmienna y już nie istnieje