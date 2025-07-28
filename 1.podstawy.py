# Python to język interpretowany (nie trzeba kompilować), tylko interpretowany – kod jest wykonywany linijka po linijce.

# Wpisując "python" w terminalu, wchodzisz w tryb interaktywny (REPL)
# Aby zakończyć: wpisz exit() albo Ctrl + Z (Windows) / Ctrl + D (Linux/macOS)

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


