from GetResult import GetJson
from WgWebapi import WgWebapi


def uploadPrivs(webapi):
    """
    上传全部权限
    :param webapi:
    :return:
    """
    method = "上传全部权限"
    webapi.logInfo(method)

    arrPrivs = []
    cardNoStart = 1230001  # 起始卡号
    total = 10000  # 总卡数
    startTime = "2022-05-10 00:00:00"
    endTime = "2099-12-31 23:59:59"
    for i in range(total):
        privs = {
            "卡号": [cardNoStart],
            "起始日期时间": startTime,
            "截止日期时间": endTime,
            "1号门控制时段": 1,
            "2号门控制时段": 1,
            "3号门控制时段": 1,
            "4号门控制时段": 1,
            "用户密码": 0
        }
        arrPrivs.append(privs)
        cardNoStart += 1

    timeout = 3000
    if len(arrPrivs) > 1000:
        timeout += (len(arrPrivs) * 4)

    strResult, _, _ = GetJson.run(method=method, id=4004, timeout=timeout, arrPrivs=arrPrivs)

    webapi.logInfoInJson(strResult)
