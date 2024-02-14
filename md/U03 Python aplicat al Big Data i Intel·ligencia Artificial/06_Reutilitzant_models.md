## Introducció: I ara, què?

En aquesta unitat hem vist com podem entrenar un model a partir de datasets existent, i comprovar la bondat o no del mateix. Prèviament a l'entrenament (`fit` i `compile`) del model haurem d'haver preparat el dataset, eliminant les dades nules que poden apareixer (amb valids mitjans o més comuns), fent-les me adaptables per el model (normalitzant o codificant). Per a comprovar la bondat, a banda de les corbes de pèrdua durant l'entrenament, podem fer prediccions amb noves dades, mitjançant `predict`.

Però al dia a dia, les dades anirem generant-les en temps real, I ara, que?

### Guardem el model

Doncs un cop tinguem el model generat (sigui amb un model de Machine Learning o de Deep Learning), aquest model el podem guardar o començar a fer prediccions reals en el dia a dia. Això és el que s'anomena **posar en producció**. Per a fer això **haurem de guardar el model** com si d'un arxiu normal es tractara.

!!! info "Un model dins d'un arxiu"
    Aquest arxiu, que per exemple en Keras te la extensió `keras` o `h5`, contindrà el model, la configuració i, com no, tots els valors dels hiperparàmetres. Podriem obrir-lo i estudiar més en detall el seu contingut, però seria com obrir la XXNN, cosa que és l'equivalent a obrir la caixa de pandora, per la seua complexitat

Un cop guardar el model, simplement haurem de carregar-lo allà on volem fer-lo servir. Llavors, simplement ens quedarà el fer les prediccions que introdueix l'usuari, be mitjançant una GUI (aplicació d'escriptori o mòbil), be mitjançant una web (aplicació web), o be atenent les peticions des d'una API REST (servici)

!!! info "Consum de recursos en producció"
    No cal que la màquina aquesta ja tingui una gran capacitat de còmput, ja que en aquest moment no hem de calcular hiperparàmetres ni aplicar algorismes costosos com el Gradient Descend. En aquest moment la _caixa_ de la xarxa neuronal no és més que una fórmula, i el càlcul serà bastant simple.

#### Guardem amb keras

La llibreria keras ens dona les següents opcions. mirem-ho a partir d'aquest codi:

!!! example "Guardem el model"

    ```python
    # despres de fer totes les preparacions del model

    model.compile()   # compilem el model

    model.fit()       # i entrenem el model

    # guardem el model al disc
    model.save('ruta/a/model.keras')  # hem de posar-li la extensió .keras

    # per a carregar-lo
    model=keras.models.load('ruta/a/model.keras')
    ```

Aquest comandament desa **un model sencer en un sol fitxer**. El fitxer inclourà:

