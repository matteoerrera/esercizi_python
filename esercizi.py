print('prima istruzione')

a = "A";
print(a=="A" or a =="E" or a=="I" or a=="O" or a=="U")

print('e\' il mio primo programma')
print('troppo semplice')

n1 = 5.834;
print(type(n1));
n2 = int(n1);
print(type(n2));
print(n2);

# operatori logici not and or
# print(True and False);
# print(True or False);
# A or B or C
# Si parte da sinistra a destra (A or B) or C

# Le precedenze sono not, and, or

# print('a' <> 'b'); # Deprecato in Python 3?
#print('a' != 'b');

# (temp > 18.0 and tempo < 22.0)
# (s == 'a' or s == 'b')

# (s == 'OK' or s == 'OK' or s == 'Okay' or s == 'O.K.')
# l'elaboratore si ferma alla prima condizione s == 'OK' qualora questa venisse soddisfatta

# print(!True) NON FUNZIONA alternativa (not True)

s = 'foo'
print (s in 'That\s food for thought') # Ritorna True se la variabile s appare nella stringa
# L'operatore [n] ritorna la n posizione di una stringa s=foo; s[2]; "o"
print(s[1])


# La funziona len() restituisce un intero che corrisponde alla lunghezza della stringa in input
# L'indice di s è nell'intervallo [0, len(s)-1]


# Possiamo usare [i:j] per prendere la sottostringa che parte dall'indice i e arriva fino all'indice j
s = 'foobar'
print(s[2:5]) # Output "oba"

# Esistono le funzioni upper() e lower() di String

# La funzione s.count("oo") conta quante volte la stringa "oo" è contenuta nella variabile
# La funzione s.find("oB") ritorna l'indice in cui è contanuta la stringa
# La funzione s.replace('oo', 'ii')

# print('stampo il numero' + 5) non si può fare perché + non è definito tra stringhe e interi

# In alternativa si può fare
print('stampo il numero ' + str(5))

# Si possono convertire delle stringhe in numeri con le funzioni int() e float()
print(float("1.1e+10"))


# Oer le costanti si usano label maiuscole

SECONDS_IN_A_DAY = 86400


"""
si può commentare su più
righe utilizzando questa
notazione
"""

"""
Esercizio:

Sia anno una variabile intera che rappresenta un anno
Scrivere una espressione booleana in cui compare la variabile anno che è vera se e solo se anno è bisestile

- Normalmente anno è bisestile se è divisibile per 4, cioè la divisione da resto 0
- Ma se è anche divisibile per 100 allora non è bisestile, come nel caso dell'anno 1900
- Nonostante le condizioni precedenti, se anno è divisibile per 400 allora è bisestile, come nel caso dell'anno 2000

Su wikipedia troviamo le regole con vari esempi.

Per venerdì

"""
year = 1936
print((year%4==0 and not year%100==0) or year%400==0)

"""
Le Funzioni
"""

import math

print(math.sqrt(4))

stampa_aiuto(10)

def stampa_aiuto(n):
    print('Questo programma serve a imparare Python')
    print('Lancialo '+ str(n) + ' volte se ci credi')
    
print(2**2)

if(True):
  print("ciao")
elif(False): # si usa elif invece di else if
  print("we")
  

# Esercizio per casa
# Verifica che un anno sia bisestile con if
# Soluzione equazione ax^2 + bx +c = 0


# Implementare un programma per calcolare il maggiore tra tre numeri interi a, b, c

a = int(input("numero A "))
b = int(input("numero B "))
c = int(input("numero C "))


if(a>b and a>c):
  maggiore = "A"
elif(b>a and b>c):
  maggiore = "B"
else:
  maggiore = "C"
  
print(maggiore)

""" 

Problema del triangolo
dato a, b, c, capire il tipo di triangolo

"""

a = int(input("lato A "))
b = int(input("lato B "))
c = int(input("lato C "))

if(a == b):
  if(a == c):
    print("È un triangolo equilatero")
  else:
    print("È un triangolo isoscele")
else:
  print("È un triangolo scaleno")

a = int(input("lato A "))
b = int(input("lato B "))
c = int(input("lato C "))

uguali = 0

if(a==b):
  uguali = uguali+1
