## Recuperació 1a Avaluació 

### Exercici processament datasets.

Tenim un datasets que tracta sobre audiollibres extret de la plataforma Audible. Aquest dataset ha estat extret mitjançant la tècnica de scrapping, la qual cosa implica que les dades no estan preparades del tot.

A partir de l'arxiu csv que es subministra realitza les següents procediments:

Al llarg del dataset hi han alguns valors no existents o nuls, decideix el que fer amb ells, justificant el perque.
La columna author te el contingut així: Writtenby:GeronimoStilton, deixa-ho com a GeronimoStilton sòlament.
Repeteix el mateix procés amb la columna narrator, que el contingut apareix com Narratedby:BillLobely i has de deixar-ho com a BillLobely.
Els audiollibres tenen una duració, que és el temps que tarda el narrador en llegir-lo. EL temps apareix com a 2 hrs and 20 mins. Has d'aconseguir transformar-lo en un valor numèric amb la quantitat de minuts:
`2 hrs and 20 mins` seria `140`, en el cas de l'exemple.
`1 hrs` seria `60`
`35 mins` seria `35`
Si apareix qualssevol format inesperat, posar-lo a 0
Afig una nova columna ratings on guardarem el nombre de qualificacions, inicialment a nul.
Transforma la columna stars, que te el següent aspecte `5 out of 5 stars34 ratings`, deixant un `5` en la columna stars i un `34` en la columna acabada de crear ratings.
Si apareix qualssevol format inesperat, posar les dos columnes a 0
 Aplica una transformació one hot encoding a la columna language, deixant com a prefixe sols lang
Exporta el dataset amb nom dataset_cleaned.csv, sense guardar cap mena d'índex.
Entregar el programa o quadern jupyter que heu fet servir per netejar el dataset, així com el dataset un cop net.

## 2a avaluació

### Scrappig

Volem fer una xicoteta aplicació d'scrapping. Es tracta d'una web ja preparada aposta per a test d'scrapping. Es tracta de https://webscraper.io/test-sites/e-commerce/allinone/

Es demana fer scrapping dels ordinadors existents a dita botiga (Computers). Has d'obtenir sols els portàtils (Laptops).

Es demana crear un arxiu CSV, que continga per a cada ordinador avaluat: Marca, tamany de pantalla, processador, memòria RAM, disc, sistema operatiu preu bàsic i amb quins tamanys de disc estan disponibles.

Entregar tant el CSV generat com el programa que heu fet servir per generar-lo

### Backend

[Dataset preu de les cases IOWA](iowa.csv)

Donat l'anterior dataset, amb dades sobre els preus de les cases a l'estat d'Iowa. 

1. Entrena un model per a predir el preu d'una casa a aquest estat utilitzant les variables que consideres més importants (4 o 5).
2. Amb flask, crea una API rest que reba un json amb el valor d'eixes variables i com a resposta envie el resultat de la predicció.
3. Utiliza thunder client o postman per a comprovar que els resultats obtesos son coherents.

### Frontend

Utilitzant flet volem crear un traductor (semblant a la següent imatge):

![traductor](translator.png)

A la part esquerre introduiràs un text, indicaràs l'idioma (castellà, català, anglés) amb que està escrit i tindràs un botó d'enviar. 

A la part dreta obtindràs el resultat en l'idioma seleccionat (castellà, català o anglés). 

En polsar sobre el botó d'enviar, es llançarà una petició al servei d'Azure corresponent per a obtindre la traducció. Aquesta es pintarà a la part dreta, que no serà editable.