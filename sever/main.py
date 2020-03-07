#!/usr/bin/python
# -*- coding: UTF-8 -*-
from client.action.get_connections import get_connections_values
from client.database.connection_pool import *
from sever.worker.check_connections import *


def main():
    try:
        conn = get_conn(host='127.0.0.1',
                        user='root',
                        passwd='******',
                        db='world')
        cur = conn.cursor()
        res = {}
        get_connections_values(res, conn)
        check_max_connections(res)
        cur.close()
        conn.close()

    except Exception, exc:
        print(exc)


if __name__ == '__main__':
    main()
