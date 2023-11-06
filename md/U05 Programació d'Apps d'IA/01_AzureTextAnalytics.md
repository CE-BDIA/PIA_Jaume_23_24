## 1. El portal d'[Azure](https://portal.azure.com/)

Anem a treballar un concepte interessant en aquesta unitat, i és el que s'anomena **AIaaS** (_Intel·ligència artificial as a service_). Consistirà en fer servir plataformes amb models i eines ja entrenades, preparades per a utilitzar-les.

Començarem a treballar amb Azure, i podem veure la justificació [ací](./docs/PresentacionAzure.pdf).

> Aquests materials complementaris són de **Javier Catalá Jiménez**.

### 1.1. Alta amb Azure amb compte educatiu

Actualment la Conselleria d'Educació  disposa d'un contracte amb Microsoft on disposem d'un compte corporatiu, dins del domini `@alu.edu.gva.es` i `@edu.gva.es` per a alumnes i professors, respectivament. Amb aquest compte disposem de 100$ de saldo per a les recursos que utilitzem, i accès a la capa gratuïta dels serveis durant un any.

Aquests  serveis tenen certes limitacions, con per exemple 5000 transaccions mensuals, suficients per a la nostra feina dins del curs.

Podem seguir el procediment d'alta [en aquesta presentació](./docs/00_Configurar_Azure.pdf)

### 1.2. Alta amb compte gratuït

Suposadament amb aquesta capa gratuïta tindrem prou per a les tasques del nostre curs. Aquesta funcionarà sempre que ens quede _algo_ de saldo.  La solució és crear-te un nou compte, amb un correu distint, obviament on tindràs 200$ i la capa gratuita de nou durant un any. 

El problema d'aquest recurs és que hem de posar el numero de la targeta de crèdit, amb la qual cosa hem de tenir molta cura de aturar els serveis que puguem arrancar, si no volem tindre sorpreses a final de més. Per sort, sembla que Microsoft abans de carregar-nos res ens enviarà un correu electrònic

![capa gratuita](./img/capa_gratis.jpeg)

### 1.3. Configuració general de les API d'azure

Anem a veure com és funcionament general d'aquest serveis d'IA:

1. Haurem de crear des de la plataforma el recurs que desitjem; veu, imatge, so, etc.
2. Un cop creat, haurem de veure a la seua configuració els paràmetres:
      1. _entrypoint_ → és la url del recurs, on farem les peticions del mateix
      2. _key_ o _token_ → és el identificador que ens ha assignat Azure per a fer ús del recurs.
3. Des del nostre programa carregarem la llibreria per a connectar-nos
4. Farem la petició
5. Processarem els resultats

Pots veure el procés de creació als següents passos. En auqest cas veurem el de text, que és el primer que treballarem:

1. Li creem un nou recurs de Anàlisi de text:
![peticions a la API](./img/ServeiTextAzure01.png)

2. Li diguem crear:
![peticions a la API](./img/ServeiTextAzure02.png)

3. Es deixen les característiques per defecte, sense afegir-ne cap altra:
![peticions a la API](./img/ServeiTextAzure03.png)

4. Indiquem que el grup de recursos, o el creem si és el primer cop (com a nom, `UDCognitiveServices` o simimlar) i un nou recurs d'Anàlisi de Text, per exemple `TextAnalyticsDemoJoange`
![peticions a la API](./img/ServeiTextAzure04.png)

5. Li indiquem el pla de pagament, gratuït. Revisem i llavors acceptem els termes de licència:
![peticions a la API](./img/ServeiTextAzure05.png)

6. Finalment creem:
![peticions a la API](./img/ServeiTextAzure06.png)

7. I ja tenim el servei a punt.
![peticions a la API](./img/ServeiTextAzure07.png)


Podem fer les peticions mitjançant _request_, postman o curl, però ens serà més complicat, sobretot per temes de seguretat:

![peticions a la API](./img/AzureRequest.png)

La millor alternativa és fer servir les llibreries del SDK de Azure, disponibles per als llenguatges de programació més utilitzats:

