import random
import sqlite3
from paho.mqtt import client as mqtt_client
import datetime
from dateutil import parser
con = sqlite3.connect('db.sqlite3')
cur = con.cursor()
broker = 'test.mosquitto.org'
port = 1883
topic = "IUT/Colmar/SAE24/Maison1"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'
cmd2 = "INSERT OR IGNORE INTO mySAE24_capteur VALUES (? , ? ,  ? , ? );"
cmd3 = "INSERT INTO mySAE24_data (temp,capteur_id,timestamp) VALUES ( ? ,  ? , ? );"
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(msg.payload.decode())
        message = msg.payload.decode()
        temp =  message.replace("=",",")
        temp = temp.split(",")
        dic = []
        for i in range(0,len(temp)):
           if (i % 2) == 0:
               pass
           else:
               dic = dic + [temp[i]]
        print(dic)
        date = parser.parse(str(dic[2]+" "+dic[3]))
        cur.execute(cmd2,(str(dic[0]),dic[1],dic[1],dic[1]))
        cur.execute(cmd3,(dic[4],dic[0],date))
        con.commit()
    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()