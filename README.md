# Instrumento de Evaluacion IoT
# Garay Garcia Cesar Enrique
# Zahir Andrés Rodríguez Mora
## Nombre del Personaje 
Cascanueces
## Creador
Cesar Enrique Garay Garcia 

|integrantes del equipo|
|----------------------|
|Cesar Enrique Garay Garcia|
|Zahir Rodriguez Mora|

## Explicacion de funcionamiento
Mi personaje va a ser un cascanueces navideño el cual tendra una base de carton, en la cual ira la cabeza del cascanuces, mientras esta da vueltas con un motor a pasas, al mismo tiempo abrira la boca con un servo que ira dentro de la cabeza. Se emitira una cancion navideña con un buzzer que estara en la cabeza, mientras que los ojos se mueven ya que estan hechos con pantallas oled. El movimiento dependera de la distancia capturada por el sensor se distancia, ademas que la base contara con adornos como una tira de leds con patrones navideños
## Materiales a utilizar 
|Material      |Imagen                                                                                                                                         |Cantidad|Costo  |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------|--------|-------|
|ESP32         |<img src="https://github.com/user-attachments/assets/e188873e-a56b-40c3-a138-fc124c85fb00" width="100"/>                                       |1       |$120    |
|HC-SR04       |<img src="https://github.com/user-attachments/assets/2633969b-87c6-49d2-bb9e-2a809461449f" width="100"/>                                        |1       |$30.00  |
|LED RGB       |<img src="https://www.electronicshub.org/wp-content/uploads/2021/05/Light-Emitting-Diode-Basics.jpg" width="100"/>                                       |5       |$10.00  |
|Servo Motor   |<img src="https://github.com/user-attachments/assets/41127814-7c83-44fc-9522-9777bc2c1e92" width="100"/>                                        |2       |$80.00  |
|Buzzer        |<img src="https://th.bing.com/th/id/OIP.zIU_nZXVd2FnBc2SaPXgewHaHa?rs=1&pid=ImgDetMain" width="100"/>                                        |1       |$15.00  |
|Protoboard    |<img src="https://cdn.shopify.com/s/files/1/0131/0792/0996/products/Protoboardde400puntos_2048x2048.jpg?v=1588537859" width="100"/>                                        |1       |$50.00  |
|Cables Jumper |<img src="https://asset.conrad.com/media10/isa/160267/c1/-/en/001970437PI01/image.jpg" width="100"/>                                        |Varios  |$20.00  |
|Batería 9V    |<img src="https://http2.mlstatic.com/duracell-bateria-alcalina-9v-mn1604b1-D_NQ_NP_777311-MLB20532680785_122015-F.jpg" width="100"/>   |1       |10.00  |
|Tijeras       |<img src="https://th.bing.com/th/id/OIP.Tx-l6ItCKWL9_l_63fsx1AHaHa?w=2500&h=2500&rs=1&pid=ImgDetMain" width="100"/>                                        |1       |$30.00  |
|Recistol      |<img src="https://th.bing.com/th/id/OIP.KF-JuA7AVXdaBMikpf9LcgHaHa?rs=1&pid=ImgDetMain" width="100"/> |1 |$20.00  |
|Cartón        |<img src="https://th.bing.com/th/id/OIP.7yh7oqTPH7djkT4J3kW0wwHaEU?rs=1&pid=ImgDetMain" width="100"/>|Varios |$10.00  |
|Pinturas|<img src="https://i0.wp.com/online.sanfelipeescolar.com.mx/wp-content/uploads/2021/03/18567.jpg?fit=500%2C500&ssl=1" width="100"/>|Varios  |$10.00|
|Pantalla OLED|<img src="https://th.bing.com/th/id/R.ceb0f9c85c12dc1e8be5ae3e232c16b2?rik=z2qL774vmm4MiQ&pid=ImgRaw&r=0" width="100"/>|Varios  |$150.00  |
|Botones|<img src="https://candy-ho.com/wp-content/uploads/2019/11/boton-de-servicio-iluminado-1.jpg" width="100"/>|Varios  |$150.00  |
|popote|<img src="https://arerofast.com/wp-content/uploads/2021/12/Popote-para-Tapioca-Oxo-Bio-1-Kg_3628-01-1.jpg" width="100"/>|Varios  |$2.00  |
|Bolas unicel|<img src="https://www.officedepot.com.mx/medias/73559.gif-1200ftw?context=bWFzdGVyfHJvb3R8NTg1MTN8aW1hZ2UvanBlZ3xoNzcvaGJlLzk0NjEwMjg4MTQ4NzguanBnfDMxZmViZTc4MDNmMmI3YjhmNWMyZTI1Yjg2ODdkYjFiM2Q4NDkxNmVmYmM4ODJmNjQ2OWM2MWUyYjEwYTRkZjA" width="100"/>|Varios  |$5.00  |
|Pistola de silicon|<img src="https://th.bing.com/th/id/OIP.exbrRglevOymj5jJmFZPKAHaHa?rs=1&pid=ImgDetMain" width="100"/>|Varios  |$150.00  |
|silicon|<img src="https://http2.mlstatic.com/D_NQ_NP_941759-MLM40437282716_012020-F.jpg" width="100"/>|Varios  |$30.00  |
|Tira de leds|<img src="https://ideocasa.com/uploads/images/md/2022/26/tiras-led-arduino.jpg" width="100"/>|Varios  |$02.00  |
|Motor a pasos|<img src="https://lh4.googleusercontent.com/JRdKCD8UyudITGGyxt7A5xbCQESTkwvhrgboI00vJFA1VZbytiN_xVmHhFQm46ftscp3q_TdqnUYOoKgrioLFxyaP3ZzzbPHzv5e2SGX2Q7cNpDok72jlK9-DRQA1pRYJoS3UwCn" width="100"/>|Varios  |$50.00  |


