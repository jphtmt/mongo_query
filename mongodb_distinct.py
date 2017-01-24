# -*- coding: utf-8 -*-

import sys
from pymongo import MongoClient
from mongodb import connect_info


def data_distinct():
    while 1:
        ip, port = connect_info()
        while 1:
            client = MongoClient(host=ip, port=port)
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
                            collection = db[db.collection_names()[num - 1]]
                            print "1. IMEI " \
                                  "2. IMSI " \
                                  "3. cellularIP " \
                                  "4. cpuABI " \
                                  "5. sdkVersion " \
                                  "6. wifiMacAddress " \
                                  "7. IDFA " \
                                  "8. displayRom "
                            choose_num = int(raw_input("输入要筛选的字段，返回上一步输入 0,退出输入 999："))
                            if choose_num != 0 and choose_num != 999:
                                while 1:
                                    if choose_num == 1:
                                        distinct_info = collection.distinct('IMEI')
                                    elif choose_num == 2:
                                        distinct_info = collection.distinct('IMSI')
                                    elif choose_num == 3:
                                        distinct_info == collection.distinct('cellularIP')
                                    elif choose_num == 4:
                                        distinct_info == collection.distinct('cpuABI')
                                    elif choose_num == 5:
                                        distinct_info == collection.distinct('sdkVersion')
                                    elif choose_num == 6:
                                        distinct_info == collection.distinct('wifiMacAddress')
                                    elif choose_num == 7:
                                        distinct_info == collection.distinct('IDFA')
                                    elif choose_num == 8:
                                        distinct_info == collection.distinct('displayRom')
                                    elif distinct_info is not None:
                                        print distinct_info
                                        break
                                continue
                            elif choose_num == '0':
                                break
                            elif choose_num == '999':
                                sys.exit(0)
                    else:
                        break
            elif num == 0:
                break
            elif num == 999:
                sys.exit(0)


if __name__ == '__main__':
    data_distinct()