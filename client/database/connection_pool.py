#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb as db
from check_args import *

LOG = logging.getLogger(__name__)

@check_required_args(['user', 'passwd', 'host'])
def get_conn(**kwargs):
    return db.connect(host=kwargs.get('host', 'localhost'),
                      user=kwargs.get('user'),
                      passwd=kwargs.get('passwd'),
                      port=kwargs.get('port', 3306),
                      db=kwargs.get('db'))
