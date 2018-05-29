# -*- coding:UTF-8 -*-
# from django.contrib import admin
import xadmin
from .models import *


@xadmin.sites.register(PaymentBase)
class PaymentBaseAdmin:

    fields = ['id', 'archiveid', 'revenueid', 'name', 'othername', 'expenseitem', 'price', 'paymentcycle',
              'incurredstartdate', 'incurredenddate', 'paystartdate', 'payenddate', 'expenseusage ', 'inorout',
              'issettled', 'settleduserid', 'settledtime', 'creationtime ', 'creatoruserid', 'lastmodificationtime',
              'lastmodifieruserid', 'isdeleted', 'unitprice ', 'settledusername', 'creatorusername ',
              'lastmodifierusername']
    list_display = ['id', 'archiveid', 'revenueid', 'name', 'othername', 'expenseitem', 'price', 'paymentcycle']
    list_filter = ['creationtime', 'price', 'incurredstartdate']
    search_fields = ['archiveid',]
    list_per_page = 20
    list_editable = ['name',]
    list_max_show_all = 200


@xadmin.site.register(ContractInfo)
class ContractInfoAdmin:
    fields = ['id', 'archiveid', 'startdate', 'enddate', 'settledstatus', 'settledamount', 'settlingtime ',
              'settledtime', 'settleduserid', 'creationtime', 'creatoruserid', 'lastmodificationtime',
              'lastmodifieruserid ', 'isdeleted',  'orgid', 'settledusername', 'creatorusername', 'lastmodifierusername ',
              'reasion', ]
    list_display = ['startdate','settleduserid', 'creationtime', 'creatoruserid', 'lastmodificationtime',]
    list_filter = ['creatorusername', ]
    search_fields = ['startdate',]
    list_per_page = 20
    list_max_show_all = 200


@xadmin.site.register(Settlements)
class SettlementsAdmin:
    fields = ['id', 'contractid', 'expenseitem', 'mayprice', 'realprice', 'inorout', 'remark ',
              'creationtime', 'lastmodificationtime', 'lastmodifieruserid', 'isdeleted',
              'orgid ', 'creatorusername',  'lastmodifierusername', ]
    list_display = ['mayprice', 'realprice', 'inorout',]
    list_filter = ['contractid','mayprice']
    search_fields = ['id',]
    list_per_page = 20
    list_max_show_all = 200


@xadmin.site.register(PaymentRecord)
class PaymentRecordAdmin:
    fields = ['id', 'paymentmethod ', 'cardno', 'paymentamount', 'paymenttime', 'remark', 'creationtime ',
              'creatoruserid', 'lastmodificationtime', 'lastmodifieruserid', 'isdeleted',
              'orgid ', 'creatorusername',  'lastmodifierusername', 'arrivaltime', 'costamount', 'arrivalamount',]
    list_display = ['id', 'cardno', 'paymentamount', 'paymenttime', 'remark',]
    list_filter = ['lastmodificationtime', 'arrivaltime', 'costamount',]
    search_fields = ['arrivalamount',]
    list_per_page = 20
    list_max_show_all = 200







