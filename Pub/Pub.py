import time
import os
from datetime import datetime


# import paho.mqtt.client as mqtt 
# from random import randrange, uniform




# flag_connected = 0

# def on_connect():
# 	flag_connected = 1

# def on_disconnect():
# 	flag_connected = 0

# def on_connect(client, userdata, flags, rc):
# 	print(" --------------------- on_connect ------------------")
# 	if rc==0:
# 		client.connected_flag=True
# 		print("connected OK")
# 	else:
# 		client.connected_flag=False
# 		print("Bad connection Returned code=",rc)


# mqttBroker ="192.168.1.61" 
# client = mqtt.Client()
# mqtt.Client.connected_flag=False
# client.on_connect = on_connect




SavedWhenDisconnected = " "

# client.loop_start()
LostConnection = 0


while 1:
    file =  open('putty.txt', 'r')
    data = file.read()
    words = data.split("\n") 
    toSend =  datetime.now().strftime("%d/%m/%Y %H:%M:%S ") + words[len(words)-2]
    # toSend = words[len(words)-2]
    # print(toSend) 
    toSendFinal = " "
    if SavedWhenDisconnected == " ":
    	toSend = toSend
    	# toSendFinal = '-----------\n "{}" \n-----------'.format(toSend)
    else:
    	toSend = SavedWhenDisconnected + "NewLine" + toSend
    	
		# toSendFinal = '-----------\n "{}" \n-----------'.format(toSend)
    
    print(toSend)
    command = 'cmd /c "mosquitto_pub -p 1881 -t TEXT -m "{}""'.format(toSend)
    # print(command)
    a = os.system(command) 
    if a == 1:
        LostConnection = 1
        SavedWhenDisconnected = toSend 
        # + "NewSaved"
        
    elif a == 0 and LostConnection == 0 :
        SavedWhenDisconnected = " "
    elif a == 0 and LostConnection == 1:
        LostConnection = 0
        # LostConnection = 0
    

    # client.connect(mqttBroker,1881) 
    # client.publish("TEXT", toSend)
    

    # if(client.connected_flag):
    # 	if SavedWhenDisconnected == ".." :
    # 		client.publish("TEXT", toSend)
    # 		print("published: ")
    # 		print(toSend)
    # 	else:
    # 		client.publish("TEXT", SavedWhenDisconnected + "\n" +toSend)
    # 		SavedWhenDisconnected = ".."
    # 		print("published after disconnect: ")
    # 		print(SavedWhenDisconnected + "\n" +toSend)
    # else:
    # 	SavedWhenDisconnected = SavedWhenDisconnected + "\n" + toSend
    # 	print("flag is zero")
    
    # time.sleep(2)

    time.sleep(10)

# client.loop_stop()
    


