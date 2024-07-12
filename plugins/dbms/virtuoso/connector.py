#!/usr/bin/env python

"""
Copyright (c) 2006-2024 fsqli developers (https://fsqli.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.exception import FsqliUnsupportedFeatureException
from plugins.generic.connector import Connector as GenericConnector

class Connector(GenericConnector):
    def connect(self):
        errMsg = "on Virtuoso it is not (currently) possible to establish a "
        errMsg += "direct connection"
        raise FsqliUnsupportedFeatureException(errMsg)
