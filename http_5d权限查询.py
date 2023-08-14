from GetResult import GetJson


def queryPrivs(webapi, cardNumber):
    """
    权限查询
    :param webapi:
    :param cardNumber: 要查询的卡号
    :return:
    """
    method = "权限查询"
    webapi.logInfo(method)

    strResult, _, _ = GetJson.run(method=method, id=4003, cardNumber=[cardNumber])

    webapi.logInfoInJson(strResult)
