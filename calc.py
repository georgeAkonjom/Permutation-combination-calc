def interface():
    print("This program Returns a Permutation given the total of a set of objects, N and a sample, R\n")
    try:
        inputN = int(input("Input total number of objects (N): "))
        inputR = int(input("Input sample of objects (R): "))
    except ValueError:
        print("Both inputs must be integers, Not complex or floating point; Only counting numbers. Try again\n")
        factorialOfInput()
    return(inputN, inputR)


# recursive function, returns the factorial of an input int n
def factorial(n):
    return 1 if (n == 1) else n * factorial(n - 1)

# resolves and prints the factorial value of the input int (from the interface() func) using the factorial() func
def factorialOfInput():
        n, r= interface()
        if r > n:
            print("Aw hell nah, You know I can't do that shit. (Basically R has to be smaller than N, but you already knew that, didn't you?) Try again...\n")
            factorialOfInput()
            return -1
        nless = n - r
        nfactorial = factorial(n)
        rfactorial = factorial(r)
        nlessfactorial = factorial(nless)
        permutation = str(nfactorial / (nlessfactorial))
        combination = str(nfactorial / (rfactorial*(nlessfactorial)))
        print(str(n) + "! = ",nfactorial,)
        print(str(r) + "! = ",rfactorial)
        print(permutation + " possible permutations")
        print(combination + " possible combinations")
    

factorialOfInput()
