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

Pueden ser actualizados con más ejemplos para afinar las predicciones