import json
from GetResult import GetJson


def getPrivs(webapi):
    """
    提取权限
    :param webapi:
    :return:
    """
    method = "权限总数读取"
    webapi.logInfo(method)

    strResult, _, _ = GetJson.run(webapi=webapi, method=method, id=4003)

    privsTotal = json.loads(strResult)['result']['权限总数']

    if privsTotal > 0:
        timeout = 3000
        if privsTotal > 600:
            timeout += (privsTotal * 5)
            print(f"提取权限，大概需要{privsTotal * 5 /1000}秒左右")

        strResult, _, _ = GetJson.run(webapi=webapi, method='提取权限', id=4005, timeout=timeout)

        arrPrivs = json.loads(strResult)['result']['记录信息']
        start = 0
        arrPrivsLen = len(arrPrivs)
        print(f'提取权限数:{arrPrivsLen}')
        print("显示最后20条权限:")
        if arrPrivsLen > 20:
            start = arrPrivsLen - 20

        while start < arrPrivsLen:
            webapi.logInfoWithTime(str(arrPrivs[start]), False)
            start += 1
