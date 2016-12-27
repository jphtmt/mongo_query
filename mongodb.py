# -*- coding: utf-8 -*-
import sys
from pymongo import MongoClient

def show_collections():
    while 1:
        IP = raw_input("输入需要连接的mongo IP:")
        PORT = int(raw_input("输入mongo 端口："))
        while 1:
            client = MongoClient(host=IP, port=PORT)
            for i in range(len(client.database_names())):
                print "%i.%s  " % (i + 1, client.database_names()[i])
            num = int(raw_input("选择一个database,返回上一步输入 0，退出输入 999："))
            if num != 0 and num != 999:
                db = client[client.database_names()[num - 1]]
                while 1:
                    print "Document:"
                    for i in range(len(db.collection_names())):
                        print "%i.%s  " % (i + 1, db.collection_names()[i])
                    num = int(raw_input("选择一个DOCUMENT,返回上一步输入 0："))
                    if num != 0:
                        while 1:
                            collection = db[db.collection_names()[num-1]]
                            device_id = raw_input("输入要查询的内码，返回上一步输入 0,退出输入 999：")
                            if device_id != '0' and device_id != '999':
                                while 1:
                                    device_id_info = collection.find_one({"dfp": device_id})
                                    if device_id_info is None:
                                        print "不存在此内码"
                                        break
                                    elif device_id_info is not None:
                                        print device_id_info
                                        break
                                continue
                            elif device_id == '0':
                                break
                            elif device_id == '999':
                                sys.exit(0)
                    else:
                        break
            elif num == 0:
                break
            elif num == 999:
                sys.exit(0)


if __name__ == '__main__':
    show_collections()




