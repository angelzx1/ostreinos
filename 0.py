def f(nome):
    return "oi, "+ nome + "!"

print (f("Nico"))

def soma (a,b):
    return a+b

print(soma(10,30))

def saudacao(nome,cumprim="oi ",pontuacao="!!"):
    return cumprim + nome + pontuacao
print(saudacao("NiNiNi", cumprim=" Muito bom ", pontuacao="..."))

def f(x):
    def g(y): 
        return x*y
    return g(2)

print (f(5))

def fahr(x):
    return 5 * (x-32) / 9
print("{0:.2}".format(fahr ((40))))