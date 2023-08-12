import json

from WgWebapi import WgWebapi


class GetJson:
    webapi = WgWebapi()

    @classmethod
    def run(cls, method, id, timeout=3000, doorNo='', maxNum='', newestIndex='', lastIndex='', startTime='', endTime='',
            doorMode='',
            doorDelay='', cardNumber='', arrPrivs=''):
        """
        除了method 和 id 外都可为空
        :param method: 要执行的方法
        :param id: id号
        :param timeout: 请求超时时间
        :param doorNo: 门号
        :param maxNum: 每次提取记录数量
        :param newestIndex 已取记录的最后记录索引
        :param lastIndex 最后记录索引
        :param startTime 开始时间
        :param endTime 结束时间
        :param doorMode 控制方式 （在线，常开，常闭
        :param doorDelay 开门延时(秒)  开门后多少秒后关门
        :param cardNumber: 卡号
        :param arrPrivs 权限
        :return: 请求后的结果 和 序列号
        """
        success = ''
        controllerSN = cls.webapi.getControllerSN()
        url = cls.webapi.getUrl()
        parameter = {
            "jsonrpc": "2.0",
            "method": method,
            "id": id,
            "params": [
                {
                    "设备序列号": controllerSN,
                    "门号": doorNo,
                    "每次提取记录数量": maxNum,
                    "已取记录的最后记录索引": newestIndex,
                    "最后记录索引": lastIndex,
                    "起始日期时间": startTime,
                    "截止日期时间": endTime,
                    "控制方式": doorMode,
                    "开门延时(秒)": doorDelay,
                    "卡号": cardNumber,
                    "权限": arrPrivs
                }
            ]
        }

        body = json.dumps(parameter)

        # print(parameter)

        strResult = cls.webapi.PushToWebWithjson(url, body, timeout)

        if len(strResult) == 0:
            cls.webapi.logInfo("通讯失败")
        else:
            success = cls.webapi.successIsTrue(strResult)
            if success:
                cls.webapi.logInfo(f"{controllerSN} {method} 成功.")
            else:
                cls.webapi.logInfo(f"{controllerSN} {method} 失败...")

        return strResult, controllerSN, success
