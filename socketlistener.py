import socket
s = socket.socket()         
s.bind(('0.0.0.0', 8090 ))
s.listen(0) 
distance_1=0
distance_2=0   
enterance_width=8000
carwidth=0  
# count=0          
while True:
    client, addr = s.accept()
    while True:
        content = client.recv(32)
        if len(content) ==0:
           break
        else:
            # print("in python")
            # print(content)
            res=[int(i) for i in content.split() if i.isdigit()]
            # res.remove(1)
            # res.remove(2)
            # distance_1=res[0]
            # distance_2=res[1]
            # print(res)
            if(len(res)!=0):
                distance_1=res[0]
                distance_2=res[1]
            # print(distance_1)
            # print(distance_2)
            carwidth=enterance_width-(distance_1+distance_2)
            with open('readme.txt', 'w') as f:
                f.write(str(carwidth))
    print("Closing connection")
    client.close()