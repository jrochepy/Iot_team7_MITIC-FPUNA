7.	Implementación y Desarrollo:
Se presenta a continuación el detalle técnico de los componentes físicos y la plataforma de software propuesto para el desarrollo del proyecto.

Componentes	Fabricante/Modelo	Características principales
Sensor de temperatura y humedad	Seeed / Grove - Temperature & Humidity Sensor (DHT11)	Voltaje de entrada 3,3 V y 5 V
		Corriente de medición 1,3 - 2,1 mA
		Hum rango 5 ~ 95% de humedad relativa
		Temp rango -20 ~ 60℃
Actuador-intermedio	Seeed / Relay Board v1.0	Fuente de alimentación: 4.75~5.5V
Corriente de conmutación máxima: 15A
Actuador-contactor	ABB / AF30-30-22-13	Corriente Nominal: (A): 32 (kw): 15
Tensión de bobina (VCA): 100-250
Tensión Nominal (VCA): 690
MCU	Espressif / ESP8266	802.11 b/g/n
Voltaje de Alimentación: 5V DC
Pines Digitales GPIO: 17
Pin Analógico ADC: 1 (0-1V)
Certificación FCC
Antena en PCB
Servidor (Software Cloud)	Azure IoT Central	Plataforma de aplicaciones como servicio
Tabla 1. Selección de componentes propuestos


Diagrama de generación de información

A continuación, se presenta el esquema de conexiones de los componentes del sistema, se muestra un flujo de datos de la programación que realiza la generación de información, transmisión, procesamiento e interacciones.

 
Figura 6. Diagrama de generación de eventos

En el esquema los sensores del dispositivo envían las temperaturas dato de telemetría a una aplicación conectada mediante Azure IoT Central. La aplicación en la nube supervisa las temperaturas y realiza acciones si la temperatura es demasiado baja o alta. Los dispositivos pueden recibir órdenes para ajustar la temperatura o iniciar y detener el funcionamiento. Se tiene un proceso de reserva en caso de que se produzca un error de funcionamiento en un sistema principal o este se quede sin conexión

 
Figura 7. Diagrama de flujo de evento


7.1 Descripción de los componentes.

a.	Sensor: Grove - Temperature & Humidity Sensor (DHT11)
Este dispositivo es un sensor de temperatura y humedad de alta precisión, amplio rango y un bajo costo.

b.	Actuador: Relay Board v1.0
Este actuador utiliza cuatro relés de alta calidad y proporciona interfaces NO/NC que controlan la carga de alta corriente.

c.	Gateway: Terminal Wio ATSAMD51 Core - Dev Board
Este gateway es un microcontrolador con conectividad inalámbrica. Posee varios periféricos multifuncionales y 40 pines GPIO.

d.	Servidor: Azure IoT Central
Este es un aPaaS (Plataforma de aplicaciones como servicio) de Microsoft que se ensambla de los componentes de PaaS de Azure en una plataforma de servicios totalmente administrada para el desarrollo y operaciones de aplicaciones de IoT.

Se opta por esta Plataforma de aplicaciones considerando las ventajas respecto a experiencia de usuario web, simplifica las operaciones, es escalable y segura. 

7.2 Cronograma de implementación propuesto.

En la Tabla X se presenta el cronograma propuesto para el desarrollo del proyecto, se puede ver que se otorga mayor cantidad de tiempo a las tareas de “Desarrollo de la plataforma” y “Pruebas y Optimización” de manera a lograr una respuesta óptima y eficiente en los resultados. A partir de la semana numero 17 en adelante se realiza el monitoreo del sistema.

 
Tabla 2. Cronograma propuesto para la implementación
