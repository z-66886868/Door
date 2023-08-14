from GetResult import GetJson


def openDoor(webapi, doorNo):
    """
    远程开门
    :param webapi:
    :param doorNo: 门号
    :return:
    """
    method = "远程开门"
    webapi.logInfo(method)
    strResult, _, _ = GetJson.run(method=method, id=1001, doorNo=doorNo)

    webapi.logInfoInJson(strResult)
