#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals


class Advise(object):
    max_connection_warning = "数据库连接数过多容易造成线程频繁的上下文切换，连接数过少不能充分发挥数据库的性能，您的数据库连接数是{0}，你的buffer pool大小是{" \
                             "1}，建议您的数据库连接数设置在{2}~{3}范围内，也可以直接设置为{4} "
