import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Mensagem recebida: " ,str(message.payload.decode("utf-8")))
    print("Topico: ",message.topic)
    print("Mensagem: ",message.qos)
    print("Flag: ",message.retain)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conexao OK")
    else:
        print("Error na conexao")

# Ponha aqui seu ip
broker_address = "192.168.0.10"

# O cliente 1 so publica as informacoes. Ele e o sensor
Cliente_1 = mqtt.Client("1")
# Os clientes 2 e 3 sao "assinantes" do topico umidade e temperatura, respectivamente. Ele apenas leem.
Cliente_2 = mqtt.Client("2")
Cliente_3 = mqtt.Client("3")

Cliente_1.connect(broker_address)
Cliente_2.connect(broker_address)
Cliente_3.connect(broker_address)

Cliente_1.on_message = on_message
Cliente_1.on_connect = on_connect

Cliente_2.on_message = on_message
Cliente_2.on_connect = on_connect

Cliente_3.on_message = on_message
Cliente_3.on_connect = on_connect

Cliente_2.subscribe("Umidade");
Cliente_3.subscribe("Temperatura");

# Escreva o nome do arquivo no campo abaixo
arquivo = open('teste.txt', 'r')

for Linha in arquivo:

   Coluna = Linha.split();
   Umidade = Coluna[1]
   Temperatura_Celsius = Coluna[3]
   Temperatura_Farenheits = Coluna[4]

   print("Topico: Umidade")
   print("Mensagem publicada: "),
   print(Umidade)
   Cliente_1.publish("Umidade", Umidade)

   print("Topico: Temperatura")
   print("Mensagem publicada: "),
   print (Temperatura_Celsius)
   Cliente_1.publish("Temperatura", Temperatura_Celsius)

   time.sleep(2)

time.sleep(4)
Cliente_1.loop_stop()

# Para desligar o broker, basta colocar as seguintes linhas de codigo no terminal:
# sudo service mosquitto stop
