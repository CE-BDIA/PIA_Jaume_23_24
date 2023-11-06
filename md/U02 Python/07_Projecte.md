## Les figures
![Les figures](img/Figures.png)

## Preparem les estructures necessàries

Com a projecte final anem a implementar el clàssic exercici de les figures, on:

- Crea una classe `Punt` amb dos coordenades `(x,y)`, constructor i getters, setters, str. Implementar:
  - Un mètode _dist_ a altre punt passat com argument, que retorna la distància euclidea entre dos punts.
  - Un mètode _dist\_x_ i _dist\_y_ que retornen la distancia en horizontal i en vertical entre dos punts.
  - Comprova que el punt el tens ben implementat, executant:
```python
p1=Punt(2,3)
p2=Punt(3,4)
print("La distancia entre",p1,"i",p2," es ",p1.dist(p2))
```
- Crea una classe `Figura`, que conte un `Punt` (la posició on està ubicat) i un color (que serà un String de 7 caracters en hexadecimal). A banda dels mètodes habituals, també contindrà dos mètodes _area()_ i _perimetre()_, sense implementar. Comprova aquest codi:

```python
  p1=Punt(2,3)
  p2=Punt(3,4)
  color="#34FFDF"
  print (f'El color {color} valid={comprovaHEX(color)}')
  f=Figura(p1,color)
  print(f)
```
- Crea tres classes que hereten de `Figura`:
  
  -  `Rectangle`, afegint altre `Punt`. El `Punt` propi de `Figura` serà el superior esquerre, i el que afegeix `Rectangle` serà l'inferior dret (per convenció el cridarem `altre`). Reimplementar els mètodes conforme calen.
  -  `Cercle`, afegint un radi. El `Punt` de `Figura` suposarem serà el centre del cercle. Reimplementar els mètodes conforme calen.
  -  `Linia`, afegint altre `Punt`. Reimplementar els mètodes conforme calen, tenint en compte que l'area és 0, i considerarem com a perímetre la longitud de la línia.

Comprova que el codi:
```python
  p1=Punt(2,3)
  p2=Punt(3,7)
  color="#34FFDF"
  f=Figura(p1,color)
  print(f)

  l=Linia(p1,p2,color)
  print(l)
  print("La longitud es",l.perimetre())

  r=Rectangle(p1,p2,color)
  print(r)
  print("El perímetre es",r.perimetre())
  print("El area es",r.area())

  c=Cercle(p1,4,color)
  print(c)
  print("El perímetre es",c.perimetre())
  print("El area es",c.area())
```

retorna:
```
Figura situada en (2,3) de color #34FFDF
Linia situada de (2,3) a (3,7) de color #34FFDF
La longitud es 4.123105625617661
Rectangle situada de (2,3) a (3,7) de color #34FFDF
El perímetre es 10
El area es 4.0
Cercle situada en centre (2,3) i radi 4 de color #34FFDF
El perímetre es 25.132741228718345
El area es 50.26548245743669
```

## El dibuix

A banda de les estructures creades, hem de emmagatzemar totes les figures que creem en algun lloc. Eixe lloc serà el nostre dibuix, i per a no complicar les coses ho farem amb una variable global amb la següent estructura:
```python
Dibuix={
  "ample":800,
  "alt":600,
  "Figures":[]
}
```

Com pot veure's, 800x600 són les dimensions per defecte i inicialment no tenim cap figura. És en aquest array on anirem guardant-les, tal i com es descriu a continuació.

## Menu principal 

Un cop dissenyades i preparades les nostres estructures, anem a crear el programa per a poder dibuixar. El programa presentarà un menú com segueix:
```
Indica el que vols fer:
  1 - Afegir figura al dibuix
  2 - Carregar dibuix des de fitxer
  3 - Exportar  dibuix a SVG
  4 - Dibuixar i exir
```

L'usuari escollirà l'opció que desitje, com es veu a continuació. Desprès  d'executar totes les opcions es retornarà de nou a aquest menú, exepcte en la opció 4, com es veurà a continuació

### 1. Afegint figures al nostre dibuix

El programa mostrarà un nou submenú, i segons el que triem:
```
Indica la figura que vols afegir:
1 - Linia
  Introdueix les dades de la linia (x1 y1 x2 y2 #color):
2 - Rectangle
  Introdueix les dades de la Rectangle (x1 y1 x2 y2 #color): 
3 - Cercle
  Introdueix les dades de la Cercle (x1 y1 r #color): 
```

