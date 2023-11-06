Es demana crear un contenidor i començar a treballar amb mongo.

1. Crear el contenidor

```sh
docker run --name mongo-test \
    -e MONGO_INITDB_ROOT_USERNAME="root" \
    -e MONGO_INITDB_ROOT_PASSWORD="toor" \
    -p 27017:27017 \
    -d mongo
```

2. Un cop creat comprovem que ens podem connectar i veure quines bases de dades existeixen:

```sh
mongo -u root -p toor

sh dbs
```

3. Tanquem la connexió amb el comandament `exit` i anem a importar una col·lecció. Al recursos tens l'arxiu [restaurants.json](restaurants.json) per a descarregar a la carpeta de treball. 

```sh
mongoimport --uri 'mongodb://localhost:27017' \
  --username='root' --password='toor' --authenticationDatabase=admin \
  --db proves_pia --collection restaurant --file restaurants.json
```

4. Entra i comprova que hi han 3772 documents a la col·lecció
```sh
use proves_pia
db.restaurant.count()
```

5. Ix i torna a importar-ho. 
   1. Entra i comprova que ara hi han 7544.
   2. Ix de nou i torna a importa-ho, però ara amb la opció `--drop`
   3. Comprova que tornen a hi haura 3772 documents.

6. Exporta la col·lecció de restaurants a un arrxiu distint. 
   1. Verifica el tamany i el contingut de l'arxiu.
   2. Són distints! Per què? Investiga-ho
7. Exporta ara de la col·lecció de restaurants a un CSV, amb els atributs name i cuisine.
```sh
mongoexport --uri 'mongodb://localhost:27017' --username='root' --password='toor'\
 --authenticationDatabase=admin --db proves_pia --collection restaurant 
 --type=csv --out restaurants.csv --fields=borough,cuisine
```


