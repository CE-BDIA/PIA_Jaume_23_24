
# 1 Què estem escoltant?


Fer un programa amb una GUI dissenyada amb flet, en la qual es demana textos escrits. Amb un botó demanarem a Azure que ens diga en quin idioma està dit text. Posteriorment farem una crida per a que ens el transforme a àudio, guardant-lo en wav o mp3. El programa reproduirà dit àudio.


# 2 Com de saludables son elements?

Volem a partir de la fotografia dels valors energètics d'un producte

![](https://images.openfoodfacts.org/images/products/842/169/134/8271/nutrition_es.5.full.jpg)

Passar un OCR que ens busque les quantitats per calcular el famòs **nutriscore** amb la fórmula que segueix:

![Nutriscore](https://sygmacert.com/wp-content/uploads/2020/11/nutriscore-calculo.jpg):

![](./img/Nutritional_info.jpg)

# 3 Predicció d'imatges (Lliure)

Crea una aplicació servidora que escoltara peticions des d'un client. El client ens enviarà una imatge, que serà recollida des del nostre servidor.

El servidor haurà de classificar-la amb un servei **creat prèviamnet** amb Azure de manera similar a l'apartat 5.3

La informació en l'element detectat serà retornada a l'aplicació client.

# 4 Traducció automàtica de manuscrits

Crea una aplicació amb Flet que utilitze la càmera web per capturar imatges de text manuscrit. Aquestes imatges s’enviaran a AWS Rekognition per a la seva anàlisi i reconeixement de text. El text que ens reconega, s'enviarà de nou a AWS Translate per a la seua traduccióa l’idioma seleccionat per l’usuari a través de la interfície.

- **Interfície d’Usuari (UI)**:
  - Activar la càmera web.
  - Prendre una fotografia del text manuscrit.
  - Seleccionar l’idioma de destí per a la traducció.
  - Visualitzar el text traduït.

- **Integració amb AWS Rekognition**:
  - Configurar una connexió amb AWS Rekognition.
  - Enviar la imatge capturada a AWS Rekognition per a l’anàlisi de text.
  - Recuperar el text reconegut des de AWS Rekognition.

- **Traducció**:
  - Configurar una conexió amb AWS Translate.
  - Traduir el text reconegut a l'idioma seleccionat per l’usuari.

- **Prova i Validació**:
  - Realitzar proves per assegurar-se que l’aplicació funciona correctament, validant la precisió del text reconegut i la traducció.

## Entrega:

- Codi font de l’aplicació Flet.
- Captures de proves i validació.