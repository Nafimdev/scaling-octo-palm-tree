def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    if b == 0:
        print("Division Error")
    else:
        return a/b

def mod(a,b):
    return a%b
while True :
    print("\n--- Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo")
    print("6. Exit")
    
    choice = input("Enter Your Choice:")
    if choice == "6" :
        print (" Menu Closed")
        break
    elif choice in ["1","2","3","4","5"]:
        a = float(input(" Enter Your First Number :"))
        b = float(input(" Enter Your Second Number:"))
    else :
        print("Choice Error")    
    if choice == "1":
        print ("Answer =", add(a,b))
    elif choice == "2":
        print ("Answer =", sub(a,b))
    elif choice == "3":
        print ("Answer =", mult(a,b))
    elif choice == "4":
        print ("Answer =", div(a,b))
    elif choice == "5":
        print ("Answer =", mod(a,b))     
    else :
        print ("Put only Numbers ! ")