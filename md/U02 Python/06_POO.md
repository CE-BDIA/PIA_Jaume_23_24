## 6.1 Definició de classes

### 6.1.1 Primera Classe
Python, a l'igual que altres llenguatges de programació permet la creació de classes. Podem fer-ho tal i com segueix:

???+ Note "Creació d'una classe `Alumne`"
    ```python
    class Alumne:
        pass        # inicialment sense res

    a=Alumne()      # creem el objecte. 

    print(a)        
    print(type(a))
    ```
    
    Ens mostrarà algo com:

    ```
    <__main__.Alumne object at 0x1029d6250>
    <class '__main__.Alumne'>
    ```

Podem ara afegir atributs a la nostre classe:

```python
class Alumne:
    dni=""
    nom=""
    cognoms=""
    edat=0

a=Alumne()

print("El nom és",a.nom)
print("La edat és",a.edat)
```

Ens donarà que les variables ja tenen valor, i llavors ja tenim els valors iniciats i podem fer servir els atributs. El problema és que si ho deixem així tots els objectes tindràn el mateix valor als seus atributs. Podriem deixar-ho així en compte de fer un _constructor per defecte_, encara que ja vorem que és convenient el crear-lo com segueix:

???+ Note "Creació d'una classe `Alumne` amb constructor per defecte"
    ```python
        class Alumne:
          def __init__(self):
            self.nom="Pere"
            self.edat=22

          def saludar(self):
            print("Hola, soc",self.nom)

        a=Alumne()      # creem el objecte. 
        a.saludar();
    ```

Fixar-se que ens trobem:

- `__init__` → aquest mètode és el que es coneix com a **constructor** i és el mètode que s'executa quan es crea un objecte
- `self` → és una variable especial que dins d'un objecte fa referència a ell mateix. És molt útil per a distingir quan una variable és la del objecte o altra (del programa principal o paràmetre). Aquest `self` és automàtic, i no cal passar-lo com a paràmetre, ja que és el propi objecte. A `Java` s'anomena `this`.

???+ Note "Creació d'una classe `Alumne` amb constructor amb paràmetres"
    ```python
    class Alumne:
      def __init__(self,nom="anònim"):
        self.nom=nom
        self.edat=22

      def saludar(self):
        print("Hola, soc",self.nom)

    a=Alumne()      # creem el objecte per defete. 
    a.saludar()

    b=Alumne("Pere")      # creem el objecte amb valors. 
    b.saludar() 
    ```

    ens donarà com a eixida:

    ```
    Hola, soc anònim
    Hola, soc Pere
    ```

## 6.2 Visibilitat dels atributs  

En la majoria dels llenguatges de programació, quan definim els atributs, hem d'especificar la modalitat d'accès del mateix. Existeixen 3 modificadors, que són `private` i `public`, i desprès un a meitat dels dos que és `protected`. Dits modificadors indiquen si podem accedir o no als atributs de la classe des de fora d'ella. Repassem-los:

> Nota: Des de dins de la classe sempre podem accedir als atributs de la mateixa, siguin publics o privats.

- `public` → Podem accedir als atributs des de fora de la classe
- `private` → No podem accedir als atributs des de fora de la classe
- `protected` → Són atributs públics, que es convertiran en `private` en les classes hereves d'on s'han definit. 

En Python no existeixen aquestes paraules reservades, però fa servir una manera curiosa de determinar-ho, que és la manera en la que posem el nom a les variables. Vejam-ho el següent classe `Empleat` i fixar-se detingudament en el nom que ens apareix desprès de `self`:

```python
class Empleat():

    def __init__(self,nom,edat,salari):
        self.nom=nom
        self._edat=edat
        self.__salari=salari

emple=Empleat("Pere",42,1230)

print("El nom es",emple.nom)
print("Edat es",emple._edat)
print("El salari és",emple.__salari)
```

ens produeix la següent sortida

```
El nom es Pere
Edat es 42
Traceback (most recent call last):
    File "provaClasses.py", line 66, in <module>
    print("El salari es",emple.__salari)
AttributeError: 'Empleat' object has no attribute '__salari'
```

Com podem comprovar:

