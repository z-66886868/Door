from GetResult import GetJson


def uploadFrameTime(webapi):
    """
    上传全部有用时段
    :param webapi:
    :return:
    """
    method = "上传全部有用时段"
    webapi.logInfo(method)
    startTime = "2022-05-10"
    endTime = "2099-12-31"
    params = []
    timesNum = 10
    for i in range(timesNum):
        i += 2
        param = {
            "时段号": i,
            "起始日期": startTime,
            "截止日期": endTime,
            "星期一": 1,
            "星期二": 1,
            "星期三": 1,
            "星期四": 1,
            "星期五": 1,
            "星期六": 1,
            "星期日": 1,
            "时区一的起始时间": "08:30",
            "时区一的截止时间": "12:00",
            "时区二的起始时间": "14:00",
            "时区二的截止时间": "17:30",
            "时区三的起始时间": "00:00",
            "时区三的截止时间": "00:00",
            "下一个链接时段": 0
        }
        params.append(param)

    timeout = 3000
    if timesNum > 10:
        timeout = timesNum * 200 + timeout
        print(f"大约需要{timeout / 1000}秒左右")

    strResult, _, _ = GetJson.run(method=method, id=5001, timeFrame=params, timeout=timeout)

    webapi.logInfoInJson(strResult)
