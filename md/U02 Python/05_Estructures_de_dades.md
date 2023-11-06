En aquesta unitat anem a treballar les estructures bàsiques d'emmagatzematgee de dades que ens ofereix Python. Serà inevitable fer una comparació amb els vectors i ArrayList d'altres llenguatges com Java.

## 5.1 Llistes (`list`)

Les llistes són una estructura que conté una sèrie d'elements ordenats, delimitades per claudàtors (`[]`) i separades per comes (`,`).

???+ warning "Atenció"
    El fet que estigui **ordenat** implica que hi ha un primer element, un segon, etc. i que podem accedir als elements per la seua posició. No vol dir que el tingui un **contingut ordenat**

Aquest elements poden ser del mateix tipus o tindre tipus heterogenis, com òdem veure a continuació:

???+ Example "Possibles llistes"
    ```python
    # llista de cadenes
    noms=["Pere","Joan","Anna"]

    # llista de valors
    notes=[7.4,3.7,8.0]

    # llista de `coses``
    dades=["Pere",True,4.7,None]
    ```

Encara que hi ha diverses maneres de afegir i eliminar, comentem les més legibles i habituals:

- `llista.append(element)` --> afig l'element al final de la llista.
- `llista.insert(index,element)` --> afig l'element en la posició determinada per índex. Si l'índex està fora de rang, ho posa al final.
- `llista.remove(element)` --> elimina l'element de la llista. Si nó existeix botarà l'error `ValueError`

Per a consultar i/o modificar elements concrets farem servir la notació dels claudàtors com si foren vectors de C o Java:

- `print(llista[3])`
- `llista[3]="Pep"`

Per a recòrrer les llistes de manera seqüencial, podem recorrer a distints tipus de bucles for:

???+ example "Recorregut sense índex"
    En aquest exemple, una variable prendrà el valor de cada element de la llista:
    ```python
    for element in llista:
        print(element)
    ```

???+ example "Recorregut amb índex"
    En aquest exemple, una variable prendrà els valor dels distints índex de la llista. Farem servir la funcio `range(n)` que torna un valor entre `0` i l'anterior a `n` i la funció `len(llista)` que ens retorna el tamany de la llista:
    ```python
    for i in range(len(llista)):
        print(noms[i])
    ```

Per últim, podem utilitzar l'operador `in` per a saber si un element està o no a una llista, per exemple per a poder esborrarlo sense problemes

```python
if element in llista:
    pass
```

### 5.1.1 Slicing (rebanar)

El slicing és una manera de treballar, una mica complexa, que ens serveix per a _rebanar_ o extreure una porció de la llista. Fa servir la notació dels dos punts `inici:fi[:bot]`. 
Aquesta notació representa començar a l'inici fins a l'anterior al fi, visitnt els elements segons el bot indicat (si bot no apareix, val 1).

> Quan els valors d'inici o fi son negatius, comencen a contar-se desde la dreta cap l'esquerre, però és poc natural, i es recomana sols en circumstànices concretes

Anem a veure-ho mitjançant exemples. A la plataforma tens un arxiu `nba.txt` amb el llistat d'equips de la nba. Amb el següent codi:

```python
nba=[]    # llista buida
data=open('nba.txt','r').read() # llegim les dades
nba=data.split('\n')    #trocejem pel bot de linia i ja tenim la llista
print(nba)
print(len(nba))

print(nba[2:5]) # mostra de la casella 2 a la 4 (última-1)
print(nba[2:])  # mostra de la casella 2 al final
print(nba[:5])  # mostra fins la casella 4 (última -1)
print(nba[-1:]) # mostra l'últim
print(nba[-3:]) # mostra els 3 últims
print(nba[-5:-3]) # Mostra des de el 5t per la dreta al tercer per la dreta
```

### 5.1.2 Altres mètodes

- `del llista[index]` → Per eliminar una element de la llista, sense saber el seu valor 
- `llista.pop()` → Per eliminar i retornar l'últim element de la llista
- `llista.count(element)`  → retorna el numero d'ocurrències de l'element a la llista
- `llista.sort()` → ordena ascendentment els elements de la llista. Si volem descendent posarem `[reverse=True]`.

## 5.2 Tuples (`tuple`)

Les tuples son estructures semblants a les llistes, però amb la gran salvetat que son inmutables, és a dir, no poden modificar-se.

Això les fa molt més eficients en quant a consum de recursos, però clar, hem d'estar segurs que les dades no necessitarem que canvien. Altres diferències:

- S'inicien amb `()` en compte de `[]`
- No podem modificar amb tupla[index]=elemet
- No disposen dels operadors `append`, `remove` i qualssevol altre que les modifiquen

## 5.3 Diccionaris (`dict`)

Un diccionari és una colecció d'elements etiquetats, amb la manera `etiqueta:valor`. Ve a ser el que coneixem amb un objecte `JSON`. Això ens permetrà, entre altres coses l'accedir a un element, no sols pel seu índex, sinó per la seua etiqueta:

```python
edats = {"Anna": 35, "Jaume": 18, "Pere": 17}

print(edats["Pere"]) # Retorna 18
```

Els diccionaris poden contenir qualssevol tipus de dades al seu valor. Vegem algunes funcions útils autoexplicades:

```python
telefons={'Pere':123456,'Ana':7483943,'Joan':None}

print(telefons['Ana'])      

#print(telefons['Pau'])  #Excepció `KeyError``

print(telefons.get('Pau'))  # Com no esta torna None, però no dona error

del(telefons['Ana'])      #Elimina la entrada del diccionari
print(telefons)

noms = ['Xavi', 'Elisa', 'Maria']
telefons = dict.fromkeys(noms, None)  # Aquestes son les claus, sense valors
print(telefons)
#{'Xavi': None, 'Elisa': None, 'Maria': None}

print('Xavi' in telefons)

# Crear a partir de un json
import json
jsonstring = '{ "nom": "erik", "edat": 38, "casat": true}'
persona=json.loads(jsonstring)
print(persona)

# recuperar les claus i els valors per separat
print(persona.keys())
print(persona.values())

# recuperar els elements
for clau,valor in persona.items():
    print(clau,"-",valor)

# nom - erik
# edat - 38
# casat - True
```



