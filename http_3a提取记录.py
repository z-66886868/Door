import json

from GetResult import GetJson


# 提取记录
def getRecord(webapi):
    """
    提取记录
    :param webapi:
    :return:
    """
    webapi.logInfo("准备提取...")
    method = "提取记录"
    newestIndex = -1
    bFinished = False

    strResult, _, _ = GetJson.run(method=method, id=3001, maxNum=1000, newestIndex=newestIndex)

    arrSwipeRecords = []

    result = json.loads(strResult)['result']
    getNum = result['提取记录数']
    if getNum > 0:
        newestIndex = result['最后记录索引']
        datas = result['记录信息']
        for data in datas:
            info = f"索引位：{data['索引位']} 时间：{data['时间']} 描述：{data['描述']} 卡号：{data['卡号']} 门号：{data['门号']} 进出：{data['进出']} 有效：{data['有效']}"
            arrSwipeRecords.append(info)

    if getNum < 1000:
        webapi.logInfo(f"记录数: {getNum}, 最后记录索引: {newestIndex}")
        bFinished = True

    # 删除已取记录
    if bFinished:
        if newestIndex > 0:
            method = "确认已接收记录"
            strResult, _, _ = GetJson.run(method=method, id=3002, newestIndex=newestIndex)

        webapi.logInfo("显示最后20条记录....")
        start = 0
        if len(arrSwipeRecords) > 20:
            start = len(arrSwipeRecords) - 20

        while start < len(arrSwipeRecords):
            webapi.logInfoWithTime(str(arrSwipeRecords[start]), False)
            start += 1
