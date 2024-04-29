## Capturar imatges des de la càmera o webcam

Amb Opencv, a banda de manipular imatges emmagatzemades en fitxers, també podem capturar imatges i videos des de la webcam o des d'altres streams de video. Anem a veure primer alguns snippets que ens ajudaran en els nostres programes.

L'equip identifica les càmares connectades amb un número enter, i per a crear un objecte que connecta amb la càmera es farà servir `camera = cv2.VideoCapture(camera_index)`. Amb aquest objecte `camera` ja podrem fer les captures.

!!! note "Atenció"
    Amb aquest mateix mètode també podem obri un arxiu de video (stream) i processar-lo de manera molt similar al stream que produeix una càmera de video

Quan s'utilitza el mètode `(retorn,retorn)=cap.read()` a OpenCV per llegir d'una capturadora de vídeo, el que es llegeix és **un sol fotograma del vídeo en curs**. El mètode cap.read() retorna una tupla amb dos valors:

- `retorn` → Aquest valor **booleà** indica si la lectura del **fotograma ha estat exitosa o no**. 
- `frame`: Aquest és **el propi fotograma** de vídeo que es llegeix. És una matriu NumPy que conté la informació de la imatge en format de píxels.


El mètode `cap.get()`  s'utilitza per obtenir propietats específiques de la càmera, retornant el valor actual de la propietat sol·licitada. Pot tenir un o dos arguments:

1. **Un Argument**: Si es proporciona un sol argument, aquest ha de ser un identificador que representi la propietat que es vol obtenir:
   
   - `cv2.CAP_PROP_FRAME_WIDTH`: Ample del fotograma.
   - `cv2.CAP_PROP_FRAME_HEIGHT`: Alt del fotograma.
   - `cv2.CAP_PROP_FPS`: Fotogrames per segon que permet capturar.
   - `cv2.CAP_PROP_POS_FRAMES`: Posició del fotograma actual en la seqüència (vídeo).
   - `cv2.CAP_PROP_POS_MSEC`: Temps actual en mil·lisegons.
   - `cv2.CAP_PROP_FRAME_COUNT`: Nombre total de fotogrames al vídeo.

> Totes aquestes constants tenen valors enters que podem posar o trobar-nos en compte de la pròpia constant. Pots consultar-lo a la [documentació de openCV](https://docs.opencv.org/4.x/d4/d15/group__videoio__flags__base.html)


2. **Dos Arguments**: Si es proporcionen dos arguments, el primer és un identificador de la propietat, i el segon és un valor per defecte que es retorna si la propietat no es pot obtenir.

També disposem de `cap.set(arg,value)` que s'utilitza per modificar algunes propietats, com els FPS (**fotogrames per segon**) i la resolució del fotograma. Pot tenir dos arguments:

1. `arg` → identificador que representa **la propietat que es vol modificar**, entre les vistes anteriorment.

2. `value` → El segon argument és **el valor que es vol establir** per a la propietat de `arg`.

És important tenir en compte que **no totes les propietats de la capturadora es poden modificar** en tots els casos. 

!!! example "Posem la càmera a 640x480 i 30FPS"

    ```python
    import cv2

    # Obrim la càmera
    cap = cv2.VideoCapture(0)

    # Ressolució a 640x480
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Cambiem els FPS a 30
    cap.set(cv2.CAP_PROP_FPS, 30)

    # Alliberem la càmera
    cap.release()
    ```

!!! example "Quantes càmares tinc i quina és la seua ressolució"

    ```python
    def list_cameras():
    camera_list=[]
    for camera_index in range(5):   # 5 is the maximum number of cameras that we will check
        cap = cv2.VideoCapture(camera_index)
        if not cap.read()[0]:
        break
        else:
        cam={
            "index": camera_index,
            "resolution": f"{cap.get(cv2.CAP_PROP_FRAME_WIDTH)}x{cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}"
        }

        camera_list.append(cam)
        cap.release()

    return camera_list
    ```

!!! example "Fes una foto i mostra-la"

    ```python
    def take_picture(cam_id):
    cap = cv2.VideoCapture(cam_id)
    ret, frame = cap.read()
    if ret:
        cv2.imshow(f"Camera {cam_id}", frame)
        cv2.waitKey(0)          # Fins apretar una tecla
        cv2.destroyAllWindows()
    else:
        print(f"No puc obrir la càmera amb id:{cam_id}")
    cap.release()
    ```
  

## Videos

### Llegint imatges de video

Un video no és més que una seqüència de frames. D'aquesta manera OpenCV representa un video de la mateixa manera que el processament d'una càmera. Així doncs si volem obrir un video ho farem de manare molt similar a la càmera:

```python
source = 'el_meu_video.mp4'  # source = 0 for webcam

cap = cv2.VideoCapture(source)  # igual que la càmera

if not cap.isOpened():
    print("Error opening video stream or file")
    quit()

ret, frame = cap.read() # ja tenim el primer frame del video
```

### Escrivint videos

Per escriure el vídeo, necessites crear un objecte `VideoWriter` amb els paràmetres adequats.


```python
VideoWriter object = cv.VideoWriter(nom_del_fitxer, fourcc, fps, frameSize )
```

on els paràmetres son:


1. `filename`: Nom del fitxer de vídeo de sortida.

2. `fourcc`: Codi de 4 caràcters del **codec utilitzat per comprimir** els frames. Per exemple, `VideoWriter::fourcc('P','I','M','1')` és un codec MPEG-1, `VideoWriter::fourcc('M','J','P','G')` és un codec motion-jpeg, etc. Es pot obtenir una llista de codis a la pàgina ***Video Codecs by FOURCC***. El backend FFMPEG amb contenidor MP4 utilitza altres valors com a codi fourcc: consulta ObjectType, per la qual cosa pot ser que rebeu un missatge d'avís d'OpenCV sobre la conversió del codi fourcc. [Consultar aci](https://www.free-codecs.com/guides/fourcc.htm)

3. `fps`: Velocitat de fotogrames de l'stream de vídeo creat.

4. `frameSize`: Mida dels frames del vídeo.

::: example "Example d'escriptura de videos

    ```python
    # mantenim les mesures d'entrada
    frame_width = int(cap.get(3))    # cv2.CAP_PROP_FRAME_WIDTH
    frame_height = int(cap.get(4))   # cv2.CAP_PROP_FRAME_HEIGHT

    # Define the codec and create VideoWriter object. per a dos videos distints
    out_avi = cv2.VideoWriter("race_car_out.avi", cv2.VideoWriter_fourcc("M", "J", "P", "G"), 10, (frame_width, frame_height))

    out_mp4 = cv2.VideoWriter("race_car_out.mp4", cv2.VideoWriter_fourcc(*"XVID"), 10, (frame_width, frame_height))

    # Llegim i escrivim als nous formats
    while cap.isOpened():
        # Llegim un fram
        ret, frame = cap.read()

        if ret:         # Si hi ha frame, guardem
            out_avi.write(frame)
            out_mp4.write(frame)

        #   Si no hi ha frame... acabem
        else:
            break
            
    cap.release()
    out_avi.release()
    out_mp4.release()
    ```