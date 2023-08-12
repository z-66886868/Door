import json

from GetResult import GetJson
from WgWebapi import WgWebapi


def getRecordTime(webapi, startTime, endTime):
    """
    提取记录_指定时间范围_当天记录
    时间格式：yyyy-MM-dd HH:mm:ss
    :param webapi:
    :param startTime: 开始时间
    :param endTime: 结束时间
    :return:
    """
    webapi = WgWebapi()
    webapi.logInfo("准备提取...")
    method = "提取记录"
    newestIndex = -1

    strResult, _, _ = GetJson.run(method=method, id=3001, maxNum=1000, newestIndex=newestIndex,startTime=startTime,endTime=endTime)

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

    for arrSwipeRecord in arrSwipeRecords:
        print(arrSwipeRecord)
