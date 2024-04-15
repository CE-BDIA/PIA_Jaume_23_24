<https://course.spacy.io/es/chapter2>

## Introducció a Spacy

```python
# Importa spaCy
import spacy

# Crea un objeto nlp vacío para procesar español
nlp = spacy.blank("es")
```

`nlp` se refiere al _pipeline_ de tokenización, inicialment blanc per al espanyol.

```python
# Creado al procesar un string de texto con el objeto nlp
doc = nlp("¡Hola Mundo!")

# Itera sobre los tokens en un Doc
for token in doc:
    print(token.text)
```

¡
Hola
Mundo
!

Cuando procesas un string de texto con el objeto nlp, spaCy crea un objeto Doc - de "documento". El Doc te permite acceder a la información sobre el texto en una forma estructurada y sin perder información.

El Doc se comporta como una secuencia normal de Python y te permite iterar sobre sus tokens u obtener un token con su índice. ¡Pero hablaremos de estas cosas más tarde!

```python
doc = nlp("Eso cuesta €5.")

print("Índice:   ", [token.i for token in doc])
print("Texto:    ", [token.text for token in doc])

print("is_alpha:", [token.is_alpha for token in doc])
print("is_punct:", [token.is_punct for token in doc])
print("like_num:", [token.like_num for token in doc])
```

mostra:
```sh
Index:    [0, 1, 2, 3, 4]
Text:     ['Eso', 'cuesta', '€', '5', '.']

is_alpha: [True, True, False, False, False]
is_punct: [False, False, False, False, True]
like_num: [False, False, False, True, False]
```

Aquí puedes ver algunos de los atributos disponibles de los tokens:

- `i` es el índice del token dentro del documento padre.
- `text` devuelve el texto del token.
- `is_alpha`, `is_punct` y `like_num` devuelven valores booleanos que indican si un token está compuesto por caracteres alfabéticos, si es un signo de puntuación, o si parece ser un número. Por ejemplo, el token "10" - uno, cero - o la palabra "diez".

Estos atributos también se llaman **atributos léxicos**: se refieren a una entrada en el vocabulario y no dependen del contexto del token.


### Qué son los pipelines entrenados?

Le permiten a spaCy predecir atributos lingüísticos en contexto:
- Etiquetado gramatical
- Dependencias sintácticas
- Entidades nombradas
- Entrenados con textos de ejemplo anotados

Pueden ser actualizados con más ejemplos para afinar las predicciones. Algunas de las cosas más interesantes que puedes analizar son específicas al contexto: por ejemplo, si una palabra es un verbo o si un span de texto es el nombre de una persona.

Los componentes de los pipelines entrenados tienen modelos estadísticos que le permiten a spaCy hacer predicciones en contexto. Esto normalmente incluye el etiquetado gramatical, dependencias sintácticas y entidades nombradas.

Los pipelines son entrenados con datasets de textos de ejemplo anotados.

Los pipelines pueden ser actualizados con más ejemplos para afinar sus predicciones - por ejemplo, para que se desempeñe mejor en tus datos específicos.

spaCy provee varios paquetes de pipelines pre-entrenados que puedes descargar usando el comando spacy download. Por ejemplo, el paquete `es_core_news_sm` es un pipeline pequeño de español que provee soporte para todas las capacidades centrales y está entrenado usando textos de internet.

El método `spacy.load` carga el paquete del pipeline por su nombre y devuelve un objeto nlp.

El paquete provee los parámetros binarios que le permiten a spaCy hacer predicciones.

También incluye el vocabulario y los metadatos acerca del pipeline y el archivo de configuración utilizado para entrenarlo. El paquete le dice a spaCy cuál clase de lenguaje usar y cómo configurar el pipeline de procesamiento.

```python
# $ python -m spacy download es_core_news_sm
import spacy

nlp = spacy.load("es_core_news_sm")
```
Parámetros binarios
Vocabulario
Metadata (lenguaje, pipeline)
Archivo de configuración

### Predicción de etiquetas gramaticales

```python    
import spacy

# Carga el pipeline pequeño de español
nlp = spacy.load("es_core_news_sm")

# Procesa un texto
doc = nlp("Ella comió pizza")

# Itera sobre los tokens
for token in doc:
    # Imprime en pantalla el texto y la etiqueta gramatical predicha
    print(token.text, token.pos_)
'''
Ella PRON
comió VERB
pizza NOUN
'''
```

