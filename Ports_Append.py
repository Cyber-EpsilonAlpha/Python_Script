ports = [21, 22, 80, 443]  #listing off ports, for instance, these could be visible ports.
ports.append(8080)  #adding in port 8080 into ports variable.
ports[0] = 2121 #altering the first port in the list.
del ports[1] #removing port 22 from the list.
print(ports) #displaying ports.
