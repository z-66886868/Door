from GetResult import GetJson


def deletePrivs(webapi, cardNum):
    """
    权限删除
    :param webapi:
    :param cardNum: 要删除的卡号
    :return:
    """
    method = "权限删除"
    webapi.logInfo(method)

    privs = [{
        "卡号": [cardNum],
    }]

    strResult, _, _ = GetJson.run(webapi=webapi, method=method, id=4002, arrPrivs=privs)
    webapi.logInfoInJson(strResult)
