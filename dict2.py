crudQueries = [
  ["INS_OR_UPD", "KEY1", "KEY2", "5"],
  ["INS_OR_UPD", "KEY1", "KEY2", "6"],
  ["INS_OR_UPD", "KEY3", "KEY2", "7"],
  ["SELECT", "KEY1", "KEY2"],
  ["SELECT", "KEY1", "KEY3"],
  ["DELETE", "KEY1", "KEY2"],
  ["DELETE", "KEY1", "KEY2"]
];

dataDict={}
outputList=[]

def myFunction():
    for query in crudQueries:
        if(query[0]=='INS_OR_UPD'):
            tempDict={query[2]:query[3]}
            dataDict[query[1]]=tempDict
            outputList.append(query[3])
        if(query[0]=='SELECT'):
            outputList.append(query[2])
        if(query[0]=='DELETE'):
            value=dataDict.pop(query[1],None) #If key is not present, then also no error
            outputList.append(value)
    return outputList,dataDict

outputList, dataDict=myFunction()
print(outputList,dataDict)