- L'arquitectura o **configuració** del model
- Valors dels **pesos** del model (que es van aprendre durant l'entrenament)
- La **informació de compilació** del model (si es va cridar a compile())
- L'**optimitzador i el seu estat**, si n'hi ha (això us permet **reiniciar** l'entrenament on vau deixar)

!!! warning "Quin és l'estandar?"
    Format `.h5` → El format **.h5** es refereix als fitxers que segueixen l'estàndard HDF5 (**Hierarchical Data Format versió 5**). Aquests fitxers poden contenir una varietat de dades, no només models de Keras:

    - Poden incloure dades multidimensionals, metadades i altres objectes.
    - Els models de Keras també es poden desar en fitxers .h5 utilitzant la funció model.save() de Keras amb l'extensió `.h5` en compte de `.keras`.
    - Els fitxers en format .h5 són més versàtils i poden ser compatibles amb una varietat d'eines i biblioteques que admeten el format HDF5.

    No obstant això, carregar models des de fitxers .h5 fora de l'entorn de Keras pot requerir l'ús de biblioteques addicionals com ara h5py per treballar amb el format HDF5.

    Recomanem `.keras`

#### Guardant qualssevol model. `joblibs`

Joblib és una biblioteca de Python dissenyada per simplificar la tasca de **desar i carregar objectes de Python** (com ara matrius NumPy, models d'aprenentatge automàtic, etc.) en el disc. El seu objectiu principal és proporcionar una manera **eficient** i **senzilla** de treballar amb dades grans i complexes, especialment en el context de l'aprenentatge automàtic i l'anàlisi de dades.

Amb Joblib, pots desar objectes de Python en el disc en un format eficient, la qual cosa significa que ocupen menys espai i es carreguen més ràpidament en comparació amb mètodes d'assignació de recursos estàndard com **pickle**. Això és particularment útil quan treballes amb conjunts de dades grans o models d'aprenentatge automàtic que poden ocupar una quantitat significativa de memòria. Això significa que pots utilitzar els **mateixos mètodes de manera intuïtiva per desar i carregar objectes, sense haver de preocupar-te pels detalls de la implementació subjacent**.

!!! example "Guardem el model amb joblibs"

    ```python
    import joblib
    # altres imports

    # preparem les dades

    # Creació del model
    model = ...

    # Compilació del model
    model.compile()

    # Entrenament del model
    history = model.fit()

    # Guardar el model, la història de compilació i els pesos amb Joblib
    # Si volem les dades ho tenim que fer per separat
    joblib.dump(model, 'model.joblib')
    joblib.dump(history.history, 'history.joblib')
    model.save_weights('model_weights.h5')
    ```

El gran aventatge és que en aquest cas, joblib permet guardar un model tant fet amb Keras d'una xarxa neuronal, com d'un fet amb Sklearn del Machine Learning clàssic

### Guardem la neteja de les dades

Sols ens queda en tindre en consideració les dades que li passarem al model per a fer les prediccions en el dia a dia. Si recordes, nosaltres partiem d'un dataset, al qual li feiem un preprocessat per adequar-ho a la xarxa neuronal. Doncs be, imagina que hem fet per exemple un escalat dels valors per predir el preu de cotxes a partir de les seues característiques. Hem codificat elèctric, hibrid, combustió amb el one hot encoding, i hem normalitzat la potència per a estar en valors entre [-2,2]. Ara imagina que un client vol una previsió de preu i ens passa les següents dades:

```json
{
  marca:Nissan,
  model:QashQai,
  potencia: 150cv,
  motor:combustio,
  ...
}
```

Evidentment aquesta informació la devem d'adaptar al nostre model:

1. El model treballa en entrades multidimensionals (dataframe de pandas o arrays de numpy)
2. Haurem d'aplicar la mateixa conversió (be ordinal be amb el one hot encoding), però espai, amb la mateixa configuració que hem fet per entrenar el model.
3. Harem de normalitzar tots aquells valors previs

!!! Example "Guardem la neteja de dades"

    ```python
    from sklearn.compose import make_column_transformer

    # Carreguem el dataframe
    X= pd.load(...)

    # característiquers numèriques del dataframe (normalitzar)
    features_num = [...]

    # característiques categoriques (one_hot o ordinal)
    features_cat = []

    # preparem el netejador
    preprocessor = make_column_transformer(
        (StandardScaler(), features_num),
        (OneHotEncoder(), features_cat),
    )

    # Entrenem el preprocessador amb totes les dades
    preprocessor.fit(X)

    # Apliquem els preprocessat a les dades
    X_processat=preprocessor.transform(X)

    # Acabem d'entrenar al model

    # Guardem el preprocessador
    joblib.dump(preprocessor,'preprocessador.pkl')

    # Guardem el model
    joblib.dump(model,'model.pkl')
    ```

Això ens permet,en un futur, quan tinguem que passar-li dades al nostre model, sobretot amb dades noves, preprocessar-les de la mateixa manera i en les mateixes condicions que el dataset que s'ha fet servir per a l'entrenament. Fariem alguna cosa com:

!!! Example "Carrega del preprocessador"

    ```python
    import joblib

    preprocessor=joblib.load('preprocessor.pkl')
    model=joblib.load('model.pkl')

    # imaginem les dades següents
    # Aquestes dades les rebem del client o pantalla o mobil
    dades_del_client={
      ...
    }

    # Funció que a partir de un json crea un array preparat
    def prepare_data(dades,preprocessador):
      # Passem el JSON a DF
      df_client=pd.DataFrame(dades,index=[0])

      # Apliquem el preprocessat
      data=preprocessor.transform(df_client)
      return data

    # preparem les dades
    dades=prepare_data(dades_client,preprocessor)

    # calculem la prediccio
    estimacio=model.predict(dades)
    ```