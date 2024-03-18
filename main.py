import paho.mqtt.client as mqtt
#biblioteca

def ao_conectar(client, userdata, flags, rc):
#criar uma função, as coisas q a função tem q receber pra ela funcionar
    print("Nos conectamos com o seguinte código de resultado {}".format(str(rc)))
#{} vai substituir pelo format bla bla bla (vai retornar um codigo)

def ao_receber(client, userdata, msg):
    print("{} --- {}".format(msg.topic, str(msg.payload)))
    #nome do topico e a mensagem q ele ta trazendo 
