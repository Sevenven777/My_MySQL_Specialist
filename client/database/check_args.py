#!/usr/bin/python
# -*- coding: UTF-8 -*-
import functools
import inspect
import logging

LOG = logging.getLogger(__name__)

def check_required_args(self):
    """check parameters of action"""

    def decorated(f):
        """decorator"""

        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            """wrapper"""
            func_args = inspect.getcallargs(f, *args, **kwargs)
            kwargs = func_args.get('kwargs')
            for item in self:
                if kwargs.get(item) is None:
                    message = "check required args failed, `{0}` is not found in {1}".format(item, f.__name__)
                    raise Exception(message)

            return f(*args, **kwargs)

        return wrapper

    return decorated
