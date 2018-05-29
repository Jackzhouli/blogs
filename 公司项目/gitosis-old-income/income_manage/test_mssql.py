import pyodbc

#2018.04.24.    us pyodbc success.
#connection = pyodbc.connect(
#    'DRIVER={SQL Server Native Client 11.0};SERVER=10.105.228.83;DATABASE=DJANGO_TEST;UID=sa;PWD=Q!$Sb8t&p@bX')
#connection = pyodbc.connect(
#    'DRIVER={SQL Server Native Client 11.0};SERVER=192.168.1.40;DATABASE=DJANGO_TEST_DB;UID=wikitec_dcc;PWD=3bRiRBYKyccbzOFJC7Xi')
#curs = connection.execute('select GETDATE()')
#curs.fetchone()

#2018.4.24. use pymssql fail.
#import pymssql
#conn = pymssql.connnect(host='10.105.228.83',user='sa',password='Q!$Sb8t&p@bX',database='DJANGO_TEST')
#cur = conn.cursor()

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','income_manage.settings')

import django
django.setup()

from django.db import connections
curs = connections['default'].cursor()
curs.execute("select GETDATE()")
curs.fetchone()

