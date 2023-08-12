from GetResult import GetJson
from Mode_Enum import Mode


def setDoor(webapi, doorNo, mode: Mode, time):
    """
    设置门控制参数
    :param webapi:
    :param doorNo: "门号"
    :param mode:   ”参数 （在线，常开，常闭）使用枚举规范参数“
    :param time: "多少秒后关门"
    :return:
    """
    method = "设置门控制参数"
    webapi.logInfo(method)
    GetJson.run(webapi=webapi, method=method, id=1004, doorNo=doorNo, doorMode=mode.value, doorDelay=time)
