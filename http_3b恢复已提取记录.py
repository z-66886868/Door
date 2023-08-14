from GetResult import GetJson


def recoverRecord(webapi):
    """
    恢复已提取记录
    :param webapi:
    :return:
    """
    webapi.logInfo("恢复已提取记录")
    method = "确认已接收记录"

    GetJson.run(method=method, id=3002, lastIndex=0)
