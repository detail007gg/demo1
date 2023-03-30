# dict1={"name":"apple","price":5,"count":6}
# dict2={"color":"red","country":"CN"}
# dict3={**dict1,**dict2}
# print(dict3)

# import threading  # 导入线程控制包
# import logging  # 导入日志管理包
# from time import sleep, ctime  # 导入时间处理包
#
# logging.basicConfig(level=logging.INFO)  # 设置日志格式
# loops = [0, 2]
#
#
# # 继承thread类，重写构造函数
# class myThread(threading.Thread):
#     def __init__(self, func, args, name=''):
#         threading.Thread.__init__(self)
#         self.func = func
#         self.args = args
#         self.name = name
#
#     def run(self) -> None:
#         self.func(*self.args)
#
#
# def loop(nloop, nsec):
#     logging.info('start loop' + str(nloop) + 'at' + ctime())
#     sleep(nsec)
#     logging.info('end loop' + str(nloop) + 'at' + ctime())
#
#
# def main():
#     logging.info("start all at " + ctime())
#     threads = []
#     nloops = range(len(loops))
#     for i in nloops:
#         t = myThread(loop, (i, loops[i]), loop.__name__)
#         print(t)
#         threads.append(t)
#     for i in nloops:
#         threads[i].start()
#     for i in nloops:
#         threads[i].join()
#     logging.info('end all at' + ctime())
#
#
# if __name__ == '__main__':
#     main()
import pytest


def add(a, b):
    return a + b


def div(a, b):
    return a / b


@pytest.mark.parametrize('data1,data2,expect',[(1,2,3),(4,5,9),(7,8,15)])
def test001(data1,data2,expect):
    print("start")
    results=add(data1,data2)
    assert results==expect


# @pytest.mark.parametrize('data1,data2,expect',[(1,2,3),(4,5,9),(7,8,15)])
# def test002(data1,data2,expect):
#     results=div(data1,data2)
#     assert results==expect
#     print("end")


if __name__ == '__main__':
    pytest.main(['-v -s'])
