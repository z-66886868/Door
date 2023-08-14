import json

from GetResult import GetJson


def getTimeFrame(webapi):
    """
    提取时段
    :param webapi:
    :return:
    """
    method = "提取时段"
    webapi.logInfo(method)

    strResult, _, success = GetJson.run(method=method, id=4005)
    results = json.loads(strResult)['result']
    timeFrameTotal = results['提取时段数']
    timeFrame = results['记录信息']
    if success:
        start = 0
        if timeFrameTotal > 20:
            start = len(timeFrame) - 20

        print('显示最后20条信息：')
        while start < timeFrameTotal:
            webapi.logInfoWithTime(str(timeFrame[start]), False)
            start += 1
