



def getRandomIPv4Address():
    '''Returns random IPv4 Address object from 10.0.0.0 to 10.255.255.255'''
    import random
    import ipaddress
    return ipaddress.IPv4Address(random.randrange(167772160,184549375))

def buildMessageBody():
    
    import uuid
    import random
    import json
    messageBody = json.load(open("wip.json","rb"))
    messageBody.update({"id":str(uuid.uuid1())})
    members = []
    for i in range(random.randrange(10)):
        j = getRandomIPv4Address()
        members.append(j.exploded)
    messageBody['WIP']['members'] = members
    return messageBody

def main():
    import stomp
    import json
    conn = stomp.Connection()
    #conn.set_listener('', MyListener())
    conn.start()
    conn.connect('admin', 'password', wait=True)
    i = 3
    while i > 0:

        conn.send(body=json.dumps(buildMessageBody()), destination='/topic/Loadbalancing.WIP.ADD', content_type="application/json")
        i = i-1
    conn.disconnect()

if __name__ == '__main__':
    main()

