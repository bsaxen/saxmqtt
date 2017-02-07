def setup():
  #read all subscriptions
  with open('list_sub.pscp') as fp:
    for line in fp:
        print line
        #subscribe
 
 
 #do not publish


def loop():
  #read delta subscriptions (use diff , ls *.sub > current-sub-list.txt)
  #subscribe
  #read publish (check if any file *.pub exists, if so, read payload, protoBuffer and publish the message, remove the file!!)
  #publish


