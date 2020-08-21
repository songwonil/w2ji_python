import struct

# writing data
age = 27              # int
height = 175.2      # float
weight = 71.3       # float

#data = struct.pack('idd',age,height,weight)
'''
f = open('teet.bin','wb')
f.write(data)
f.close()
'''
# reading data
f = open('teet.bin','rb')
data = f.read()
print(data)
#(age,height,weight) = struct.unpack('idd',data)