Implementación y Desarrollo:
Se presenta a continuación el detalle técnico de los componentes físicos y la plataforma de software propuesto para el desarrollo del proyecto.

![tabla](https://github.com/jrochepy/Iot_team7_MITIC-FPUNA/assets/133827326/2cb39fb9-4931-4e67-a327-45e2a2110901)

Tabla 1. Selección de componentes propuestos


Diagrama de generación de información

A continuación, se presenta el esquema de conexiones de los componentes del sistema, se muestra un flujo de datos de la programación que realiza la generación de información, transmisión, procesamiento e interacciones.

![Imagen1](https://github.com/jrochepy/Iot_team7_MITIC-FPUNA/assets/133827326/2503b39e-f97a-427b-8a45-02c089e76414)

Figura 1. Diagrama de generación de eventos

En el esquema los sensores del dispositivo envían las temperaturas dato de telemetría a una aplicación conectada mediante Azure IoT Central. La aplicación en la nube supervisa las temperaturas y realiza acciones si la temperatura es demasiado baja o alta. Los dispositivos pueden recibir órdenes para ajustar la temperatura o iniciar y detener el funcionamiento. Se tiene un proceso de reserva en caso de que se produzca un error de funcionamiento en un sistema principal o este se quede sin conexión

 ![Imagen2](https://github.com/jrochepy/Iot_team7_MITIC-FPUNA/assets/133827326/f2b39051-a3b2-4679-b571-b50737433d4f)
 
Figura 2. Diagrama de flujo de evento

[![Alt text](https://img.youtube.com/vi/ggm8BB73cKA&t=4s/0.jpg)](https://www.youtube.com/watch?v=ggm8BB73cKA&t=4s)

Descripción de los componentes.

a.Sensor: Grove - Temperature & Humidity Sensor (DHT11)
Este dispositivo es un sensor de temperatura y humedad de alta precisión, amplio rango y un bajo costo.

b.	Actuador: Relay Board v1.0
Este actuador utiliza cuatro relés de alta calidad y proporciona interfaces NO/NC que controlan la carga de alta corriente.

c.	Gateway: Terminal Wio ATSAMD51 Core - Dev Board
Este gateway es un microcontrolador con conectividad inalámbrica. Posee varios periféricos multifuncionales y 40 pines GPIO.

d.	Servidor: Azure IoT Central
Este es un aPaaS (Plataforma de aplicaciones como servicio) de Microsoft que se ensambla de los componentes de PaaS de Azure en una plataforma de servicios totalmente administrada para el desarrollo y operaciones de aplicaciones de IoT.

Se opta por esta Plataforma de aplicaciones considerando las ventajas respecto a experiencia de usuario web, simplifica las operaciones, es escalable y segura. 

Cronograma de implementación propuesto.

En la Tabla X se presenta el cronograma propuesto para el desarrollo del proyecto, se puede ver que se otorga mayor cantidad de tiempo a las tareas de “Desarrollo de la plataforma” y “Pruebas y Optimización” de manera a lograr una respuesta óptima y eficiente en los resultados. A partir de la semana numero 17 en adelante se realiza el monitoreo del sistema.

![crono](https://github.com/jrochepy/Iot_team7_MITIC-FPUNA/assets/133827326/2697060c-bb08-4c25-8046-6c732469f2ec)

Tabla 2. Cronograma propuesto para la implementación
