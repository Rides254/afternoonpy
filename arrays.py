
devices=["computer","phone","laptop"]
print(devices)
#Accessing an element
print(devices[1])

#looping through elements in an arrey
for dev in devices:
    print(dev)

#Adding an element
devices.append("tablet")
print(devices)

#Removing an element
devices.remove("computer")
print(devices)