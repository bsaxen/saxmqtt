#!/usr/bin/python
#==================================================
# pscp.py
# 2017-02-07 
#==================================================
import os
import paho.mqtt.client as mqtt
import time
from datetime import date
from datetime import datetime
import sys
import generated_proto.messages_pb2 as messages_pb2
import generated_proto.proto_io as ProtoIO
from ioant.utils import utils
from google.protobuf.message import Message
from google.protobuf.descriptor import FieldDescriptor

def pscp_now():
    today = date.today()
    t1 = time.time()
    ts = datetime.fromtimestamp(t1).strftime('%H:%M:%S')
    timestamp = str(today) + " " + ts + " "
    #print today
    #print ts
    return timestamp
  
def pscp_log(info):
    ts = pscp_now()
    print "pscp_log: " + ts + info
    f = open("log.pscp",'a')
    f.write(ts)
    f.write(info)
    f.write('\n')
    f.close()
    return
  
def pscp_subscribe(client, topic)
  tpm = topic.split('-')
  t_top      = tpm[0]
  t_global   = tpm[1]
  t_local    = tpm[2]
  t_clientid = tpm[3]
  t_msgtyp   = tpm[4]
  t_msgindex = tpm[5]
  ttopic = t_top+'/'+t_global+'/'+t_local+'/'+t_clientid+'/'+t_msgtyp+'/'+t_msgindex
  stemp = 'subscribe ' + ttopic
  pscp_log(stemp)
  client.subscribe(topic)

  
def setup():
  #read all subscriptions
  os.system("ls *.sub > list_sub.pscp")
  with open('list_sub.pscp') as fp:
    for line in fp:
        print line
        pscp_subscribe(client,line)
  return 

def loop():
  
  #read delta subscriptions (use diff , ls *.sub > current-sub-list.txt)
  #subscribe
  #read publish (check if any file *.pub exists, if so, read payload, protoBuffer and publish the message, remove the file!!)
  #publish

#====================================
setup()
while True:
  loop()
#====================================