Revisemos las predicciones del modelo. En este ejemplo estamos usando spaCy para predecir etiquetas gramaticales, es decir, los tipos de palabras en contexto.

Primero, cargamos el modelo pequeño de español y recibimos un objeto nlp.

Luego, procesamos el texto "Ella comió pizza".

Por cada token en el doc, podemos imprimir en pantalla el texto y la etiqueta gramatical predicha usando el atributo .pos_.

En spaCy, los atributos que devuelven un string normalmente terminan con un guion bajo (_). mientras que atributos sin un guion bajo devuelven un valor ID de tipo entero.

Aquí el modelo predijo correctamente "comió" como el verbo y "pizza" como el sustantivo.

Además de las etiquetas gramaticales, también podemos predecir las relaciones entre las palabras. Por ejemplo, si una palabra es el sujeto o el objeto de una oración.

El atributo `.dep_` devuelve la etiqueta de la dependencia sintáctica predicha.

El atributo `.head` devuelve el token de la cabeza de la dependencia sintáctica. Otra forma de concebirlo es como el token "padre" al que esta palabra está atada.

```python
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
'''
Ella PRON nsubj comió
comió VERB ROOT comió
pizza NOUN obj comió
'''
```

spaCy usa un esquema de etiquetas estándar para describir dependencias sintácticas. Aquí verás un ejemplo de algunas etiquetas comunes:

- El pronombre "Ella" es un sujeto nominal unido al verbo - en este caso, a "comió".
- El sustantivo "pizza" es un objeto unido al verbo "comió". Este objeto está siendo comido por el sujeto "ella".

### Prediciendo entidades nombradas

```python
# Procesa un texto
doc = nlp(
    "Apple es la marca que más satisfacción genera en EE.UU., "
    "pero el iPhone, fue superado por el Galaxy Note 9"
)

# Itera sobre las entidades predichas
for ent in doc.ents:
    # Imprime en pantalla el texto y la etiqueta de la entidad
    print(ent.text, ent.label_)
'''
Apple ORG
EE.UU LOC
iPhone MISC
Galaxy Note 9 MISC
'''
```

Las entidades nombradas son "objetos de la vida real" que tienen un nombre asignado. Por ejemplo, una persona, una organización o un país.

La propiedad doc.ents te permite acceder a las entidades nombradas predichas por el modelo de reconocimiento de entidades.

La propiedad doc.ents devuelve un iterador de objetos Span, así que podemos imprimir en pantalla el texto y la etiqueta de la entidad usando el atributo .label_.

En este caso, el modelo predijo correctamente "Apple" como una organización, "EE.UU" como un lugar, "iPhone" y "Galaxy Note 9" con la categoría miscelanea.

### Tip: el método spacy.explain

Obtén definiciones rápidas de las etiquetas más comunes.

- `spacy.explain("LOC")`
'Name of politically or geographically defined location'
- `spacy.explain("NNP")`
'noun, proper singular'
- `spacy.explain("MISC")`
'Miscellaneous entities, e.g. events, nationalities, products or works of art'


## Encontrando patrones basados en reglas

¿Por qué no simplemente expresiones regulares?

Buscar patrones en objetos Doc, no solamente en strings
Buscar patrones en tokens y atributos de tokens
Usa las predicciones del modelo
Ejemplo: "araña" (verbo) vs. "araña" (sustantivo)

Comparándolo con las expresiones regulares, el matcher funciona con objetos Doc y Token, en vez de únicamente strings.

También es más flexible: puedes buscar patrones en textos, pero también en otros atributos léxicos.

Inclusive puedes escribir reglas que usen las predicciones del modelo.

Por ejemplo, encontrar la palabra "araña" únicamente si es un verbo y no un sustantivo.

Los patrones del matcher son listas de diccionarios. Cada diccionario describe un token. Los keys son los nombres de los atributos del token, mapeados a sus valores esperados.

En este ejemplo, estamos buscando dos tokens con el texto "iPhone" y "X".

También podemos usar otros atributos de los tokens para encontrar lo que buscamos. Aquí estamos buscando dos tokens que en minúsculas son iguales a "iphone" y "x".