if(a==c):
  uguali = uguali+1
if(b==c):
  uguali = uguali+1

if(uguali==0):
  print('scaleno')
elif(uguali==1):
  print('isoscele')
elif(uguali==3):
  print('equilatero')

# Soluzione equazione ax^2 + bx +c = 0
import math
def calcEq(a,b,c):
  delta = (b**2)-4*(a*c)
  if(delta > 0):
    x1 = (-b+math.sqrt(delta))/2*a
    x2 = (-b-math.sqrt(delta))/2*a
    print("X1 :" + (str)(x1))
    print("X2 :" + (str)(x2))
  else:
    print("Non esistono soluzioni")
a = int(input("A"))
b = int(input("B"))
c = int(input("C"))

calcEq(a,b,c)

# Istruzioni ripetitive
maxN = int(input("Inserisci numero massimo "))
n = 1
tot = 0
while(n < maxN):
  tot = tot+n
  n=n+1
print(tot)

lastN = 0
n = 1
while(n != 0):
  n = int(input("Inserisci un numero: "))
  print(n+lastN)
  lastN = n+lastN

# Divisione con resto
a = int(input("Inserisci primo numero A "))
b = int(input("Inserisci secondo numero B"))

if(a > 0 and b > 0):
  x = a;
  count = 0

  while(x >= b):
    x = x-b
    count = count +1

  print("RESTO: "+ str(x))
  print("QUOZIENTE: "+ str(count))
else:
  print("Divisione per 0 non permessa")

"""
Liste

insieme ordinato
le stringhe sono immutabili, l'interprete crea sempre nuove stringhe.

len(x) restituisce la lunghezza di una lista

"""
primi = [2,3,5,6,11,13,17,19]
b = 3 in primi # si usa in per controllare se un elemento è contenuto in un array
print(b)

# È possibile stampare degli elementi consecutivi
print(primi[2:5])

"""
È possibile creare una lista dei caratteri estratti da una string
"""

s = "CIAO!"
l = list(s)
print(l)

"""
Funzioni utili
append(element)
extend(l2) aggiunge tutti gli elementi di l2 in coda
insert(i,e) aggionge e nell'indice i
pop() elimina e restituisce ultimo elemento
pop(i) elimina l'elemento di indice i
index(x) restituisce l'indice di x nella lista, blocca l'esecuzione se non è nella lista

Per passare da una lista a una stringa si usa join()

As esempio:
"""
l1 = ['H','E','L','L','O']
print(''.join(l1))

"""
La funzione di help range() accetta due parametri e restituisce una lista di tutti gli interi
range(1,10) -> [1,2,3,4,5,6,7,8,9]
da 1 (incluso) a 9 (escluso)
"""

# Contatore
tot = 0
for n in range(1,6):
  tot = tot+(n*n)
print(tot)

# Fattoriale
def fattoriale(max):
  tot = 1
  for n in range(1, max):
    tot = tot+tot*n
  
  return tot

print(fattoriale(5))

# Somma dei numeri dispari
tot = 0
for n in range(1, int(input("INSERISCI UN NUMERO: "))*2):
  if(n%2 !=0 ):
    tot = tot+n
print("La somma dei numeri dispari è "+ str(tot))

# Stampa una piramide
def stampaPiramide():

  h = int(input("Inserisci altezza: "))
  simbolo = input("Inserisci un simbolo: ")
  simboloSfondo = input("Inserisci un simbolo per lo sfondo: ")

  if(len(simbolo)!=1 or len(simboloSfondo) != 1): 
    print("Il simbolo deve essere di lunghezza 1")
    return

  for i in range(0, h):
    for j in range(i, h):
      print(simboloSfondo, end="")

    for j in range(0, i*2+1):
        print(simbolo, end="")

    for j in range(i, h):
      print(simboloSfondo, end="")

    print("")
  




stampaPiramide()

# Stampa una piramide
 h = int(input("Inserisci altezza: "))

for i in range(0, h):
  for j in range(i, h):
    print(" ", end="")

  for j in range(0, i*2+1):
      print("*", end="")

  print("")

tot = 0
for i in range(0, 10):
  n = int(input("Inserisci un numero intero: "))
  tot = tot+n
