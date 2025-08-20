
# Python to język interpretowany (nie trzeba kompilować), tylko interpretowany – kod jest wykonywany linijka po linijce.

# Wpisując "python" w terminalu, wchodzisz w tryb interaktywny (REPL)
# Aby zakończyć: wpisz exit() albo Ctrl + Z (Windows) / Ctrl + D (Linux/macOS)
#Mogę uruchomić srodowisko do Pythona przez przeglądarke-Jupyter Notebook 

#Jupyter Notebook(Anaconda) który można również zainstalować i uzywać na komputerze- ale muszę mieć zaintalowanego już Pythona
#Kod można pisać w dowolnym edytorze, choćby w notatniku, i poprzez uruchominie pliku w lokalnym wierszu poleceń(cmd), wywoływac plik
#Edytorów do pracy z pythonem jest na prawde dużo np.Spyder

'''gddsfdsf''' #komentarz blokowy :)

#Funkcja print() - console.log()
#Może wyświetlać jedną- wiele wartości, przedzielonych przecinkami
#Wyświetlać można teksty, zmienne, liczby, mogę umieścić znaki specjalne


# --- WYPISYWANIE NA EKRAN ---

print("Hello world")          # Wypisze: Hello world
print(5 + 7)                  # Wypisze: 12
print("Python" * 3)           # Wypisze: PythonPythonPython
print("Imię:", "Jan")         # Można wypisać kilka rzeczy naraz

# --- ZMIENNE ---

tekst = "To jest zmienna tekstowa"
liczba = "123"                # input zawsze zwraca tekst!

print(tekst)
print("Liczba jako tekst:", liczba)

# --- POBIERANIE DANYCH OD UŻYTKOWNIKA ---

imie = input("Podaj swoje imię: ")
miasto = input("Skąd jesteś? ")

print("Cześć", imie + "!")
print("Miło, że jesteś z", miasto)

# --- OPERACJE NA TEKSTACH ---

ulubiony_kolor = input("Jaki jest Twój ulubiony kolor? ")
print("Twój kolor to:", ulubiony_kolor * 2)  # Powtórzenie tekstu

# --- ŁĄCZENIE ZMIENNYCH ---

greeting = "Witaj"
name = input("Podaj swoje imię: ")

print(greeting + " " + name)  # Łączenie tekstów (konkatenacja)


