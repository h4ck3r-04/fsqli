#!/usr/bin/env python

"""
Copyright (c) 2006-2024 fsqli developers (https://fsqli.org/)
See the file 'LICENSE' for copying permission
"""

try:
    import _mssql
    import pymssql
except:
    pass

import logging

from lib.core.common import getSafeExString
from lib.core.convert import getText
from lib.core.data import conf
from lib.core.data import logger
from lib.core.exception import FsqliConnectionException
from plugins.generic.connector import Connector as GenericConnector

class Connector(GenericConnector):
    """
    Homepage: http://pymssql.sourceforge.net/
    User guide: http://pymssql.sourceforge.net/examples_pymssql.php
    API: http://pymssql.sourceforge.net/ref_pymssql.php
    Debian package: python-pymssql
    License: LGPL

    Possible connectors: http://wiki.python.org/moin/SQL%20Server

    Important note: pymssql library on your system MUST be version 1.0.2
    to work, get it from http://sourceforge.net/projects/pymssql/files/pymssql/1.0.2/
    """

    def connect(self):
        self.initConnection()

        try:
            self.connector = pymssql.connect(host="%s:%d" % (self.hostname, self.port), user=self.user, password=self.password, database=self.db, login_timeout=conf.timeout, timeout=conf.timeout)
        except (pymssql.Error, _mssql.MssqlDatabaseException) as ex:
            raise FsqliConnectionException(ex)
        except ValueError:
            raise FsqliConnectionException

        self.initCursor()
        self.printConnected()

    def fetchall(self):
        try:
            return self.cursor.fetchall()
        except (pymssql.Error, _mssql.MssqlDatabaseException) as ex:
            logger.log(logging.WARN if conf.dbmsHandler else logging.DEBUG, "(remote) '%s'" % getSafeExString(ex).replace("\n", " "))
            return None

    def execute(self, query):
        retVal = False

        try:
            self.cursor.execute(getText(query))
            retVal = True
        except (pymssql.OperationalError, pymssql.ProgrammingError) as ex:
            logger.log(logging.WARN if conf.dbmsHandler else logging.DEBUG, "(remote) '%s'" % getSafeExString(ex).replace("\n", " "))
        except pymssql.InternalError as ex:
            raise FsqliConnectionException(getSafeExString(ex))

        return retVal

    def select(self, query):
        retVal = None

        if self.execute(query):
            retVal = self.fetchall()

            try:
                self.connector.commit()
            except pymssql.OperationalError:
                pass

        return retVal