print("Il totale è " + str(tot))

output = False
lastN = 0
x = 1
while x != 0:
  x = int(input("Inserisci un numero intero "))
  if x > 0 and lastN > 0:
    output = True
  lastN = x
print(output)

# Stampare il tempo attuale
import time
print(time.time())

# Verifica universale
trovato = False;
n = int(input("Su quanti numeri vuoi eseguire la ricerca? "))
numeri = []
for n in(range(0,n)):
  numeri.append(int(input("Inserisci un numero ")))

i = 0
while(not trovato and i < len(numeri)):
  if numeri[i] <= 0:
    trovato = True
  i+=1

if(trovato):
  print("Non tutti gli interi sono positivi")
else:
  print("Tutti gli interi sono positivi")

# Verifica esistenziale, controllare se esiste almeno un negativo

n = int(input("Su quanti numeri vuoi eseguire la ricerca?"))
negativi = 0
for n in range(0, n):
  if(int(input("Inserisci un numero "))<=0):
    negativi+=1
     
if(negativi > 0):
  print("Esiste almeno un negativo")
else:
  print("Sono tutti positivi")

"""
Dizionari (array associativi)
"""

eng2it = dict() #creo dizionario vuoto
#oppure
eng2it = {}
print(eng2it)

eng2it['one'] = 'uno'
eng2it['due'] = 'dos'
eng2it['due'] = 'tre'

print(eng2it)
# {'chiave' : 'valore'}

# Un dizionario si può creare anche con
eng2it = {'one':'uno', 'two':'due', 'three': 'tre'}

# È possibile leggere una chiave in questo modo
print(eng2it['two']) # 'due'
# Per ottenere il numero di relazioni
n = len(eng2it) # n è pari a 3

# Si può cancellare una relazione con
eng2it.pop('two')
eng2it.clear() #cancella tutti gli elementi

# Controllare se esiste un elemento
'one' in eng2it # Output: True

# Cancellare una chiave che non esiste è un errore, controllare prima che essa esista con un IF
# Ottengo tutte le chiavi con eng2it.keys() e mi ritorna un array
# Ottengo tutti i valori con eng2it.values() e mi ritoìrna un array

# Si può iterare su un dictionary in questo modo

for key in eng2it: # <= implicitamente itera sulle chiavi
  print('{}:{}'.format(key, eng2it[key]))

# Oppure
for val in eng2it.values():
  print(val)


"""
Formattare stringhe
"""

persone = 3
conto = 5.578
data = 'Lunedi'
# .2f indica di stampare al massimo 2 cifre dopo la virgola
print('Persone = {:d}, Conto = {:.2f}'.format(persone, conto))
# Output: Persone = 3, Conto = 5.58

print('Data = {:d}'.format(data))
# Output: Data = Lunedi



"""
ATTENZIONE
Se stampo il tipo del dizionario, il tipo non è una lista ma è un tipo particolare
Per utilizzarle come liste, va tramutato in lista in questo modo
"""

l = list(eng2it.values())
print(l[0])

"""
Ma è comunque possibile iterarci sopra
"""

# Conto quante lettere in una parola senza usare count() e inserendo le lettere in un dizionario

def count_az2(word):
  output = {}
  for l in word:
    if(l in output):
      output[l] = int(output[l])+1
    else:
      output[l] = 1
    return output

print(count_az2("SOQQUADRO"))

alph = {"A": "å", "B":"∫", "C":"©", "D":"∂", "E":"€","F":"ƒ", "G":"∆", "H":"∆","I":"œ", "L":"¬", "M":"µ", "N":"˜","O":"ø","P":"π","Q":"„", "R":"®", "S":"ß", "T":"™", "U": "¨", "V": "√", "Z": "∑"}

# Codificare e decodificare una parola utilizzando un dizionario

def codifica(parola):
  output = []
  for l in parola.upper():
    output.append(alph[l])
  return ("".join(output))

def decodifica(parola):
  output = []
  conv_alph = {}
  for key in alph:
    conv_alph[alph[key]] = key
  for l in parola:
    output.append(conv_alph[l])
  return ("".join(output))


print(codifica("PROVA"))
print(decodifica("π®ø√å"))