![peticions a la SDK](./img/AzureSDK.png)

Aquest eines, a banda d'oferir objectes estructurats per a enviar i arreplegar la informació, encripten automàticament les peticions (i la informació que viatja amb elles), donant-li una major capa de protecció.

## 2. Llenguatge - Anàlisi de sentiments

Anem a estudiar com podem analitzar els sentiments d'un text. L'anàlisi de sentiments és com **fer un exàmen d'emocions en textos per determinar si el contingut expressa opinions positives, negatives o neutres**. Els algorismes d'anàlisi de sentiments utilitzen **processament del llenguatge natural** (PLN) per analitzar les paraules i frases en un text i determinar la seva _tonalitat emocional_.

Això implica:

* identificar paraules clau, 
* frases o contextos que indiquin sentiments

Per exemple, si algú diu *estic molt content amb aquest producte*, el sistema hauria de reconèixer la paraula _content_ i interpretar-la com una expressió positiva.

Aquesta tecnologia és molt utilitzada en:

* monitorització de xarxes socials 
* ressenyes de productes
* opinions dels clients i 
* altres àmbits on es vol entendre la resposta emocional dels usuaris. 

Hi ha diverses eines i plataformes que ofereixen serveis d'anàlisi de sentiments utilitzant tecnologies de **processament del llenguatge natural** (PLN). Algunes d'aquestes inclouen:

1. **IBM Watson Natural Language Understanding:** Proporciona anàlisi de sentiments entre altres funcionalitats PLN.

2. **Google Cloud Natural Language API:** Ofereix anàlisi de sentiments i altres funcions de PLN.

3. **Microsoft Azure Text Analytics:** Proporciona anàlisi de sentiments, detecció d'idiomes i altres funcionalitats basades en text.
   
4. **AWS (Amazon Web Services)** ofereix una eina anomenada **Amazon Comprehend** que inclou funcionalitats d'anàlisi de sentiments, que pot detectar i analitzar les emocions expressades en text. A través de l'API d'Amazon Comprehend, pots enviar text i rebre informació sobre les emocions associades, com ara positiu, negatiu, neutre o mixt.

5. **Aylien:** Una plataforma de processament del llenguatge natural que ofereix anàlisi de sentiments i altres eines d'anàlisi de text.

6. **VADER (Valence Aware Dictionary and sEntiment Reasoner):** Una eina específica per a l'anàlisi de sentiments en anglès, molt utilitzada i senzilla.

7. **NLTK (Natural Language Toolkit):** Una llibreria de Python que inclou mòduls per a l'anàlisi de sentiments i altres tasques de PLN.

8. **TextBlob:** Una llibreria de Python que facilita l'anàlisi de sentiments i altres tasques relacionades amb el processament del llenguatge natural.

9.  **Hugging Face Transformers:** Una llibreria que proporciona models preentrenats per a diverses tasques, inclosa l'anàlisi de sentiments.

### 2.1. Detecció de sentiments amb Azure

Anem a estudiar les eines que ens ofereix el SDK de Python per a Azure

#### 2.1.1. Creació del client
L'objecte clau per fer la crida és el client, i aquest és els [`class azure.ai.textanalytics.TextAnalyticsClient`](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-ai-textanalytics/5.3.0/azure.ai.textanalytics.html?highlight=textanalyticsclient#azure.ai.textanalytics.TextAnalyticsClient)

Aquest classe presenta dos arguments:

* `endpoint (str)` → sent la **url** al nostre recurs del servei del llenguatge supportat per Azure. Es del tipus `https://<resource-name>.cognitiveservices.azure.com`.
* `credential (AzureKeyCredential or TokenCredential)` → La credencial necessaria per a validar el client al servei d'Azure. Pot ser de dos tipus:
    * `AzureKeyCredential` si fem servir un token del serveis de _Cognitive Services/Language API_
    * Un token credential de `azure.identity`.

Aquesta informació la pots extreure del servei que haurem creat prèviament. Des de les opcions del recurs: 
![Buscar les claus](./img/AzureKey01.png)

