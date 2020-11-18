# Zadanie kalkulator

# Dodawanie
def add(x, y):
    return x + y
# Odejmowanie

def subtract(x, y):
    return x - y
# Mnożenie

def multiply(x, y):
    return x * y
# Dzielenie

def divide(x, y):
    return x / y


print("Podaj działanie, posługując się odpowiednią liczbą:")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")

while True:
    # Take input from the user
    choice = input("Wybierz działanie(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Podaj składnik 1: "))
        num2 = float(input("Podaj składnik 2: "))

        if choice == '1':
            print(num1, "+", num2, "=", "Wynik to", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", "Wynik to", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", "Wynik to", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", "Wynik to", divide(num1, num2))
        break
    else:
        print("Błąd")