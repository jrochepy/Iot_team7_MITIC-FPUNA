import paho.mqtt.client as mqtt
import json
import time

from counterfit_shims_grove.grove_relay import GroveRelay
from os import path
from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5000)

# Declaracion del relé en el puerto 4
rele = GroveRelay(4)
limite = 23

#Parametros de conexion MQTT con MikroDash
mqtt_servidor = 'mqtt.mikrodash.com'
mqtt_puerto = 1883
nivel_qos = 2  #Calidad del servicio MQTT -> 0=lanzar y olvidar. 1=entregado al menos una vez(puede haber duplicados). 2= entrega exactamente una vez (4 pasos, no hay duplicados).

#Credenciales MQTT MikroDash
mqtt_usuario = "iotgrupo7"
mqtt_pass = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2wiOiI0IiwiZXhwIjoxNzA0MDY2ODE4LCJpYXQiOjE2OTM5NDAwMTgsInVzZXJfaWQiOiI2NGY1MjE2OTcxZDFlOWY3OWQ0M2NiY2IiLCJ1c2VybmFtZSI6IiJ9.GU_CrkqTx-vK42nDSTamvM40ggvbFWL064cpXxy6jfQ"

# El cliente siempre tiene que ser diferente para cada dispositivo
cliente = 'grupo07iotuna_Equipo_Rele' 

# Topic, es el elemento en comun al que se suscriben o publican los clientes
canal_temp_lim      = '64f5216971d1e9f79d43cbcb/Temperatura_limite' 
canal_temp          = '64f5216971d1e9f79d43cbcb/Temperatura' 
canal_interruptor   = '64f5216971d1e9f79d43cbcb/Interruptor'

mqtt_client = mqtt.Client(cliente)
mqtt_client.username_pw_set(username= mqtt_usuario, password= mqtt_pass)
mqtt_client.connect(mqtt_servidor, mqtt_puerto)

mqtt_client.loop_start()

def handle_telemetry(client, userdata, message):
    payload = json.loads(message.payload.decode())
    global limite

    if payload['from'] == 'device': # Si es enviado desde un dispositivo (codigo en python)
        if payload['message'] == 'Temperatura_Limite':
            limite = int(payload['value']) # se obtiene el valor del límite
            print('Limite: ' + str(payload['value']))

        if payload['message'] == 'Temperatura': # Se evalua solo si se recibe temperatura
            print('Temperatura:', str(payload['value']), " °C")
            if int(payload['value']) > limite: # Si la temperatura es mayor al limite se enciende el interruptor y el relé
                rele.on()
                mqtt_client.publish(canal_interruptor, json.dumps({'from' : 'device', 'message' : 'Interruptor', 'value': True}), nivel_qos, True)
                print('Interruptor: Prendido')
            else:# Si la temperatura es menor al limite se apaga el interruptor y el relé
                rele.off()
                mqtt_client.publish(canal_interruptor, json.dumps({'from' : 'device', 'message' : 'Interruptor', 'value': False}), nivel_qos, True)
                print('Interruptor: Apagado')
    else: # payload['from'] == 'app'
        if payload['message'] == 'Hola desde MikroDash':
            if type(payload['value']) == type(True): # Si es booleano es desde el interruptor
                if bool(payload['value']):
                    rele.on()
                    mqtt_client.publish(canal_interruptor, json.dumps({'from' : 'device', 'message' : 'Interruptor', 'value': True}), nivel_qos, True)
                    print('Interruptor: Prendido')
                else:
                    rele.off()
                    mqtt_client.publish(canal_interruptor, json.dumps({'from' : 'device', 'message' : 'Interruptor', 'value': False}), nivel_qos, True) 
                    print('Interruptor: Apagado')
            else: # Si es numerico es desde el sensor analogico se cambia la temperatura limite
                mqtt_client.publish(canal_temp_lim, json.dumps({'from' : 'device', 'message' : 'Temperatura_Limite', 'value': int(payload['value'])}), nivel_qos, True)

#Topics a los que se suscribira para recibir cambios
mqtt_client.subscribe(canal_temp_lim, nivel_qos)
mqtt_client.subscribe(canal_temp, nivel_qos)
mqtt_client.subscribe(canal_interruptor, nivel_qos)
mqtt_client.on_message = handle_telemetry

while True:
    time.sleep(10)