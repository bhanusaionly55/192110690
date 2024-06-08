from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def calc(request):
    val = request.POST.get('dig', '')
    x = map(int, val.split())
    z = list(x)
    return render(request, 'calc.html', {'digit': z})

def even(request):
    val = request.POST.get('dig', '')
    x = map(int, val.split())
    z = list(x)
    evens = [i for i in z if i % 2 == 0]
    return render(request, 'calc.html', {'digit': z, 'even': evens})

def prim(request):
    def is_prime(num):
        if num <= 1:
            return False
        for n in range(2, int(num ** 0.5) + 1):
            if num % n == 0:
                return False
        return True

    val = request.POST.get('dig', '')
    x = map(int, val.split())
    z = list(x)
    primes = [i for i in z if is_prime(i)]
    return render(request, 'calc.html', {'digit': z, 'prime': primes})