También podemos escribir patrones que usen los atributos predichos por el modelo. Aquí estamos buscando un token con el lemma "comprar", más un sustantivo. El lemma es la forma básica, así que este patrón encontraría frases como "comprando leche" o "compré flores".

```python
import spacy

# Importa el Matcher
from spacy.matcher import Matcher

# Carga el modelo y crea un objeto nlp
nlp = spacy.load("es_core_news_sm")

# Inicializa el matcher con el vocabulario compartido
matcher = Matcher(nlp.vocab)

# Añade el patrón al matcher
pattern = [{"TEXT": "adidas"}, {"TEXT": "zx"}]
matcher.add("ADIDAS_PATTERN", [pattern])

# Procesa un texto
doc = nlp("Nuevos diseños de zapatillas en la colección adidas zx")

# Llama al matcher sobre el doc
matches = matcher(doc)

# Llama al matcher sobre el doc
doc = nlp("Nuevos diseños de zapatillas en la colección adidas zx")
matches = matcher(doc)

# Itera sobre los resultados
for match_id, start, end in matches:
    # Obtén el span resultante
    matched_span = doc[start:end]
    print(matched_span.text)
```

on:

- `match_id`: valor del hash del nombre del patrón
- `start`: índice de inicio del span resultante
- `end`: índice del final del span resultante

Cuando llamas el matcher sobre un doc, este devuelve una lista de tuples.

Cada tuple consiste de tres valores: el ID del resultado, el índice de inicio y el índice del final del span resultante.

Esto significa que podemos iterar sobre los resultados y crear un objeto Span: un slice del doc que comienza en el índice de inicio y termina en el índice del final.

```python
pattern = [
    {"IS_DIGIT": True},
    {"LOWER": "copa"},
    {"LOWER": "mundial"},
    {"LOWER": "fifa"},
    {"IS_PUNCT": True}
]
doc = nlp("2014 Copa Mundial FIFA: Alemania ganó!")

# 2014 Copa Mundial FIFA:
```

Aquí tenemos un ejemplo de un patrón más complejo usando atributos léxicos.

Estamos buscando cinco tokens:

Un token compuesto únicamente por dígitos.

Tres tokens insensibles a mayúsculas/minúsculas para "copa", "mundial" y "fifa".

Un token que está compuesto por puntuación.

El patrón encuentra los tokens "2014 Copa Mundial FIFA:".

```python
pattern = [
    {"LEMMA": "comer", "POS": "VERB"},
    {"POS": "NOUN"}
]
doc = nlp("Camila prefería comer sushi. Pero ahora está comiendo pasta.")
'''
comer tacos
comiendo pasta
'''
```

Los operadores y cuantificadores te permiten definir con qué frecuencia un token debe ser encontrado. Pueden ser añadidos con el key "OP".

Aquí, el operador "?" hace que el token determinante sea opcional, así que encontrará un token con el lemma "comprar", un artículo opcional y un sustantivo.

```python
pattern = [
    {"LEMMA": "comprar"},
    {"POS": "DET", "OP": "?"},  # opcional: encuentra 0 o 1 ocurrencias
    {"POS": "NOUN"}
]
doc = nlp("Me compré un smartphone. Ahora le estoy comprando aplicaciones.")
'''
compré un smartphone
comprando aplicaciones
'''
```

| Ejemplo      | Descripción                   |
|--------------|-------------------------------|
| {"OP": "!"}  | Negación: busca 0 veces       |
| {"OP": "?"}  | Opcional: busca 0 o 1 veces   |
| {"OP": "+"}  | Busca 1 o más veces           |
| {"OP": "*"}  | Busca 0 o más veces           |


### Exercici

Probemos el Matcher basado en reglas de spaCy. Vas a usar un ejemplo del ejercicio anterior y escribirás un patrón que encuentre la frase “adidas zx” en el texto.

Importa el Matcher desde spacy.matcher.
Inicialízalo con el vocab compartido del objeto nlp.
Crea un patrón que encuentre los valores "TEXT" de dos tokens: "adidas" y "zx".
Usa el método matcher.add para añadir el patrón al matcher.
Llama al matcher en el doc y guarda el resultado en la variable matches.
Itera sobre los resultados y obtén el span resultante desde el índice start hasta el índice end.

