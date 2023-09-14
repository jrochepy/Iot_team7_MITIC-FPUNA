from counterfit_connection import CounterFitConnection
from datetime import datetime
from counterfit_shims_seeed_python_dht import DHT
CounterFitConnection.init('127.0.0.1', 5000)

import paho.mqtt.client as mqtt
import json
import time

# Dispositivo DHT11 ... en la posicion indicada "5" lee la humedad y automaticamente en la siguiente, lee la temperatura
sensor = DHT("11", 5) 

# El cliente siempre tiene que ser diferente para cada dispositivo
cliente = 'grupo07iotuna_Equipo_Sensor' 

# Topic, es el elemento en comun al que se suscriben o publican los clientes
canal_temp_lim  = '64f5216971d1e9f79d43cbcb/Temperatura_limite' 
canal_temp      = '64f5216971d1e9f79d43cbcb/Temperatura' 
canal_humedad   = '64f5216971d1e9f79d43cbcb/Humedad'

#Credenciales MQTT MikroDash
mqtt_usuario = "iotgrupo7"
mqtt_pass = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2wiOiI0IiwiZXhwIjoxNzA0MDY2ODE4LCJpYXQiOjE2OTM5NDAwMTgsInVzZXJfaWQiOiI2NGY1MjE2OTcxZDFlOWY3OWQ0M2NiY2IiLCJ1c2VybmFtZSI6IiJ9.GU_CrkqTx-vK42nDSTamvM40ggvbFWL064cpXxy6jfQ"

# Conexion al Servidor
mqtt_client = mqtt.Client(cliente)
mqtt_client.username_pw_set(username= mqtt_usuario, password= mqtt_pass)
mqtt_client.connect('mqtt.mikrodash.com',1883)
print("MQTT connected!") 

# Temperatura limite por defecto
datos_temp_lim = json.dumps({'from' : 'device', 'message' : 'Temperatura_Limite', 'value': 23})
mqtt_client.publish(canal_temp_lim, datos_temp_lim, 1, True)

while True:
    # Se capturan los datos del Sensor
    hum, temp = sensor.read()

    # Se publican los datos de la temperatura
    mqtt_client.publish(canal_temp, json.dumps({'from' : 'device', 'message' : 'Temperatura','save' : True, 'value': '' + str(round(temp)) + ''}), True)
    print("Temperatura:", str(round(temp))," °C" )

    # Se Publican los datos de la humedad
    mqtt_client.publish(canal_humedad, json.dumps({'from' : 'device', 'message' : 'Humedad', 'save' : True, 'value': '' + str(round(hum)) + ''}), True)
    print("Humedad:", str(round(hum))," %")
    
    time.sleep(15)