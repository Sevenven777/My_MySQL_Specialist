#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging

import pandas as pd

LOG = logging.getLogger(__name__)

def get_connections_values(res, conn):
    sql_cmd1 = "show variables like '%max_connections%';"
    sql_cmd2 = "show global variables like 'innodb_buffer_pool_size';"
    max_connections_table = pd.read_sql(sql_cmd1, conn)
    innodb_buffer_pool_size = pd.read_sql(sql_cmd2, conn)
    res['max_connections'] = int(max_connections_table.ix[[0]].values[0][1])
    res['innodb_buffer_pool_size'] = int(innodb_buffer_pool_size.ix[[0]].values[0][1])

    return