I les podem veure o inclòs directament copiar-les:
![Seleccionar](./img/AzureKey02.png)

???+ example "Example de configuració del client"
    ```python
    import os
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import TextAnalyticsClient

    """"  
    Si guardem les credencials com a variables d'entorn del SO
    les podem carregar amb aquestes instruccions
    endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]
    key = os.environ["AZURE_LANGUAGE_KEY"]
    """

    key="XXXXXXXXXXXXXXXXXXXXXXXXXX"
    endpoint= "https://nom_del_teu_recurs.cognitiveservices.azure.com/"
    text_analytics_client = TextAnalyticsClient(endpoint, AzureKeyCredential(key))
    ```

#### 2.1.2. Avaluant el sentiment

El mètode per a fer la petició és `analyze_sentiment`, amb aquesta sintaxi retallada:

```python
analyze_sentiment(
        documents: Union[List[str], 
        . . .
         → List[Union[AnalyzeSentimentResult, DocumentError]]
```

Per simplificar:

* A aquest mètode li passarem un o més textos, anomentats com a documents. Ha de ser una llista: 
    * Poden ser un llistat de textos, com a str:
  
    ```python
    documents=["Hola m'encanta aquest modul","Estic una mica cansat","I'm very bored"]
    ```

    * Un llistat del anomentat `TextDocumentInput`, en el qual podem donar-li més detalls:
  
    ```python
      documents=[{"id": "1", "language": "ca", "text": "Hola m'encanta aquest modul"},
                {"id": "1", "language": "es", "text": "Me encuentro cansado"},
                {"id": "1", "language": "en", "text": "I'm very bored"}]
    ```

