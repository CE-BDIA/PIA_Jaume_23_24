## 3.1. Sentències

Les **sentències** són cadascuna de les ordres que es donen a un programa. Si recordem un _algorisme_ és una seqüencia de passos, doncs be, una sentència especificarà un (o diversos) d'aquests passos per transcriure un algorisme a un programa.

Les sentències poden ser de distint tipus, ateses a la seua naturalesa:

- **Importació**. Són les sentències (habitualment a l'inici del programa) que indiquen quines llibreries del programa van a fer-se servir. Com ja hem vist, les llibreries són un conjunt de funcions que ja estan a punt per a fer-se servir.

```
import java.io      // importació de llibreria en Java
import time         // importació de llibreria en Python
#include<stdio.h>   // importació de llibreria en C
```

- **Declaratives**. Són les sentències que es fan servir per a indicar alguna cosa. No representen cap acció dins d'un programa. Per exemple destaquen la declaració de variables o les de funcions:

```
int n;                      // en Java es declaren les variables
def area(base, altura):     // declaració de funció en Python
public float area(float base, float altura)  //declaració de funció en Java
```

- __Assignacions__ o __Instruccions sequencials__. Són les instruccions propiament dites. Serveixen per a fer un càlcul i assignar-lo a una variable. El càlcul es pot fer amb qualsevol dels operadors estudiats, i habitualment guardar el valor calculat en una variable. També poden simplement fer una acció sense guardar-la en cap lloc, com puga ser mostrar alguna cosa per pantalla (`print`), emetre un so o esborrar un fitxer.
- **Sentències de control**. És el que estudiarem en aquest tema. Són aquelles instruccions que ens permeten moure el fluxe _continuo_ o de dalt cap avall d'un programa, permetent-nos prendre desicions i repetir una sèrie d'intruccions les vegades que calga. Es tracta de les **bifurcacions** i dels **bucles**

## 3.2. Sentències alternatives

### 3.2.1. Condicions simples

Com ja em comentat, l'ordre en el fluxe del programa és de dalt cap avall i d'una en una. 

```
...
sentència 1
sentència 2
sentència 3
...
sentència n
```

Si volem alternar entre un o altre camí deurem de fer alguna mená de pregunta o condició, de manera que si passa una condició farem una cosa i cas que no pase farem altra. La sintaxi en `Python` és:

???+ Example "Bifurcacions simples en `Python`"

    ```Python
    if condicio1:
        sentencia 1
        sentencia 2
        #...
    elif condicio2:
        sentencia a
        sentencia b
        #...
    else:
        sentencia n
        sentencia m
        #...
    ```

On:

- `condicio1` i `condicio2` son expressions relacionals, que ens donen com a resultat `True` o `False`. Si s'acompleix la `condicio1` s'executa les sentencies indentades desprès dels `:` (sentencies 1,2,...). Molt important el tabular be aquelles sentències dins de cada `if`
- Si la `condicio1` ha donat com ha resultat `False` llavors s'avalua la `condicio2`, dins del `elif`. `elif` ve a ser la contracció de `else - if`. Si la `condició2` és `True` llavors s'executa el bloc indentat (sentencies a, b ,...). Poden apareixer molts o cap bloc `elif`, per la qual cosa és opcional.
- Sinó s'ha acomplit cap condicio (ni `if` ni `elif`) finalment s'executarà el bloc `else`, com alternativa a niguna de les anteriors. Aquest bloc també és opcional.
  
L'equivalent en `Java` és el següent:

???+ Example "Bifurcacions simples en `Java`"
    ```java
    if (condicio1){         // condició entre parèntesi
        sentencia 1;        // els blocs venen marcat per les claus
        sentencia 2;        // no per la indentació
        //...
    }
    else if (condicio2){       // no es contrau else-if per elif
        sentencia a;
        sentencia b;
        //...
        }
    else{
        sentencia n;
        sentencia m;
        //...
    }
    ```

???+ Success "**Exercici resolt** Demanar un numero a l'usuari i indicar si el número és positiu."
    ```python
    n=int(input("Dona'm un numero: "))
    if n>=0:
        print("El numero",n,"es positiu")

    print("Fi del programa")
    ```

???+ Success "**Exercici resolt** Demanar un numero a l'usuari i indicar si el número és positiu o negatiu."
    ```python
    n=int(input("Dona'm un numero: "))
    if n>=0:
        print("El numero",n,"es positiu")
    else:
        print("El numero",n,"es negatiu")

    print("Fi del programa")
    ```

???+ Success "**Exercici resolt** Indicar la situació administrativa d'una persona (estudiant, treballador o jubilat) depenent de la seua edat."
    ```python
    edat=int(input("Dona'm l'edat de la persona: "))
    if edat<16:
        print("Eres estudiant")
    elif edat<65:
        print("Eres treballador")
    else:
        print("Eres jubilat")

    print("Fi del programa")
    ```

### 3.2.2. Condicions compostes

Com s'ha anomentat, desprès del `if` o del `elif` ha d'aparèixer una condició, la qual ha d'avaluar-se a `True` o `False`. La condició pot ser simple, però també la podem fer composta i més complexa mitjançant els operadors `and`, `or` i `not`, seguint les taules de la veritat que vegerem als temes anteriors.

???+ Success "**Exercici resolt** Demanar un numero a l'usuari i indicar si parell i està entre 10 i 20 (incloses)"
    ```python
    n=int(input("Dona'm un numero: "))
    if n%2==0 and (n>=10 and n<=20):
        print("Si que es parell entre 10 i 20")
    else:
        print("No compleix la condició")

    print("Fi del programa")
    ```

### 3.2.3. Condicions niuades

Si tenim diverses condicions que complir, com hem vist abans les podem composar amb els operadors lògics. El tema és que, sinó es compleix la condició no sabrem si és per la primera condició o per la segona (mirar l'exemple anterior). Llavors en aquests cassos el que podem fer és posar condicions simples niuades (una dins de l'altra).

???+ Example "Programa alternatiu a la solució anterior:"
    ```python
    n=int(input("Dona'm un numero: "))
    if n%2==0:
        if n>=10 and n<=20:
            print("Si que es parell entre 10 i 20")
        elif:
            print("El número ès parell però no està entre 10 i 20")
    else:
        print("El número és imparell")

    print("Fi del programa")
    ```

## 3.3. Bucles

De vegades a un programa ens interessarà pel motiu que siga repetir un conjunt d'instruccions. El nombre de repeticions pot saber-se a priori o no. Cas de saber-ho, direm que estem en bucles incondicional, i cas de no saber-ho en bucles condicionals, ja que la repetició es farà fins que s'acomplisca una condició.

### 3.3.1. Bucles condicionals. `while`

Imaginem la següent situació. A un programa volem calcular l'àrea i el cercle d'una circumferència, per la qual cosa hem de demanar el radi de la mateixa. 

???+ Example "**Primera solució**"
    ```python
    import math

    radi=int(input("Dona'm el radi de la circumferencia: "))

    area=math.pi*radi**2
    print("L'area de la cirumferència és %6.3f"%area)

    print("Fi del programa")
    ```

Aquest programa semble correcte a priori, perà que passa si a l'executar li donem al radi un valor de `-4`, per exemple:

```
L'area de la cirumferència és 50.265
El cercle de cirumferència és -25.133
```

Quin rang de valors és acceptable per al radi? La resposta és _nombres majors que zero_. Anem a intentar solucionar-ho amb el que sabem. 

???+ Example "**Segona solució**:"
    ```python
    import math

    radi=int(input("Dona'm el radi de la circumferencia: "))

    if radi>0:
        area=math.pi*radi**2
        cercle=2*math.pi*radi
        print("L'area de la cirumferència és %6.3f"%area)
        print("El cercle de cirumferència és %6.3f"%cercle)
    else:
        print("No podem fer càlculs amb radis negatius o zero")

    print("Fi del programa")
    ```

Com vegem ara sols fem el càlcul quan el radi és positiu. El problema és que quan és negatiu el programa acaba. Llavors el que podem fer quan l'usuari pose un radi negatiu és tornar-lo a demanar. Què pot passar? que el tornen a posar negatiu 😞... 

La gran pregunta és **quants cops caldrà demanar el radi fins assegurar-nos que el radi siga positiu?**. Resposta: **No ho sabem**. Llavors haurem de demanar el radi fins tenir un valor positiu, 

???+ Example "**Tercera solució**"
    ```python
    import math

    radi=0              # Li assignem al radi un valor dels considerats com a incorrectes
    while radi<=0:      # mentre la variable radi tingui un valor incorrecte → repetim     
        radi=int(input("Dona'm el radi de la circumferencia: "))
        if (radi<=0):   # Informem a l'usuari que ha posata valor incorrecte
            print("No podem fer càlculs amb radis negatius o zero")

    #   si hem aconseguit eixir del bucle, és per que la condició és falsa
    #   per tant el radi>0. Ja podem fer els càlculs

    area=math.pi*radi**2
    cercle=2*math.pi*radi
    print("L'area de la cirumferència és %6.3f"%area)
    print("El cercle de cirumferència és %6.3f"%cercle)

    print("Fi del programa")
    ```

Vist aquest exemple, les conclussions són:

- Farem servir un bucle condicional o `while` quan el número de repeticions no depenguen del programador ni del problema, sinó de l'usuari o de les condicions d'execució, que cada cop son distintes.
- Abans d'escriure la condició haurem d'inicialitzar la varible(s) que apareixen a la condició. En aquesta inicialització la condició ha de ser `True`, de manera que puguem entrar al bucle. 
- Dins del bucle haurem de modificar d'alguna manera eixa variable, de manera que en algun moment la condició sigui `False`, per poder eixir del bucle.
- Mai sabrem a priori quantes vegades s'executarà

???+ Example "Sintaxi de bucle `while`en `Python`:"
    ```python
    while condició:
    accio1
    accio2
    ...
    accion

    acció_fora_del_bucle  
    ```

S'avalua la condició, ocòrre que:

  - La condició és `True` → entrem al bucle, s'executen totes les accions, des de la `1` fins la `n`. En acabar es torna a avaluar la condició.
  - La condició és `False` → s'acaba el bucle, i llavors s'executa `acció_fora_del_bucle`.

#### Convergencia

Com s'ha comentat abans, l'execució del bucle acaba quan la condició és `False`. Observa els següents exemples i intenta pensar que passa quan s'executen:

```python
n=0
while n<100:
    print(n)
```
La sortida del programa anterior mostra `0` per sempre:

```
0
0
...
0
```

Això ocorre perquè no hem escrit cap ordre que modifica la `n` (no hem modificat la condició). Això ens provoca un **bucle infinit**. Modifiquem-ho:

```python
n=0
while n<100:
    print(n)
    n=n-1
```

Ja hem modificat la `n`, i per tant la condició, però la sortida ara és:

```
0
-1
-2
...
-9999999999
```

En aquest cas la condició és que `n<100`, sent `n=0`. Nosaltres (per error 🙃) modifiquem la `n` restant-li un en cada iteració. Llavors és impossible que mai arribe a ser igual o superior a `100`. Tornem a estar en bucle infinit. Solucionem-ho

```python
n=0
while n<100:
    print(n)
    n=n+1
```

Finalment s'imprimeix:

```
0
1
2
...
99
```

El que tenim que observar és que la variable que controla la condició (`n`) ha de convergir al valor final (`100`). Observar també que el numero 100 no s'imprimeix, ja que quan `n==100` la condició és `False`, i ja s'ix del bucle.

### 3.3.2. Bucle incondicional. Bucle `for`

Aquest tipus de bucles es fa servir quan sabem a priori el numero de vegades que volem repetir les instruccions que formen part del bucle. En aquest tipus de bucles hi ha una variable índex que ens permet portar un compte del nombre de repeticions que portem. En `Python` aquest bucle ha canviat bastant respecte a altre llenguatges com `Java`, llavor anem a explicar-ho en els dos llenguatges.

### 3.3.3. `for` en `Java`

En `Java` el `for` te 3 apartats. Es fa servir una variable que s'inicia a un valor inicial. Desprès es posa una condició, com si fos un `while` i finalment es posa un increment que es farà cada cop que s'executen les accions. El bucle anirà repetint-se fins que la condició siqui `false`

```java
for (int i=0;i<10;i++){
    printf(i);
}
```

aquest bucle imprimeix del 0 al 9 (recorda que el 10 ja no forma part, ja que no acompleix la condició)

```java
for (int i=0;i<10;i=i+2){
    printf(i);
}
```

aquest bucle imprimeix del 0,2,4,6 i 8. L'increment en aquest cas es fa de 2 en 2

```java
for (int i=30;i>=0;i=i-5){
    printf(i);
}
```
aquest bucle mostrarà 30,25,20,15,10,5,0. Comença de 30 i va baixant de 5 en 5 fins a 0 (inclòs)

En `Python` existeix també una variable que controla el bucle. La diferència és que hem d'indicar la seqüencia de valors que volem que prenga dita variable en forma de llistat o _tupla_. Parlarem de les tuples o llistats més endavant. Tot això s'aconsegueix amb la funció `range()`, que és molt completa i admet molts argument, per la qual cosa anem a fer un miniapartat per a explicar-la.

#### `range()`

La seua sintaxi és `range([start,] stop[, step])`:

- `start` → indica des de quin número comença la seqüencia. Si no s'indica s'escomença desde `0`.
- `stop` → indica fins a quin límit arribarem. La seqüencia acaba en **l'anterior a** `stop`.
- `step` → indica de quant en quan es modifica la seqüencia. Si no es posa res va de 1 en 1 de manera ascendent. Aquest atribut no pot ser zero

!!! Example
    ```python
    >>> range(10)                       # 10 números
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]      # Del 0 al 9
    >>> range(0,5)                      # 5 numeros
    [0, 1, 2, 3, 4]                     # Del 0 al 4
    >>> range(0,10,2)           
    [0, 2, 4, 6, 8]
    >>> range(10,0,2)         # Està mal, no puc anar del 10 al 0
    []                        # anant de 2 en 2      
    >>> range(10,0,-2)              # Ara sí
    [10, 8, 6, 4, 2]
    >>> range(0,51,10)
    [0, 10, 20, 30, 40, 50]

    # Si volem del 1 al 100
    >>>range(1,101)

    >>> range(1,10,0)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ValueError: range() step argument must not be zero
    ```

### 3.3.4. `for` en `Python`

Vista la funció `range()` podem veure el bucle for en `Python`:

```python
for variable in llista:
  accio1
  accio2
  ...
```

Es repeteix el bucle executant-se les accions on la varaible pren com a valor cada element de la llista. Si volem que la llista sigui una serie de números, ho substituirem per la funció `range()` vista anteriorment. Vegem els següents exemples, comparant-ho amb `Java`.

???+ Success "**Exercici resolt** Imprimir un llistat del 1 al 10:"
    ```python
    for i un range(1,11):
        print(i)
    ```


???+ Success "**Exercici resolt** Imprimir la taula de multiplicar de 3"
    ```python
    for i un range(1,11):
        print("3*",i,"=",3*i)
    ```
   
???+ Success "**Exercici resolt** Imprimir els numeros parells des del 40 fins al 0 (no inclòs)"
    ```python
    for i un range(40,0,-2):
        print(i)
    ```

Veurem més avantages del `for` quan estudiem els vectors o tuples.

### 3.3.5. Bucles infinits

Com hem vist abans, moltes vegades per error podem escriure bucles infinits, cosa que pot portar el sistema informàtic a inestabilitats. Però, moltes vegades ens interessarà programa un bucle infinit i, de fet, és fan servir moltíssim. Pensem per exemple en un caixer automàtic. El programa està en una espera infinita a que algun usuari vaja a executar algun procediment. Quan un usuari va i posa la targeta el programa propiment dit l'aten. Quan l'usuari acaba d'operar, el caixer es torna a posar en dita espera infinita. Vejam l'algorsime:

```
// ALGORISME CAIXER

// Algú encen el caixer automàtic
per sempre:
    esperar_introduccio_targeta()
    intent_pin=1
    seguir=false
    mentre (intents_pin<=3)
        PIN==llegir("Posa el PIN de la targeta")
        si  (PIN_OK(PIN))   // comprovar el PIN
            seguir=true
        sino
            intents_pin=intents_pin+1
        fi_si
    fi_mentre
    si (not seguir)  // pin incorrecte
        tragar targeta
        mostrar missatge
    sino
        operacio=llegir("Que vols fer")
        si (operacio==1)
            // consultar saldo
        sino si (operacio==2)
            // treure diners
        ...
        ...
    fi_si
fi_per_sempre 

// algú apaga el caixer automàtic
```

Com aconseguim programar un `per_sempre` que hem indicat. La resposta es senzilla però no evident. Posar una condició que sempre siga certa i que sigui inmutable (que no es modifique)

```python
while True:
    accio1
    accio2
    ...
```

D'aquesta manera entrem al bucle i passe el que passe dins de les accions, el `True` com és una constant no serà mai modificat, i llavors no eixirem del bucle.

NOTA: No te sentit fer en algun lloc `while False:`, ja que en eixe bucle no s'entra mai (millor no escriure res).

#### Ruptura de bucles. `break`, `continue` i `else` als bucles

Tot això dels bucles infinits està molt be, però com podem eixir d'un bucle infinit? La resposta ens la dona la sentència `break`, que ens permet eixir d'un bucle (independentment de la condició, siga infinit o no):

- `break` interromp l’execució del bucle i seguim per la instrucció seguent fora del bucle.
- `continue` fa que el programa comence altra iteració, encara que no s’haja acabat l’actual. Per tant les línies que hi han dins d’un bucle per davall del continue no s’executen. Cas d’estar dins d’un `for`, anirem a l’increment de la variable comptadora o al següent element de la llista.
- `else` s'afig un bloc adicional a un bucle `while` que s'executarà quan hem eixit del bucle debut a la falsetat de la condició del mateix, i no quan hem eixit per un `break`. No és gaire intuitiu. 

!!! Example **Exemple**
    ```python
    for i in range(20):         # Això recorre del 0 al 19
        print(i)
        if i<10:
            continue
        if i%2==0:
            print("Es parell")
        if i>=15:
            break

    print("Final del bucle")
    ```

Aquest programa sols te sentit acadèmic, per entendre que farà cada cosa:

- Imprimim el numero.
- Si els numeros son inferiors a 10 passem al següent nuúmeo (`continue`). Fixa't que ens botem tot el que queda dins del bucle
- Si es parell ho mostrem
- En arribar al 15 acabem el bucle (`break`), de manera que del 16 al 19 ja no es fa res més.

```
0
1
2
3
4
5
6
7
8
9
10
Es parell
11
12
Es parell
13
14
Es parell
15
Final del bucle
```

!!! notes NOTES: 

  - Les sentències `break` i `continue` **sempre** es posaran dins d'un `if`, ja que sinó s'executaran sempre dins del cos del bucle.
  - El `break` permet eixir del bucle més niuat que hi ha. Si per exemple estem dins de un bucle niuat i volem acabar en tots els bucles, necessitarem dos `break` (un per cada bucle)

### 3.3.6. Bucle de demanar dades

Una de les parts més importants a l'hora de programar és demanar dades a l'usuari, i penseu que l'usuari serà una gran font d'errors del nostre programa. Penseu que dins del sistema informàtic, qui més errors provoca és l'usuari, ja que fa clic on no toca, posa lletres quan correspon números i mai llig la documentació ni els misstges d'error dels programes. És per això que deguem de ser molt cautelosos a l'hora de validar la informació que ens dona. Par a practicar-ho anem a fer un exemple complet i ens servirà també per a introduir el concepte d'excepcions.

**Exercici resolt** Volem fer un programa que demana un número i calcula el doble del mateix. Volem forçar que el número sigui **positiu**. En acabar preguntarà a l'usuari si vol eixir o no, tinguent com a possibles respostes `s`o `n`. Cas de no voler sortir repetirem el mateix procés.

???+ Success "**Solució 1** Fem el programa que demana un número i calcula el doble del mateix"
    ```python
    n=int(input("Dona'm un numero: "))
    print("El numero es",n,"i el seu doble",2*n)
    ```

Mirem que passa a l'executar:

```
Dona'm un numero: 4
El numero es 4 i el seu doble 8
Dona'm un numero: -5
El numero es -5 i el seu doble -10
Dona'm un numero: Hola
Traceback (most recent call last):
  File "proves.py", line 1, in <module>
    n=int(input("Dona'm un numero: "))
ValueError: invalid literal for int() with base 10: 'Hola'
```

Ocórre que:

- si podem tenir números negatius, 
- el programa demana un número, fa l'operació i acaba.

???+ Success "**Millora 1** Preguntem a l'usuari si vol acabar" 

    Per a fer aquesta millora anem a fer un bucle infinit, on posarem al cos del bucle el que hem programat anteriorment, afegint la pregunta a l'usuari si vol acabar o no, i en cas de voler acabar, trencarem el bucle.

    ```python
    while True:
        # Demanem el numero i calculem el doble
        n=int(input("Dona'm un numero: "))
        print("El numero es",n,"i el seu doble",2*n)

        # Preguntem a l'usuari si vol continuar
        resposta=input("Vols eixir del programa (s/n): ")
        if resposta=='s' or resposta=='S':
            break

    print("Acabant el programa. Adeu")
    ```

A l'executar apareix:

```
Dona'm un numero: 3
El numero es 3 i el seu doble 6
Vols eixir del programa (s/n): n
Dona'm un numero: 12
El numero es 12 i el seu doble 24
Vols eixir del programa (s/n): k        <ATENCIÓ>
Dona'm un numero: -3                    <ATENCIÓ>
El numero es -3 i el seu doble -6
Vols eixir del programa (s/n): s
```

Ocórre que:

 - Encara permet números negatius
 - Permet tot tipus de lletres com a resposta. Amb la 's' eixim, però seguim amb la `n`, la `k` i altres.

???+ Success "**Millora 2. Validació dels inputs** Per a fer aquesta millora anem a fer un bucle per a cada entrada de dades, fins permetre valors vàlids: números positius en la primera entrada i unas `s` o `n` en la segona."
    ```Python
    while True:
        # Demanem el numero i calculem el doble
        # iniciem el número a un valor incorrecte
        n=-1
        while n<0:      # mentre el numero siga incorrecte
            n=int(input("Dona'm un numero: "))      # Demanem el numero
            if (n<0):                               # Si està fora de rang li recordem a l'usuari
                print("El número ha de ser positiu. ",end='')   # end='' per a no botar de linia

        # Ja fora del bucle. Vol dir que el número és ja positiu
        # Fem els calcul
        print("El numero es",n,"i el seu doble",2*n)

        # Preguntem a l'usuari si vol continuar
        resposta='z'    # iniciem a un valor incorrecte
        while resposta!='s' and resposta != 'n':
            resposta=input("Vols eixir del programa (s/n): ")
            if resposta!='s' and resposta != 'n':
                print("Selecciona una de les lletres correctes. ",end='')

        if resposta=='s' or resposta=='S':
            break

    print("Acabant el programa. Adeu")
    ```

A l'executar comprovem que tot està funcionant de manera correcta:

```
Dona'm un numero: 6
El numero es 6 i el seu doble 12
Vols eixir del programa (s/n): n
Dona'm un numero: 2
El numero es 2 i el seu doble 4
Vols eixir del programa (s/n): k
Selecciona una de les lletres correctes. Vols eixir del programa (s/n): n
Dona'm un numero: -4
El número ha de ser positiu. Dona'm un numero: -17
El número ha de ser positiu. Dona'm un numero: 90
El numero es 90 i el seu doble 180
Vols eixir del programa (s/n): s
Acabant el programa. Adeu
```

### 3.3.7. `else` en bucles

La sentència `else` normalment va precedida d'un `if` com hem vist al seu moment, però en `Python` pot anat precedida d'un bucle. Quan es fa servir amb bucles les ordres que posem al `else` s'executaran sempre que no s'haja executat un `break`. És una manera de controlar si el bucle ha acabat per ell mateix o per un `break`

```
bucle:
    sentencies
    if condicio:
        break
else:
    # coses a posar quan el bucle acaba per ell mateix. Sense break 
```

La part del `else` s'executarà sols quan el bucle ha acabat de manera normal:

- En un `while` per que la condició és `False`
- En un `for` per que s'han recorregut els elements de la llista
- Sols te sentit posar `else` en bucles que tinguen `break`. Sinó tenen `break` eixe codi s'executa sempre


### 3.3.8. La sentència `pass`

La sentència `pass` és fa servir quan volem deixar alguna zona del programa sense codi, be perquè estem a les fases inicials del programa i ho deixem per a desprès, be per millorar la llegibilitat. Simplement és una sentència que no fa res. Exemples:

```python
if x>1000:
    print("numero massa gran")
else:
    pass
```
Encara no sabem que farem al `else`, però de moment l'escric i més endavant veurem. 

`pass` es fa servir allí on cal posar una sentència de manera obligatòria però no volem posar res. Apareix molt en la POO (Programació Orientada a Objectes),  per a crear classes i/o mètodes buits:

```python
class prova:
    pass

def metodeQueSeQueFarePeroEncaraNoVullFer:
    pass        # Pendent d'implementar
```