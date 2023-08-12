from WgWebapi import WgWebapi
from GetResult import GetJson


# 远程开门
def getPrivsTotal(webapi):
    """
    权限总数读取
    :return:
    """
    method = "权限总数读取"
    webapi.logInfo(method)

    strResult, _, _ = GetJson.run(method=method, id=1004)

    webapi.logInfoInJson(strResult)