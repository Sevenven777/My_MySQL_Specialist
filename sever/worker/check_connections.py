#!/usr/bin/python
# -*- coding: UTF-8 -*-
from advise import *


def check_max_connections(res):
    """
    {'action': 'CheckConnections', 'body': {'innodb_buffer_pool_size': 25769803776, 'max_connections': 3000},
     'is_success': True}

    建议每G内存分配最少200个连接，最大350个连接，合理值每G内存300个连接
    """
    """
        In [1]: 1024 / 200.0
        Out[1]: 5.12

        In [2]: 1024 / 300.0
        Out[2]: 3.4133333333333336

        In [3]: 1024 / 400.0
        Out[3]: 2.56
    """
    max_connections = res['max_connections']
    innodb_buffer_pool_size = res['innodb_buffer_pool_size']
    innodb_buffer_pool_size_in_M = innodb_buffer_pool_size / 1024 / 1024.0
    low, up = innodb_buffer_pool_size_in_M / 5.12, innodb_buffer_pool_size_in_M / 2.56
    recommend = innodb_buffer_pool_size_in_M / 3.41

    if max_connections < low or max_connections > up:
        Advise.max_connection_warning.format(max_connections, innodb_buffer_pool_size_in_M,
                                             int(low), int(up), int(recommend))

    print("您的数据库连接数是{0}，你的buffer pool大小是{1}M，建议您的数据库连接数设置在{2}~{3}范围内，也可以直接设置为{4} ".format(max_connections,
                                                                                          innodb_buffer_pool_size_in_M,
                                                                                          int(low), int(up),
                                                                                          int(recommend)))
