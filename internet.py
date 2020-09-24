import socket
import wikipedia





def check_connection():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False
    
    
def ipaddress():
    ip = socket.gethostbyname(socket.gethostname())
    if ip == "127.0.0.1":
        return False
    
    else:
        print(ip)
        return True


def check_wiki(query):

    query = query.lower()
    query.replace("who is","")
    query.replace("what is","")
    query.replace("tell me","")
    query.replace("tell me about","")
    query.replace("tell me who is","")
    query.replace("tell me what is","")
    query.replace("do you know","")
    query.replace("do you know who is","")
    query.replace("do you know what is","")
    query.replace("do you know about","")

    try:
        data = wikipedia.summary(query, sentences=2)
        return data
    
    except:
        return ""

#def wifi_pass():

 #   a = subprocess.check_output([wlan','show','profiles']).decode('utf-8').split('\n')
  #  a = [i.split(":"[1][1:-1]) for i in a if "All User Profile" in i ]
   # for i in a:
    #    results = subprocess.check_output(['netsh','wlan','show','profiles',i , 'key=clear']).decode('utf-8').split('\n')
      #  results = [b.split(":")[1][1:-1] for b in results if "key content " in b ]
#       try:
 #           print ("{:<30}| {:<}".format(i,results[0]))
  #          
   #     except:
    #        print ("{:<30}| {:<}".format(i,""))

    
        