- Per fer un atribut `public` el farem de manera normal sense fer ninguna cosa especial. El definirem amb `self.atribut`. Tenim l'exemple amb el `self.nom=nom`, i posteriorment accedim a ell amb `print("El nom és",emple.nom)` sense cap tipus de problema.
- Per fer un atribut `protected` el que farem serà definir l'atribut amb **un guió baix** al principi, `self._atribut`. Tenim l'exemple amb `self._edat=edat`. Com que l'accés per a la classe `Empleat` és públic podem seguir treballant amb dita variable desde fora de la classe sense que ens done cap error, amb la qual cosa `print("L'edat és",emple._edat)` funciona sense cap problema. Les particularitats del `protected` les estudiarem amb l'herència.
- Per fer una atribtu `private` el que farem serà definir l'atribut amb **dos guions baixos** al principi, `self.__atribut`. Tenim l'exemple amb `self.__salari=salari`. Com que ara l'accès és privat, llavors des de fora de la classe és com si aquest atribut no existira. Llavors si intentem fer `print("El salari és",emple.__salari)` ens bota l'excepció `AttributeError` amb el missatge  `'Empleat' object has no attribute '__salari'`

???+ Warning "Getters i Setters"
    Ni cal dir que la manera més estàndar i còmoda d'accedir als atributs és mitjançant els getters i setters, de manera que farem els atributs privats i els mètodes públics

???+ Note "Exemple complet"
    ```python
    class Empleat():

        def __init__(self,nom,edat,salari):
            self.__nom=nom
            self.__edat=edat
            self.__salari=salari
        
        def getNom(self):
            return self.__nom
        
        def getEdat(self):
            return self.__edat
        
        def getSalari(self):
            return self.__salari

    emple=Empleat("Pere",42,1230)

    print("El nom es",emple.getNom())
    print("Edat es",emple.getEdat())
    print("El salari és",emple.getSalari())
    ```

## 6.3 Altres mètodes i sobrecàrrega

Existeixen diversos mètodes interessants que de vegades caldrà escriure. Anem a veure'ls i els provem al nostre empleat:

???+ Note "toString i equals"
    ```python
    class Empleat():

      def __init__(self,nom,edat,salari):
          self.__nom=nom
          self.__edat=edat
          self.__salari=salari
      
      def getNom(self):
          return self.__nom
      
      def getEdat(self):
          return self.__edat
      
      def getSalari(self):
          return self.__salari
    
      def __eq__(self, other: object) -> bool:
          return self.__edat==other.__edat and self.__nom==other.__nom and self.__salari==other.__salari
      
      def __str__(self) -> str:
          # return self.__nom + " te " + str(self.__edat) + " i guanya " + str(self.__salari) + " euros"
          return f'{self.__nom} te {self.__edat} i guanya {self.__salari} euros'

    emple=Empleat("Pere",42,1230)
    emple2=Empleat("Pere",42,1230)

    print(emple==emple2)
    print(emple is emple2)

    print(str(emple))
    print(emple)
    ```

    ense retorna:

    ```
    True      # tenen els mateixos valors
    False     # NO SON el mateix objecte
    Pere te 42 i guanya 1230 euros  # representació del toString
    ```

## 6.4 Herència

Per a declarar una clase com a hereva d'altra, haurem de posar el seu nom entre parètesi. Anem a veure-ho amb altre exemple.

???+ Note "Exemple de Herència"
    ```python
    class Comercial(Empleat):
      def __init__(self,nom,edat,salari,comisio):
        # Empleat.__init__(self,nom,edat,salari)  Hi ha que indicar self com a paràmetre
        super().__init__(nom,edat,salari)    # amb super() i sense self
        self.__comisio=comisio

      def __str__(self):
        sou= self.getSalari() + self.__comisio
        return f'{self.getNom()} te {self.getEdat()} i guanya {sou} euros'

    comercial=Comercial("Joange",46,1200,300)
    print(comercial)    #Joange te 46 i guanya 1200 euros
    # ams __str__ l'eixida és Joange te 46 i guanya 1500 euros
    ```
  
  Com podem veure:

  -  `Comercial` hereta d'`Empleat`
  -  El primer que hem de fer al constructor de Comercial és cridar al constructor de  Empleat, i com que no existeix `super()` es fa indicant-ho directament. Això ens ve de perles també, ja que Python supporta herència múltiple
  -  Acabem d'assignar els atributs propis (`__comisio`)
  -  Si no definim el `__str__`, En la crida dins del print com que no l'hem definit, l'herència funciona adequadament, i es crida al `str` de Emplet. Cas de definir-lo, mostraria el missatge `Joange te 46 i guanya 1500 euros`.