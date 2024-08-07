#!/usr/bin/env python

"""
Copyright (c) 2006-2024 fsqli developers (https://fsqli.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.enums import PRIORITY

__priority__ = PRIORITY.HIGHEST

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Replaces instances of UNION ALL SELECT with UNION SELECT counterpart

    >>> tamper('-1 UNION ALL SELECT')
    '-1 UNION SELECT'
    """

    return payload.replace("UNION ALL SELECT", "UNION SELECT") if payload else payload
