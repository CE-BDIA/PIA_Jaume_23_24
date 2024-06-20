## Examen de Programació d'Intel·ligència Artificial

### Pregunta 1: Web Scraping

#### **Enunciat**:
Utilitzant la tècnica de web scraping, extrau la següent informació de cada portàtil listat a la pàgina [PcComponentes Portàtils](https://www.pccomponentes.com/portatiles):

1. Nom del producte
2. Preu
3. Característiques principals (com ara processador, RAM, capacitat de l'emmagatzematge, mida de la pantalla)
4. Enllaç al producte

**Requeriments**:
- Utilitza Python com a llenguatge de programació.
- Empra la llibreria BeautifulSoup per a analitzar el HTML.
- Guarda les dades extretes en un fitxer CSV amb les següents columnes: `Nom_Producte`, `Preu`, `Processador`, `RAM`, `Disc`, `Pes net`,  `Tamany de pantalla`, `Enllaç_Producte`.
- Gestiona les excepcions que poden sorgir durant el web scraping, com ara la pàgina que no respon o canvis en l'estructura del HTML.

**Entrega**:
- El codi font complet juntament amb el fitxer CSV generat.

## Pregunta 2: Comparativa d'Algorismes de Machine Learning

**Enunciat**:
Realitza un estudi comparatiu utilitzant almenys **tres algorismes de machine learning** diferents per a predir el preu de productes del següent [dataset](datasets/Laptop_price_dirty.csv). Els algorismes a comparar són:

1. Regressió Lineal
2. Màquines de Suport Vectorial (SVM)
3. Random Forest

**Entrega**:
- El codi font complet.
- Un informe que incloga una comparativa dels resultats, gràfics de rendiment, i una justificació del millor model basada en les mètriques d'avaluació.

## Pregunta 3: Optimització de Xarxes Neuronals

**Enunciat**:
Desenvolupa un model de xarxa neuronal per a predir el preu de productes basant-se en un conjunt de dades proporcionat. Experimenta amb diverses arquitectures, ajustant el nombre de capes i neurones, per determinar la configuració més eficaç.

**Requeriments**:
- Implementa una xarxa neuronal utilitzant una llibreria d'aprenentatge profund com keras.
- Prova diferents arquitectures de xarxa, variat el nombre de capes ocultes i neurones per capa.
- Optimitza el procés d'entrenament per assegurar una convergència ràpida i evitar l'ajust excessiu.
- Genera un gràfic comparatiu que mostri l'impacte de les diferents arquitectures en el rendiment del model.

**Entrega**:
- El codi font complet del model de xarxa neuronal.
- El gràfic comparatiu dels resultats d'entrenament.
- Un informe que justifique els resultats, incloent una discussió sobre les decisions preses durant l'optimització del model.

## Pregunta 4: Creació d'un Backend amb Flask i MySQL en Docker

**Enunciat**:
Crea un servei backend amb Flask que expose dos endpoints HTTP. Quan el primer endpoint (entrada) reba una petició POST amb una matrícula de vehicle en el cos, el sistema haurà d'inserir un nou registre a la base de dades MySQL amb la matrícula proporcionada i el timestamp actual. Quan el segon endpoint (eixida) reba una petició, marcarà al registre l'hora d'eixida.

**Requeriments**:
- Utilitza Docker per a encapsular l'aplicació Flask i la base de dades MySQL.
- Configura la base de dades MySQL per a acceptar connexions des de l'aplicació Flask.
- Crea una taula `aparcament` amb les columnes `id`, `matricula`, `entrada` i `eixida`.
- Implementa la lògica per a processar peticions POST i inserir dades a la base de dades.
- Assegura't que el timestamp siga el moment exacte en què la petició és processada.

**Entrega**:
- El codi font de l'aplicació Flask.
- Els fitxers de configuració de Docker necessaris per a executar l'aplicació i la base de dades.
- Un script SQL per a crear la taula `aparcament` a la base de dades MySQL.
- Documentació que explique com construir i executar el contenidor Docker, així com com fer peticions al backend.
- Captures que demostren que el backend funciona.

## Pregunta 5: Desenvolupament d'un Frontend amb Càmera Web per a un Aparcament

**Enunciat**:
Desenvolupa una interfície d'usuari amb Flet que interactue amb el backend definit en la pregunta 4. L'aplicació haurà de:
- Activar la càmera web per permetre a l'usuari fer una foto de la matrícula del vehicle a l'entrada i a l'eixida de l'aparcament.
- Enviar la foto capturada al primer endpoint (entrada) del backend per inserir un nou registre amb la matrícula i el timestamp actual.
- Enviar una petició al segon endpoint (eixida) per marcar l'hora de sortida i calcular el temps total d'estada.
- Calcular el cost de l'aparcament a raó de **1 cèntim per minut**.
- Mostrar a l'usuari l'import total a pagar en el moment de la sortida.

**Requeriments**:
- Implementa la funcionalitat de càmera web dins de l'aplicació Flet.
- Assegura't que les fotos de les matrícules siguin clares i llegibles.
- Estableix una comunicació segura i eficient entre l'aplicació frontend i els endpoints del backend.
- Presenta a l'usuari una interfície clara i intuïtiva per a la captura de fotos i la visualització del cost.


**Entrega**:
- El codi font de l'aplicació Flet.
- Captures de pantalla o vídeos demostrant la funcionalitat de l'aplicació.
- Documentació que explique el flux d'interacció entre l'usuari, l'aplicació frontend, i el backend.