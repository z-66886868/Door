from http_1a远程开门 import openDoor
from http_2a查询控制器状态 import checkState
from http_2b校准时间 import checkTime
from http_3a提取记录 import getRecord
from http_3b恢复已提取记录 import recoverRecord
from http_3c提取记录_指定时间范围_当天记录 import getRecordTime
from http_4ab设置门控制参数 import setDoor
from http_4c读取门控制参数 import getStart
from http_5a上传全部权限1万人 import uploadPrivs
from http_5b权限总数读取 import getPrivsTotal
from http_5c单个权限添加修改 import updatePrivs
from http_5d权限删除 import deletePrivs
from http_5d权限查询 import queryPrivs
from http_6提取权限 import getPrivs

from WgWebapi import WgWebapi