## Software a utilizar 
|Software       |Versión       |
|---------------|--------------|
|Arduino IDE    |2.0.3         |
|Wokwi          |N/A           |
|Thonny         |4.1.6         |
|Node-red       |v4.0.5        |
|Node-js        |v20.15.1      |

## Dibujo del personaje 
![image](https://github.com/user-attachments/assets/ba0a213e-11b5-4d91-998c-48aaffe4321d)

## Comunicacion
La comunicación del usuario con el prototipo se realizará mediante una conexión inalámbrica a través del protocolo Wi-Fi usando Node-Red. El ESP32 actuará como un servidor Wi-Fi conectado mediante un broker a Node-red. Mediante este, el usuario podra controlar los pasos que avanza o retrocede el motor a pasos, tambien podra cambiar el tono de cancion que es emitida por el buzzer, mientras que ne la parte inferior se imprimira tanto la distancia de un objeto o persona y la temperatura del lugar.
![image](https://github.com/user-attachments/assets/e76594df-d1fd-438b-bd8f-90b5675cabb9)
![image](https://github.com/user-attachments/assets/ada32519-75a5-4743-99b0-b3a7208d76f1)


## Enlaces de la simulación de Wokwi Navidad
https://wokwi.com/projects/410247506847750145

## Enlaces de la simulación de Wokwi 
https://wokwi.com/projects/410247744825285633


## Videos del funcionamiento 

(https://drive.google.com/drive/folders/1bB0ah-XkBKzjL5KlCOgBnNVd5imOTrXh?usp=sharing)

## Fotos de elaboracion
![Imagen de WhatsApp 2024-12-02 a las 19 17 02_c34df781](https://github.com/user-attachments/assets/347515cf-cf54-4e0f-aad4-a9589f1f6e81)

![Imagen de WhatsApp 2024-12-02 a las 19 17 02_01515715](https://github.com/user-attachments/assets/a2fe1779-ca9d-475c-9f52-0b1436feb897)

![Imagen de WhatsApp 2024-12-02 a las 19 17 00_2018690f](https://github.com/user-attachments/assets/ce448d7f-b1c3-48b9-98fb-756776e4fd79)

![Imagen de WhatsApp 2024-12-02 a las 19 17 01_5d099e01](https://github.com/user-attachments/assets/af91f0a4-0500-4c51-819a-c7d845091a79)

![Imagen de WhatsApp 2024-12-02 a las 19 17 02_8e951a0e](https://github.com/user-attachments/assets/f4267078-e7c9-4c27-8973-6ad381403463)

![Imagen de WhatsApp 2024-12-02 a las 19 17 01_f6309e15](https://github.com/user-attachments/assets/3515d768-36e6-4d4d-be6f-1277358e8fbc)

![Imagen de WhatsApp 2024-12-02 a las 19 17 01_1c1c906f](https://github.com/user-attachments/assets/4fd6166a-879c-4ba5-8c66-cef751fed07d)

![Imagen de WhatsApp 2024-12-02 a las 19 17 01_9db91a29](https://github.com/user-attachments/assets/caf84a28-bdcf-49c0-ba71-b5f9252bda02)

![Imagen de WhatsApp 2024-12-02 a las 19 17 01_f821a37c](https://github.com/user-attachments/assets/79927547-9db9-4326-b5c5-ef362c761e32)




## Imagen de la captura de pantalla de los exámenes Cisco C
![image](https://github.com/user-attachments/assets/fa20304b-317d-4ed2-9806-bb29826f481f)
![image](https://github.com/user-attachments/assets/58b78486-29d6-4554-b370-83ddc6d2031c)
![image](https://github.com/user-attachments/assets/165ffecf-5a98-42fb-9413-5ef9fd72ebe8)
![image](https://github.com/user-attachments/assets/e0d38c4d-3a31-442a-9233-171c9b77aa13)
![image](https://github.com/user-attachments/assets/530715f3-925d-42b7-aec3-16a2abd91e7e)
![image](https://github.com/user-attachments/assets/84bbe28b-8a0b-4aed-8955-1e56603826cf)






