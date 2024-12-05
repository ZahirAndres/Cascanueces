# Instrumento de Evaluación IoT

## Creador
**Cesar Enrique Garay Garcia**  
**Zahir Rodríguez Mora**

---

## Nombre del Personaje
**Cascanueces**

---

## Explicación de Funcionamiento

Mi personaje va a ser un cascanueces navideño el cual tendrá una base de cartón, en la cual irá la cabeza del cascanueces. Mientras esta da vueltas con un motor a pasos, al mismo tiempo abrirá la boca con un servo que irá dentro de la cabeza. Se emitirá una canción navideña con un buzzer que estará en la cabeza, mientras que los ojos se mueven ya que están hechos con pantallas OLED. El movimiento dependerá de la distancia capturada por el sensor de distancia. Además, la base contará con adornos como una tira de LEDs con patrones navideños.

---

## Materiales a Utilizar

| Material      | Imagen                                                                                                                                          | Cantidad | Costo |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------|
| ESP32         | <img src="https://github.com/user-attachments/assets/e188873e-a56b-40c3-a138-fc124c85fb00" width="150" height="auto" />                       | 1        | $120  |
| HC-SR04       | <img src="https://github.com/user-attachments/assets/2633969b-87c6-49d2-bb9e-2a809461449f" width="150" height="auto" />                       | 1        | $30   |
| LED RGB       | <img src="https://www.electronicshub.org/wp-content/uploads/2021/05/Light-Emitting-Diode-Basics.jpg" width="150" height="auto" />               | 5        | $10   |
| Servo Motor   | <img src="https://github.com/user-attachments/assets/41127814-7c83-44fc-9522-9777bc2c1e92" width="150" height="auto" />                        | 2        | $80   |
| Buzzer        | <img src="https://th.bing.com/th/id/OIP.zIU_nZXVd2FnBc2SaPXgewHaHa?rs=1&pid=ImgDetMain" width="150" height="auto" />                           | 1        | $15   |
| Protoboard    | <img src="https://cdn.shopify.com/s/files/1/0131/0792/0996/products/Protoboardde400puntos_2048x2048.jpg?v=1588537859" width="150" height="auto" />| 1        | $50   |
| Cables Jumper | <img src="https://asset.conrad.com/media10/isa/160267/c1/-/en/001970437PI01/image.jpg" width="150" height="auto" />                            | Varios   | $20   |
| Batería 9V    | <img src="https://http2.mlstatic.com/duracell-bateria-alcalina-9v-mn1604b1-D_NQ_NP_777311-MLB20532680785_122015-F.jpg" width="150" height="auto" />| 1        | $10   |
| Tijeras       | <img src="https://th.bing.com/th/id/OIP.Tx-l6ItCKWL9_l_63fsx1AHaHa?w=2500&h=2500&rs=1&pid=ImgDetMain" width="150" height="auto" />             | 1        | $30   |
| Recistol      | <img src="https://th.bing.com/th/id/OIP.KF-JuA7AVXdaBMikpf9LcgHaHa?rs=1&pid=ImgDetMain" width="150" height="auto" />                          | 1        | $20   |
| Cartón        | <img src="https://th.bing.com/th/id/OIP.7yh7oqTPH7djkT4J3kW0wwHaEU?rs=1&pid=ImgDetMain" width="150" height="auto" />                          | Varios   | $10   |
| Pinturas      | <img src="https://i0.wp.com/online.sanfelipeescolar.com.mx/wp-content/uploads/2021/03/18567.jpg?fit=500%2C500&ssl=1" width="150" height="auto" />| Varios   | $10   |
| Pantalla OLED | <img src="https://th.bing.com/th/id/R.ceb0f9c85c12dc1e8be5ae3e232c16b2?rik=z2qL774vmm4MiQ&pid=ImgRaw&r=0" width="150" height="auto" />           | Varios   | $150  |
| Botones       | <img src="https://candy-ho.com/wp-content/uploads/2019/11/boton-de-servicio-iluminado-1.jpg" width="150" height="auto" />                        | Varios   | $150  |
| Popote        | <img src="https://arerofast.com/wp-content/uploads/2021/12/Popote-para-Tapioca-Oxo-Bio-1-Kg_3628-01-1.jpg" width="150" height="auto" />          | Varios   | $2    |
| Bolas Unicel | <img src="https://www.officedepot.com.mx/medias/73559.gif-1200ftw?context=bWFzdGVyfHJvb3R8NTg1MTN8aW1hZ2UvanBlZ3xoNzcvaGJlLzk0NjEwMjg4MTQ4NzguanBnfDMxZmViZTc4MDNmMmI3YjhmNWMyZTI1Yjg2ODdkYjFiM2Q4NDkxNmVmYmM4ODJmNjQ2OWM2MWUyYjEwYTRkZjA" width="150" height="auto" />| Varios | $5 |
| Pistola de Silicón | <img src="https://th.bing.com/th/id/OIP.exbrRglevOymj5jJmFZPKAHaHa?rs=1&pid=ImgDetMain" width="150" height="auto" /> | Varios | $150 |
| Silicón      | <img src="https://http2.mlstatic.com/D_NQ_NP_941759-MLM40437282716_012020-F.jpg" width="150" height="auto" /> | Varios | $30 |
| Tira de LEDs  | <img src="https://ideocasa.com/uploads/images/md/2022/26/tiras-led-arduino.jpg" width="150" height="auto" />| Varios | $2 |
| Motor a Pasos | <img src="https://lh4.googleusercontent.com/JRdKCD8UyudITGGyxt7A5xbCQESTkwvhrgboI00vJFA1VZbytiN_xVmHhFQm46ftscp3q_TdqnUYOoKgrioLFxyaP3ZzzbPHzv5e2SGX2Q7cNpDok72jlK9-DRQA1pRYJoS3UwCn" width="150" height="auto" /> | Varios | $50 |

