markdown_content = """
# 📝 Projekt: Aplikacja budżetowa w Pythonie z GUI (Flet)

## 🎯 Cel projektu

Stworzenie aplikacji desktopowej (GUI), która pomaga w zarządzaniu domowym budżetem.

**Główne funkcje:**
- Zarządzanie **wpływami** i **wydatkami**.
- Wydatki dzielą się na kategorie (np. jedzenie, dom, raty...).
- **Stałe wydatki** (np. subskrypcje, raty) mają przypisaną stałą kwotę i powtarzają się co miesiąc.
- Aplikacja wspiera **planowanie na przyszły miesiąc** i pilnowanie dostępnego budżetu.

## 🛠️ Technologia

- **Język:** Python 3.10+
- **GUI:** [Flet](https://flet.dev)
- **Dane:** JSON (przechowywane lokalnie w katalogu `data/`)
- **Brak** Tkintera, brak zewnętrznych baz danych na start

## 🗂️ Struktura projektu (planowana)

budget_app/

├── data/ # folder na pliki JSON

│ ├── incomes.json

│ └── expenses.json

├── models.py # Klasy danych: Income, Expense

├── storage.py # Obsługa zapisu/odczytu JSON

├── constants.py # Kategorie wpływów i wydatków

├── ui/

│ └── main_view.py # Komponenty GUI w Flet

├── main.py # Punkt wejścia do aplikacji


## ✅ Gotowe do tej pory:

### ✔️ `models.py`
- Klasy: `Operation` (bazowa), `Income`, `Expense`
- Każda ma:
  - `title` (nazwa operacji)
  - `amount` (kwota)
  - `category` (np. "Jedzenie", "Pensja")
  - `date` (`datetime.date`)
  - `subscription` (dla `Expense`, określa czy wydatek się powtarza)
- Dodane metody:
  - `.to_dict()` – konwersja na słownik dla zapisu do JSON
  - (zadanie 2 będzie dotyczyło `.from_dict()`)

### ✔️ GUI
- Użytkownik wybrał **Flet** jako framework do GUI
- Pierwsza wersja strony powitalnej działa

## 📋 Zadania wykonane:

### Zadanie 1: `to_dict()`  
Zaimplementowane w klasach danych, pozwala na zapis do JSON.

## 📌 Zadania do zrobienia dalej:

### 🔸 Zadanie 2: `from_dict()` w `Income` i `Expense`
- Umożliwi odczyt danych z pliku JSON
- Obsługa konwersji daty (`str -> datetime.date`)

### 🔸 Zadanie 3: `storage.py` z obsługą plików JSON
- Zapisywanie danych do `incomes.json`, `expenses.json`
- Ładowanie danych przy starcie
- Tworzenie plików i folderów, jeśli nie istnieją

### 🔸 Zadanie 4: Inicjalizacja aplikacji
- Funkcja `initialize_storage()` – ładowanie danych
- Tworzenie zmiennych `incomes`, `expenses`

### 🔸 Zadanie 5: Dodawanie danych
- `add_income()`, `add_expense()` – dodają i zapisują dane

## 🔜 Co dalej?

Po zadaniach związanych z JSON:
- Budowa GUI do:
  - dodawania wpływów i wydatków
  - wyświetlania podsumowania
  - planowania miesiąca
- Obsługa daty, miesięcy, automatycznego kopiowania stałych wydatków

## 💾 Eksport i kontynuacja

- Możesz tę notatkę:
  - dołączyć do repozytorium (np. GitHub, lokalne Git),
  - wkleić do folderu projektu jako plik `.md`,
  - wkleić do notatnika (Notion, Obsidian, cokolwiek).
- W przyszłości, w nowym czacie możesz mi wkleić ten plik i kontynuujemy bez tłumaczenia.
"""

with open("README_BudgetApp.md", "w", encoding="utf-8") as f:
    f.write(markdown_content)

print("Plik README_BudgetApp.md został zapisany.")