* El retorn de la funció és una llista combinada (de tuples)  de [`AnalyzeSentimentResult`](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-ai-textanalytics/5.3.0/azure.ai.textanalytics.html?highlight=textanalyticsclient#azure.ai.textanalytics.AnalyzeSentimentResult) o `DocumentError`, amb tants elements com documents s'han passat.

???+ example "Valor real retornat"
    ```python
    AnalyzeSentimentResult(id=3, sentiment=negative, warnings=[], statistics=None,
    confidence_scores=SentimentConfidenceScores(positive=0.0, neutral=0.01, negative=0.98), 
    sentences=[
      SentenceSentiment(
        text=I'm very bored, 
        sentiment=negative, 
        confidence_scores=SentimentConfidenceScores(positive=0.0, neutral=0.01, negative=0.98), 
        length=14, 
        offset=0, 
        mined_opinions=[])], 
      is_error=False, 
      kind=SentimentAnalysis)
    ```

Com podem veure, les opcions importants del `AnalyzeSentimentResult` son:

* `sentiment` → ens classifica el text avaluat en **positiu, neutral o negatiu**. Pot apareixer un **mixed**.
* `confidence_scores` → ens informa de la probabilitat de cada un dels tres nivells.
* `sentences` → per a cada unitat del text individual (fixa't que divideix el text en sentències) ens torna a donar la informació per separat.

???+ example "Procés dels resultats"
    ```python
    # ens quedem en aqulles que no donen error, en un llistat
    docs = [doc for doc in result if not doc.is_error]

    # processem els documents
    for idx, doc in enumerate(docs):
      print(f"Opinión general del document {idx}: {doc.sentiment}"); 
      for sentencia in doc.sentences:
        print(f"\tOpinio de la frase {sentencia.text} és <{sentencia.sentiment}>")
    ```

## 3. Llenguatge. Detecció d'idioma

Per a anàlisi de llenguatge necessitem crear un recurs de traducció, de manera similar de com l'hem creat anteriorment.

![Azure Text Analytics](./img/AzureTranslate.png)

Per fer una primera detecció del llenguatge, haurem de procedir invocant al recurs d'Azure i cridar al mètode `detect_language` de l'analitzador de text:

???+ example "Accès al recurs i identificació del llenguatge"
    ```python
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import TextAnalyticsClient

    key="XXXXXX"
    endpoint= "https://textanalyticsdemojoange.cognitiveservices.azure.com/"
    text_analytics_client = TextAnalyticsClient(endpoint, AzureKeyCredential(key))

    TEXT1="En un lugar de la mancha de cuyo nombre"
    TEXT2="Once upon a time"
    TEXT3="Dans la deuxième partie (Cosette), on voit Jean Valjean s'évader, arracher Cosette aux Thénardier, et tenter de s'installer à Paris"

    documents=[TEXT1,TEXT2,TEXT3]

    resultats=text_analytics_client.detect_language(documents)
    ```

Els resultat és un llistat (un per text enviat) de `DetectLanguageResult`, un objecte que el podem veure detallat com segueix:

```json
{ 'id': '0', 
  'primary_language':
  DetectedLanguage(
    name=Spanish, 
    iso6391_name=es, 
    confidence_score=1.0), 
  'warnings': [], 'statistics': None, 'is_error': False, 'kind': 'LanguageDetection'
}
```

on l'element més important és el `DetectedLanguage`, contenint com podem veure el nom del llenguatge i el grau de confiança de la detecció.

## 4. Llenguatge - Detecció d'entitats

La detecció d'entitats en text d'Azure és una funció que utilitza tecnologies de **processament de llenguatge natural** per identificar i extraure informació rellevant o entitats d'un text. Les **entitats** es refereixen a elements específics o conceptes dins del text, com ara **noms de persones**, **llocs**, **dates**, **quantitats**, etc.

Això pot ser molt útil en diverses aplicacions, com ara l'anàlisi de sentiments (vist), la categorització de contingut, l'extracció d'informació clau i altres tasques de processament de llenguatge natural.

Per fer-lo servir, haurem de fer referència a un `TextAnalyticsClient` com el que hem fet servir abans. A l'igual que abans, prepararem el text o texts dins d'un llistat de docuents, i cridarem el mètode `recognize_entities`. Pots trobar més informació [ací](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-ai-textanalytics/5.3.0/index.html#recognize-entities)

???+ example "Reconeixemnet d'entitats"
    ```python
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import TextAnalyticsClient

    key="XXXXXXXXXXXXXXXXXXXXXXXXXX"
    endpoint= "https://nom_del_teu_recurs.cognitiveservices.azure.com/"
    text_analytics_client = TextAnalyticsClient(endpoint, AzureKeyCredential(key))
    # iniciem els 3 text
    reviews = [TEXT1,TEXT2,TEXT3]
    
    result = text_analytics_client.recognize_entities(reviews)
    ```

El resultat és un llistat d'objectes de tipus `RecognizeEntitiesResult`, que ja deuriem de recòrrer per treure una col·lecció, anomenada `CategorizedEntity`, on tenim la informació de les entitats detectades. Ací podem veure un exemple de valor retornat:

```
RecognizeEntitiesResult(
  id=0, 
  entities=[
    CategorizedEntity(text=Francia, category=Location, subcategory=GPE, length=7, offset=13, confidence_score=1.0), 
    CategorizedEntity(text=verano, category=DateTime, subcategory=DateRange, length=6, offset=25, confidence_score=0.8), 
    CategorizedEntity(text=Provenza, category=Location, subcategory=GPE, length=8, offset=105, confidence_score=0.78), 
    CategorizedEntity(text=Normandía, category=Location, subcategory=GPE, length=9, offset=194, confidence_score=0.96), 
    CategorizedEntity(text=guía, category=PersonType, subcategory=None, length=4, offset=231, confidence_score=0.92), 
    CategorizedEntity(text=Pierre Martin, category=Person, subcategory=None, length=13, offset=237, confidence_score=1.0)], 
    warnings=[], statistics=None, is_error=False, kind=EntityRecognition)
```

### 4.1. Entitats enllaçades

Investiga al voltant de les [`Entitats enllaçades`](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-ai-textanalytics/5.3.0/index.html#recognize-linked-entities), on a banda de trobar les entitats, podem trobar enllaços per aprofundir en les entitas trobades.



## 5. Llenguatge -  Traducció de texts

Per a la traducció anem a fer una crida que no requereix d'un recurs propiament dit però si d'una credencial d'Azure. Com a novetat anem a fer-ho amb un request simple en compte d'eines concretes del SDK.
Hem de preparar per tant la petició del request, amb aquestes característiques:

```python
request = requests.post(constructed_url, params=params, headers=headers, json=body)
```

???+ example "Preparació de la url"

    ```python
    endpoint_textTranslation="https://api.cognitive.microsofttranslator.com/"
    path = '/translate'
    constructed_url = endpoint_textTranslation + path
    ```

    Amb això ja tenim el punt de conexió de la nosta API



???+ example "Paràmetres de la crida"
    En aquest apartat indicarem la versió de la api, així com l'idioma del text que anem a passar i una llista dels idiomes als quals volem traduir. Tenim a continuació un exemple:

    ```python
    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': ['ca', 'es']
    }
    ```

???+ example "Capçalera de la petició"
    Ací hem de indicar la metainformació de la petició, en el format esperat per la API. En la primera opció posarem la nostra clau del recurs `TextAnalytic` que hem creat.

    L'altra opció important és la localització del servei, al nostre cas europa de l'oest

    ```python
    key="la_nostra_clau_de_azure"
    location = "westeurope"
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    ```

???+ example "Text a traduir"

    Ens resta completar el cos de la petició, indicant els text o textos a traduir. Serà una llista amb tants elements json com desitjem, encapsultas dins d'una etiqueta `text`.

    ```python
    body = [
      {
      'text': 'Hello, friend! What did you do today?'
      },
      {
      'text': 'A long time ago in a galaxy far, far away....'
      }
    ]
    ```

???+ example "Crida i arreplegant el resultat"

    Finalment farem la crida i arreplegarem el resultat en un JSON. Aquest JSON conte una llista amb una col·lecció d'objectes, tants com texts passats:

    * Objectes amb clau `translations`, que tindra tindrà un llistat amb les traduccions als distints idiomes que hem indicat.
    * Cada objecte dins del llistat contindrà:
      * Una clau `to` on d'indica a quin idioma s'ha traduit
      * Una clau `text` amb el text traduit a l'idioma indicat

    ```python
    # crida
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    # extracció de resultats
    response = request.json()
    ```
    
    i el contingut de la resposta és pot veure a continuació:
    ```json
    [{
        "translations": [
            {
                "text": "Hola amic! Què has fet avui?",
                "to": "ca"
            },
            {
                "text": "¡Hola! ¿Qué has hecho hoy?",
                "to": "es"
            }
        ]
    },
    {
        "translations": [
            {
                "text": "Fa molt de temps en una galàxia llunyana, llunyana....",
                "to": "ca"
            },
            {
                "text": "Hace mucho tiempo en una galaxia muy, muy lejana...",
                "to": "es"
            }
        ]
    }]
    ```

### 5.1. Ampliació

Investiga per la teua part i intenta fer la implementació anterior amb eines pròpies del SDK d'Azure. Ens referim a `TextTranslationClient`

### 5.2. Traducció de documents

Respecte a la traducció de documents sencers, la deixarem com a opcional, ja que requereix de la creació d'un recurs especial, que pots suposar un cost afegit. Tot i ser relativament barat, anar en compte per no acabar el saldo que disposem d'Azure

La forma de treballar seria la següent:

1. Crear un [Azure Blob Storage containers](https://learn.microsoft.com/en-us/azure/ai-services/translator/document-translation/quickstarts/document-translation-rest-api?tabs=csharp&pivots=programming-language-csharp#create-azure-blob-storage-containers), que és un contenidor (espai) per a emmagatzemar els nostres documents a traduir.
2. Crear un [DocumentTranslationClient](https://learn.microsoft.com/en-us/azure/ai-services/translator/document-translation/quickstarts/document-translation-sdk?tabs=dotnet&pivots=programming-language-python), en el qual especificarem:
   1. Entrades: que seràn documents guardats al nostre contenidor
   2. Eixides: que es guardaran també al nostre contenidos

Queda proposat com a exercici opcional

## 6. Llenguatge - Text a veu i vice-versa

En primer lloc hem de crear un recurs de veu, dins del nostre contenidor de recursos.

![AzureVeu](./img/AzureVeu1.png)

Recorda de posar el pla gratuït. Als noms no poden fer-se servir barres baixes.

![AzureVeu](./img/AzureVeu2.png)

![AzureVeu](./img/AzureVeu3.png)

![AzureVeu](./img/AzureVeu4.png)

Per últim fixar-se que el recurs no és nostre propi, sinò és un _entrypoint_ genèric. Serà amb el token com s'accedirà al nostre recurs.

![AzureVeu](./img/AzureVeu5.png)

Al nostre programa ens caldrà per tant la regió i el token d'accès

### 6.1. Desenvolupant el programa, de veu a text

Necessitarem crear un objecte de tipus `SpeechConfig`, al qual li indicarem el token i la regio creada

???+ example "Creació del recurs de veu"
    ```python
    import azure.cognitiveservices.speech as speechsdk

    speech_key="XXXXXX"
    speech_region="westeurope"
    speech_endpoint="https://westeurope.api.cognitive.microsoft.com/sts/v1.0/issuetoken"

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
    speech_config.speech_recognition_language="es-ES"
    ```

A continuació necessitarem crear la configuració del audio i del reconeixedor de veu, tot a partir del sdk de veu:

???+ example "Audio i reconeixedor"
    ```python
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    ```
    
Ahí indiquem:

- Que farem servir el micròfon per defecte a la classe `AudioConfig`. Podeu trobar més informació [ací](https://learn.microsoft.com/es-es/javascript/api/microsoft-cognitiveservices-speech-sdk/audioconfig?view=azure-node-latest)
- Enllacem el microfon amb la configuració creada anteriorment

Finalmen farem servir el mètode `recognize_once_async` per a transcriure blocs de fins a 30 segons  o fins detectar un silenci. Podeu trobar més informació per a més coses dins de la documentació de [Reconeiximent de veu](https://learn.microsoft.com/es-es/azure/ai-services/speech-service/how-to-recognize-speech?pivots=programming-language-python)

???+ example "Crida i processament del resultat"
    ```python
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    print(str(speech_recognition_result))

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Text reconegut: {}".format(speech_recognition_result.text))
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No s'ha detectat text parlat: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("S'ha cancelat la parla: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Detall dels errors: {}".format(cancellation_details.error_details))
            print("Tens ben posat la clau i la zona de la parla?")
    ```

El resultat obtigut desprès de `speech_recognizer.recognize_once_async().get()` és algo un `SpeechRecognitionResult`

que te com a contingut:
```json
result_id=920a7d085efb4c23adf056e37df82986, 
text="Bon día com va tot?", 
reason=ResultReason.RecognizedSpeech
```
### 6.2. Desenvolupant el programa, de text a veu

Indiquem sols el programa d'exemple, el qual deuries de provar i analitzar.

??? example "Problema resolt de text a veu. Analitza'l"
    ```python
    import azure.cognitiveservices.speech as speechsdk

    # Creem la instancia del recurs de veu
    speech_key, service_region = "XXXX", "westeurope"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    # Establim la veu, a https://aka.ms/speech/voices/neural tens la llista completa. Espai que les neutres ja no funcionen.
    speech_config.speech_synthesis_voice_name = "es-ES-ElviraNeural"

    # Creem el sintetitzador de veu
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    # Llegim el text de l'usuari
    text = input("Escriu el text que vols narrar...")

    # Fem la crida asíncrona
    result = speech_synthesizer.speak_text_async(text).get()

    print(str(result))

    # Checks result.
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Text a reproduir [{}]".format(text))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Parla cancelada: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Detalls dels errors: {}".format(cancellation_details.error_details))
        print("Tens be la informació de la subscripció?")
    ``` 


### 6.3. Exercici

Intenta fer un programa que et demana textos, els transforma en veu i els guarda en arxiu de àudio (wav o mp3)

