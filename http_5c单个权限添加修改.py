from GetResult import GetJson


def updatePrivs(webapi, cardNumber):
    """
    权限添加或修改
    :param webapi:
    :param cardNumber: 要修改的卡号
    :return:
    """
    method = "权限添加或修改"
    webapi.logInfo(method)


    startTime = "2022-05-10 00:00:00"
    endTime = "2099-12-31 23:59:59"

    privs = [{
        "卡号": [cardNumber],
        "起始日期时间": startTime,
        "截止日期时间": endTime,
        "1号门控制时段": 1,
        "2号门控制时段": 1,
        "3号门控制时段": 1,
        "4号门控制时段": 1,
        "用户密码": 0
    }]

    strResult, _, _ = GetJson.run(method=method, id=4001, arrPrivs=privs)
    webapi.logInfoInJson(strResult)
