from GetResult import GetJson


def checkTime(webapi):
    """
    校验时间
    :param webapi:
    :return:
    """
    method = "设置日期时间"
    webapi.logInfo(method)

    GetJson.run(method=method, id=1003)

