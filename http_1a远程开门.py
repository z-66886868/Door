from GetResult import GetJson


# 远程开门
def openDoor(webapi, doorNo):
    method = "远程开门"
    webapi.logInfo(method)

    strResult, _, _ = GetJson.run(method=method, id=1001, doorNo=doorNo)

    webapi.logInfoInJson(strResult)
