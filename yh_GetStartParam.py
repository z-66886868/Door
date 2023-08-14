from GetResult import GetJson


# 远程开门
def getDoorParam(webapi):
    """
    读取门控制参数
    :param webapi:
    :return:
    """
    method = "读取门控制参数"
    webapi.logInfo(method)

    strResult, _, _ = GetJson.run(method=method, id=1004)

    webapi.logInfoInJson(strResult)
