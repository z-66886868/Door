import json

from GetResult import GetJson


def checkState(webapi):
    """
    查看控制器状态
    :param webapi:
    :return:
    """
    method = "查询控制器状态"
    webapi.logInfo(method)
    # 执行方法
    (strResult, controllerSN, success) = GetJson.run(method=method, id=1002)

    if success:
        result = json.loads(strResult)['result']
        if result is not None:
            controllerInfo = result['控制器信息']
            info = ''
            info += "控制器时间 = " + controllerInfo['时间'] + "\r\n"
            info += "1号门状态 = " + controllerInfo['1号门'] + "\r\n"
            if controllerSN > 200000000:
                info += "2号门状态 = " + controllerInfo['2号门'] + "\r\n"
            if controllerSN > 400000000:
                info += "3号门状态 = " + controllerInfo['3号门'] + "\r\n"
                info += "4号门状态 = " + controllerInfo['4号门'] + "\r\n"
            webapi.logInfo(info)

            arrDoor = controllerInfo['最近六条记录']
            print("最近六条数据")
            for (i, item) in enumerate(arrDoor):
                info = ''
                if i == 0:
                    info += '最新的一条记录\r\n'
                info += "索引位 = " + str(item['索引位']) + "\r\n"
                info += "时间 = " + str(item['时间']) + "\r\n"
                info += "描述 = " + str(item['描述']) + "\r\n"
                info += "卡号 = " + str(item['卡号']) + "\r\n"
                info += "门号 = " + str(item['门号']) + "\r\n"
                info += "进出 = " + str(item['进出']) + "\r\n"
                info += "有效 = " + str(item['有效']) + "\r\n"

                if len(info) != 0:
                    webapi.logInfo(info)
