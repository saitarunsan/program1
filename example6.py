data2 = {'A':1,'B':3}
try:
    print(data2['C'])
except KeyError as k:
    print(k,'key error has occured as not present in the dictionery')




