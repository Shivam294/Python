dataDict ={}

def createDict(key, value):
    dataDict[key]=value
    print(f"Add key: {key} with value: {value}")

def readDict(key):
    if key in dataDict:
        return dataDict[key]
    else:
        print(f"Key: {key} not found!")

def updateDict(key, value):
    if key in dataDict:
        dataDict[key]=value
        print(f"Updated key: {key} with value: {value}")
    else:
        print(f"Key: {key} not found!")

def deleteDict(key):
    if key in dataDict:
        del dataDict[key]
        print(f"Deleted key: {key}")
    else:
        print(f"Key: {key} not found!")

createDict("name","John")
print(readDict("name"))
updateDict("name", "Jane")
print(readDict("name"))
deleteDict("name")