---

## **Software a Utilizar**

| Software       | Versión       |
|----------------|---------------|
| Arduino IDE    | 2.0.3         |
| Wokwi          | N/A           |
| Thonny         | 4.1.6         |
| Node-red       | v4.0.5        |
| Node-js        | v20.15.1      |

---

## **Dibujo del Personaje**

<img src="https://github.com/user-attachments/assets/ba0a213e-11b5-4d91-998c-48aaffe4321d" width="300" height="auto" />

---

## **Comunicación**

La comunicación del usuario con el prototipo se realizará mediante una conexión inalámbrica a través del protocolo Wi-Fi usando Node-Red. El ESP32 actuará como un servidor Wi-Fi conectado mediante un broker a Node-red. Mediante este, el usuario podrá controlar los pasos que avanza o retrocede el motor a pasos, también podrá cambiar el tono de canción que es emitida por el buzzer, mientras que en la parte inferior se imprimirá tanto la distancia de un objeto o persona y la temperatura del lugar.

---

## **Enlaces de la Simulación de Wokwi Navidad**

[Simulación de Navidad en Wokwi](https://wokwi.com/projects/410247506847750145)

[Simulación de Wokwi](https://wokwi.com/projects/410247744825285633)

---

## **Videos del Funcionamiento**

[Videos en Google Drive](https://drive.google.com/drive/folders/1bB0ah-XkBKzjL5KlCOgBnNVd5imOTrXh?usp=sharing)

---

## **Fotos de Elaboración**

<div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center;">
  <img src="https://github.com/user-attachments/assets/347515cf-cf54-4e0f-aad4-a9589f1f6e81" width="200" height="auto" />
  <img src="https://github.com/user-attachments/assets/a2fe1779-ca9d-475c-9f52-0b1436feb897" width="200" height="auto" />
  <img src="https://github.com/user-attachments/assets/ce448d7f-b1c3-48b9-98fb-756776e4fd79" width="200" height="auto" />
  <img src="https://github.com/user-attachments/assets/af91f0a4-0500-4c51-819a-c7d845091a79" width="200" height="auto" />
  <img src="https://github.com/user-attachments/assets/f4267078-e7c9-4c27-8973-6ad381403463" width="200" height="auto" />
  <img src="https://github.com/user-attachments/assets/3515d768-36e6-4d4d-be6f-1277358e8fbc" width="200" height="auto" />
  <img src="https://github.com/user-attachments/assets/4fd6166a-879c-4ba5-8c66-cef751fed07d" width="200" height="auto" />
  <img src="https://github.com/user-attachments/assets/caf84a28-bdcf-49c0-ba71-b5f9252bda02" width="200" height="auto" />
</div>

---

## **Imagen de la Captura de Pantalla de los Exámenes Cisco C**

<div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center;">
  <img src="https://github.com/user-attachments/assets/fa20304b-317d-4ed2-9806-bb29826f481f" width="200" height="auto" />
  <img src="https://github.com/user-attachments/assets/58b78486-29d6-4554-b370-83ddc6d2031c" width="200" height="auto" />
  <img src="https://github.com/user-attachments/assets/165ffecf-5a98-42fb-9413-5ef9fd72ebe8" width="200" height="auto" />
  <img src="https://github.com/user-attachments/assets/e0d38c4d-3a31-442a-9233-171c9b77aa13" width="200" height="auto" />
  <img src="https://github.com/user-attachments/assets/530715f3-925d-42b7-aec3-16a2abd91e7e" width="200" height="auto" />
  <img src="https://github.com/user-attachments/assets/84bbe28b-8a0b-4aed-8955-1e56603826cf" width="200" height="auto" />
</div>
