## 1. Computer Vision
Azure té bàsicament 2 serveis d'anàlisi d'imatges→

* **Computer Vision**→ Analitza el contingut d'imatges i vídeos.
* **Custom Vision**→ Ens permet personalitzar el reconeixement d'imatges per adaptar-lo a les nostres necessitats.

Ens centrem de moment en computer vision. Computer Vision ens permet→

* Detectar **elements** en una imatge
![ComputerVision](./img/AzureCompVision01.png)

* Obtenir les coordenades d'un rectangle que delimita l'**àrea principal** d'interès

![ComputerVision](./img/AzureCompVision02.png)
* Ens permet fer **miniatures** centrant-nos només en una zona d'interès.

![ComputerVision](./img/AzureCompVision03.png)
* Reconèixer text imprès o escrit a mà en imatges i PDFs (OCR)

![ComputerVision](./img/AzureCompVision04.png)

### 1.1. Anàlisi d'imatges

Quan utilitzem la funcionalitat d'anàlisi d'imatge podrem sol·licitar al servei les característiques següents→

* Categoria → classificació de la imatge dins una llista tancada de categories i subcategories.
* Etiquetes → llista de paraules rellevants per al contingut de la imatge. Es pot sol·licitar amb la funcionalitat _Independent Tag Image_.
* Descripció → genera una descripció de la imatge en una frase en **llenguatge natural**. Es pot sol·licitar amb la funcionalitat _Independent Describe Image_.
* Objectes → llista d'objectes trobats a la imatge, indicant per a cadascun el tipus d'objecte i les coordenades del rectangle que el delimita. Es pot sol·licitar amb la funcionalitat independent Detect Objects.
* Cares → llista de cares trobades a la imatge. Per a cada cara, se n'obté el rectangle associat, el gènere i l'edat estimada.
* Color → color dominant (de primer pla i fons) i color d'èmfasi de la imatge. També determina si la imatge és blanc i negre.
* Marques → marques comercials reconegudes a la imatge.
* Adults → determina si el contingut de la imatge pot ser catalogat com contingut per a adults, pujat de to o violent.
* Tipus d'imatge → detecta si la imatge és un dibuix o imatge predissenyada.

#### 1.1.1. Creant peticions

???+ example "Preparant la petició"
    ```python
    from azure.cognitiveservices.vision.computervision import ComputerVisionClient
    from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
    from msrest.authentication import CognitiveServicesCredentials

    # Add your key and endpoint
    key_computer_vision="XXX"
    endpoint_computer_vision= "https://XXX.cognitiveservices.azure.com/"
    region_computer_vision="eastus"

    # Preparem les característiques que vullguem
    visual_features=[
            VisualFeatureTypes.image_type,  # Could use simple str "ImageType"
            VisualFeatureTypes.faces,      # Could use simple str "Faces"
            VisualFeatureTypes.categories,  # Could use simple str "Categories"
            VisualFeatureTypes.color,      # Could use simple str "Color"
            VisualFeatureTypes.tags,       # Could use simple str "Tags"
            VisualFeatureTypes.description,  # Could use simple str "Description"
            VisualFeatureTypes.objects,     # Could use simple str "Objects"
            VisualFeatureTypes.adult,    # Could use simple str "Adult"
            VisualFeatureTypes.brands # Could use simple str "Brands"
        ]
    credentials = CognitiveServicesCredentials(key_computer_vision)
    client = ComputerVisionClient(
      endpoint=endpoint_computer_vision,
      credentials=credentials)

    # fem la petició
    image_analysis = client.analyze_image(url_image,visual_features=visual_features)
    ```

???+ info Petició
    La petició que ens ha permés efectuar l'anàlisi és `client.analyze_image(url_image,visual_features=visual_features)`. Com podem veure:

    * li pasem la url de la imatge a estudiar
    * Li indiquem les característiques que volem obtenir de la mateixa
    * En compte de `analyze_image` podem cridar a `analyze_image_in_stream` passant-li la imatge pròpiament dita en compte de la url de la mateixa.
  

#### 1.1.2. Processant les respostes
El servei ens retornarà un objecte del tipus `ImageAnalysis`, que contindrà, segons el demanat les següents claus, del tipus indicant:
```json
{
    'adult': AdultInfo,
    'brands': [DetectedBrand],
    'categories':[Category],
    'color': ColorInfo,
    'description': ImageDescriptionDetails,
    'faces': [FaceDescription],
    'imageType': ImageType,
    'metadata': ImageMetadata,
    'modelVersion': str,
    'objects':[DetectedObject],
    'requestId': str,
    'tags': [ImageTag]
  }
```

Pot consultar-se si tenim o no dits atributs:

* `dir(objecte)` → Retorna una llista amb els nom i mètodes del objecte.
* `hasattr(objecte, element)` →  retorna `True` si l'objecte te dit element.

Fixar-se que alguns atributs estan tancats entre claudàtors, el que significa que el valor retornat és una llista, i tindrem per tant una col·lecció d'objectes, com per exemple s'han detectat diversos objectes.

#### 1.1.3. Dibuixant caixes

Podem fer servir les llibreries de `matplotlib` combinades amb la llibreria `PIL` per a representar les imatges analitzades i afegir els mecanismes de detecció.

Una de les coses més habituals serà tancar en una caixa (rectangle) els objectes i cares detectades. És per això que tant els objectes `FaceDescription` com `DetectedObject` inclouen un atribut `rectangle`, amb les coordenades del **vertex superior esquerre** i l'**alt i ample**.

???+ example "Dibuix de caixes sobre objectes"
    Prèviament:
    
    *  s'ha carregat en la variable `img` la imatge a processar.
    *  El servei ens ha retornat l'estudi en la variable `analysis`

    ```python
    import matplotlib.pyplot as plt
    from PIL import Image, ImageDraw

    fig = plt.figure(figsize=(16, 8))

    if analysis.objects:
    for object in analysis.objects:
        r = object.rectangle
        bounding_box = ((r.x, r.y), (r.x + r.w, r.y + r.h))  # sup-esq a inf-dret
        draw = ImageDraw.Draw(img)                           # dibuixem imatge sencera
        draw.rectangle(bounding_box, outline='magenta', width=5)  # dibuixem caixa
        plt.annotate(object.object_property,(r.x, r.y), backgroundcolor='magenta')   # etiqueta de la caixa

    plt.axis('off')
    plt.imshow(img)
    ```

### Exercici.

A partit d'una imatge que tinga 3 o 4 objectes ben diferenciats has de :

* Pássala a Azure per a analitzar-la.
* A partir dels objectes que et retorna:
  * Retalla cadascun dels objectes
  * Guarda una imatge amb cada retall aconseguit
  
   
### 1.2. Àrees d''interes

### 1.3. Miniatures

### 1.4. OCR des d'imatges

  

