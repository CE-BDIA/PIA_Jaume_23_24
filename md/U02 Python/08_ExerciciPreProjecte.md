## Exercici: Gestió d'una Biblioteca

Crea una aplicació de línia de comandes de gestió de biblioteca en Python que utilitze els conceptes de POO vistos en classe. La biblioteca ha de ser capaç de gestionar material (llibres, revistes i pel·lículs), socis i administradors de préstecs. 

Cada llibre ha de tindre:
- un títol
- un autor
- un número d'exemplars disponibles

Cada revista ha de tindre:
- un títol
- un data de publicació
- un número d'exemplars disponibles

Cada pel·lícula ha de tindre:
- un títol
- un director
- un gènere
- un número d'exemplars disponibles

Cada soci ha de tindre:
- un nom
- un DNI
- una llista de llibres prestats.

Cada administrador de préstecs ha de tindre:
- un nom
- un DNI
- un càrrec (administrador o ajudant)

L'aplicació ha de permetre les següents funcions:

- Afegir un llibre a la biblioteca amb la informació del títol, autor i nombre d'exemplars disponibles.
- Afegir una pel·lícula a la biblioteca amb la informació del títol, director, gènere i nombre d'exemplars disponibles.
- AAfegir una revista a la biblioteca amb la informació del títol, la data de publicació i nombre d'exemplars disponibles.
- Afegir un soci amb el seu nom i DNI.
- Afegir un administrador amb el seu nom, DNI i càrrec.
- Prestar un recurs a un soci. Cal verificar que el recurs estiga disponible i que el soci no haja superat el límit de llibres prestats (per exemple, un màxim de 3 llibres per soci).
- Retornar un llibre.
- Mostrar una llista de tots els recursos, amb la possibilitat de filtrar per tipus. En el cas de pel·lícules s'haurà de filtrar també per gènere. En el cas de revista per any de publicació.
- Mostrar una llista de tots els socis.
- Mostrar una llista de tots els administradors de préstecs.
- Mostrar una llista amb la informació sobre quins recursos estan prestats a cada soci.

Definix una classe per a cada objecte i utilitzar correctament els conceptes de programació orientada a objectes com l'herència, encapsulació i mètodes per gestionar les operacions anteriorment mencionades. A més, en cada classe, afegeix unes proves, que sols s'executaran en cas que es cride al mòdul, però no si s'importa.

Crea també una classe principal o un programa de prova per interactuar amb la biblioteca.

Aquest exercici t'ajudarà a practicar els conceptes de programació orientada a objectes, com la creació de classes, la gestió d'objectes i la interacció entre ells.