```python
import spacy

# Importa el Matcher
from spacy.matcher import Matcher

nlp = spacy.load("es_core_news_sm")
doc = nlp(
    "Los Olímpicos de Tokio 2020 son la inspiración para la nueva "
    "colección de zapatillas adidas zx."
)

# Inicializa el matcher con el vocabulario compartido
matcher = Matcher(nlp.vocab)

# Crea un patrón que encuentre dos tokens: "adidas" y "zx"
pattern = [{"TEXT": "adidas"}, {"TEXT": "zx"}]

# Añade el patrón al matcher
matcher.add("ADIDAS_ZX_PATTERN", [pattern])

# Usa al matcher sobre el doc
matches = matcher(doc)
print("Resultados:", [doc[start:end].text for match_id, start, end in matches])
```

### Exercici
Escribe un patrón que únicamente encuentre menciones de las versiones completas de iOS: “iOS 7”, “iOS 11” and “iOS 10”.

```pytohn
import spacy
from spacy.matcher import Matcher
​
nlp = spacy.load("es_core_news_sm")
matcher = Matcher(nlp.vocab)
​
​
doc = nlp(
    "Después de hacer la actualización de iOS no notarás un rediseño "
    "radical del sistema: no se compara con los cambios estéticos que "
    "tuvimos con el iOS 7. La mayoría de las funcionalidades del iOS 11 "
    "siguen iguales en el iOS 10."
)
​
# Escribe un patrón para las versiones de iOS enteras
# ("iOS 7", "iOS 11", "iOS 10")
pattern = [{"TEXT": "iOS"}, {"IS_DIGIT": True}]
​
# Añade el patrón al matcher y usa el matcher sobre el documento
matcher.add("IOS_VERSION_PATTERN", [pattern])
matches = matcher(doc)
print("Total de resultados encontrados:", len(matches))
​
# Itera sobre los resultados e imprime el texto del span
for match_id, start, end in matches:
    print("Resultado encontrado:", doc[start:end].text)
```

Escribe un patrón que únicamente encuentre formas de “descargar” (tokens con el lemma “descargar”) seguido por un token que tenga la etiqueta gramatical "PROPN" (proper noun).

```python
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("es_core_news_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "descargué Fortnite en mi computadora, pero no puedo abrir el juego. "
    "Ayuda? Cuando estaba descargando Minecraft, conseguí la versión de Windows "
    "donde tiene una carpeta '.zip' y usé el programa por defecto para "
    "descomprimirlo…así que también tengo que descargar Winzip?"
)

# Escribe un patrón que encuentre una forma de "descargar" más un nombre propio
pattern = [{"LEMMA": "descargar"}, {"POS": "PROPN"}]

# Añade el patrón al matcher y usa el matcher sobre el documento
matcher.add("DOWNLOAD_THINGS_PATTERN", [pattern])
matches = matcher(doc)
print("Total de resultados encontrados:", len(matches))

# Itera sobre los resultados e imprime el texto del span
for match_id, start, end in matches:
    print("Resultado encontrado:", doc[start:end].text)

'''
Total de resultados encontrados: 3
Resultado encontrado: descargué Fortnite
Resultado encontrado: descargando Minecraft
Resultado encontrado: descargar Winzip
'''
```

Escribe un patrón que encuentre un sustantivo "NOUN" seguido de uno o dos adjetivos "ADJ"(un adjetivo y un adjetivo opcional).

```python
import spacy
from spacy.matcher import Matcher
​
nlp = spacy.load("es_core_news_sm")
matcher = Matcher(nlp.vocab)
​
doc = nlp(
    "El gigante tecnológico IBM está ofreciendo lecciones virtuales "
    "sobre tecnologías avanzadas gratuitas en español."
)
​
# Escribe un patrón para un sustantivo más uno o dos adjetivos
pattern = [{"POS": "NOUN"}, {"POS": "ADJ"}, {"POS": "ADJ", "OP": "?"}]
​
# Añade el patrón al matcher y usa el matcher sobre el documento
matcher.add("NOUN_ADJ_PATTERN", [pattern])
matches = matcher(doc)
print("Total de resultados encontrados:", len(matches))
​
# Itera sobre los resultados e imprime el texto del span
for match_id, start, end in matches:
    print("Resultado encontrado:", doc[start:end].text)

'''
Total de resultados encontrados: 3
Resultado encontrado: gigante tecnológico
Resultado encontrado: lecciones virtuales
Resultado encontrado: tecnologías avanzadas
'''
```



