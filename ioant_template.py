#=======================================
# Template for IOANT Python Application
# Date: 2017-02-14
#=======================================
import ioant
#=======================================

topic1 = "live/global/local/clientid/messagetype1/streamindex1"
topic1 = "live/global/local/clientid/messagetype1/streamindex2"
topic1 = "live/global/local/clientid/messagetype2/streamindex"

def setup():
  payload1 = ioantSubscribe(topic1)
  payload2 = ioantSubscribe(topic2)
  return



def loop():
  if payload1.value == payload2.value:
    ioantPublish(topic3,pyload)
  return
  