L'usari indicarà els paràmetres de la figura en qüestió, en el format indicat. Un cop llegida la linea que descriu la figura es crearà la figura corresponent (`Linia`, `Rectangle` o `Cercle`) i s'afegira al llistat de figures de `Dibuix`. Aquesta opció d'afegir figures la podrem executar tantes vegades com vullguem, com s'ha comentat en la descripció del menú.

???+ Warning "Atencio"
    Fer el control d'errors que cadascú considere. Per a verificar el color en hexadecimal, es disposa implementada de la següent funció
    ```python
    import re   #regular expression
    
    def comprovaHEX(hex_string):
      match =re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex_string)
      if match:
        return True
      else:
        return False
    ```

### 2. Carregant la informació desde fitxers

Tenim un format de fitxer de text com es veu a continuació.
```
dimensions 320 300
cercle 166 105 26 #94c147
rectangle 137 108 58 58 #ffffff
cercle 173 96 3 #ffffff
rectangle 126 115 11 31 #94c147
linia 186 75 164 93 #94c147
```

Deurem de:

- Demanar a l'usuari el nom del fitxer de text
- Llegir linia a linia d'aquest fitxer de text i avaluar la primera paraula del mateix:
  - `dimensions` --> modificarà les dimensions de la variable `Dibuix`
  - per a la resta de figures, crearà la figura corresponent i l'afegirà a la llista de figures de `Dibuix`

### 3. Exportant la informació a Inkscape

En aquest apartat, anem a exportar les figures que tenim a la variable `Dibuix` a un format estàndar de dibuix vectorial, el format `SVG`. Aquest format és text formatat com a XML, com podeu consultar an aquest enllaç [format svg](https://es.wikipedia.org/wiki/Gráficos_vectoriales_escalables):

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg height="300" width="320">
  <circle cx="166" cy="166" fill="#94c147" r="26"/>
  <rect fill="#ffffff" height="58" width="58" x="137" y="108"/>
  <rect fill="#94c147" height="31" width="11" x="146" y="150"/>
  <circle cx="151" cy="151" fill="#94c147" r="5"/>
  <line stroke="#94c147" stroke-width="3" x1="142 " x2="164" y1="75" y2="93"/>
</svg>
```

Haurem de:

- Crear a la clase `Figura` un mètode `toXML` abstracte.
- Implementar-lo en les classes hereves, definint-lo i transformat el contingut de cada `Figura` com es veu a l'exemple
- Recorrer tot el contigut de la variable `Dibuix` i guardar-lo a un fitxer de text, amb l'extensió SVG. 
- El nom del fitxer es preguntarà a l'usuari.
  
### 4. Pintant i eixint

Per a acabar, es subministra un mètode ja totalment implementat per a representar gràficament el nostre `Dibuix` i acabar el programa. Aquest programa fa servir la llibreria `Flet`, que estudiarem més endavant per a crear interfícies d'usuari, i concretament la llibreria `canvas` (llençol o lienzo en castellà) per a dibuixar figures. Presetem la estructura del codi, sense entrar massa en detalls. Al programa de partida que se us passa la podeu consultar tota.

```python
import flet as ft
import flet.canvas as cv

# creem el dibuix per defecte
Dibuix={
  "ample":800,
  "alt":600,
  "Figures":[]
}

# funció que dibuixa totes les figures. 
def dibuixar(page: ft.Page):
  pass

# Al programa principal, dins de la opció de menú 4
 elif opcio==4:
      print("Dibuixem i eixim")
      ft.app(target=dibuixar)   # Es crea una finestra flet amb la funció Dibuixar
      eixir=True
```

???+ Warning "**Important** per a que tot funcione adequadament"
    - Les classes han de dir-se exactament `Linia`, `Rectangle` i `Cercle`
    - La classe auxiliar `Punt`, ha de tindre els mètodes `getX()`, `getY()`, `__str__`, `dist()`, `dist_x()` i `dist_y()`
    - `Figura` ha de tindre els mètodes `getPos()`, `getColor()`, `__str__`, `toXML()`, `area()` i `perimetre()`
    - `Rectangle`, ademés, ha de tindre els mètode `getAltre()`, per a retornar el punt inferior dret.
    - `Linia`, ademés, ha de tindre els mètode `getAltre()`, per a retornar l'altre punt de la linia.
    - `Cercle`, ademés, ha de tindre els mètodes `getRadi()`, per a retornar el radi.

Als recursos i exercicis tens l'arxius [***U02_Projecte_0.py***](./exercicis/U02_Projecte_0.py)  com a punt de partida per a programar, així com els esquelets i funcions ja implementades.