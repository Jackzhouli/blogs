# -*- coding:UTF-8 -*-
from __future__ import unicode_literals

from django.db import models


class ApprovalAuditor(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sysroleid = models.IntegerField(db_column='SysRoleId', blank=True, null=True)  # Field name made lowercase.
    stepid = models.ForeignKey('ApprovalStep', db_column='StepId', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Approval_Auditor'


class ApprovalFunlink(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True)  # Field name made lowercase.
    link = models.CharField(db_column='Link', max_length=200, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Approval_FunLink'


class ApprovalStep(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True)  # Field name made lowercase.
    templateid = models.ForeignKey('ApprovalTemplate', db_column='TemplateId', blank=True, null=True,on_delete=models.CASCADE )  # Field name made lowercase.
    dictate = models.IntegerField(db_column='Dictate')  # Field name made lowercase.
    level = models.IntegerField(db_column='Level')  # Field name made lowercase.
    isend = models.BooleanField(db_column='IsEnd')  # Field name made lowercase.
    funlinkid = models.ForeignKey(ApprovalFunlink, db_column='FunLinkId', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Approval_Step'


class ApprovalTemplate(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100, blank=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    isok = models.BooleanField(db_column='IsOk')  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime')  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(db_column='CreatorUserId', blank=True, null=True)  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(db_column='LastModificationTime', blank=True, null=True)  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(db_column='LastModifierUserId', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId', blank=True, null=True)  # Field name made lowercase.
    creatorusername = models.TextField(db_column='CreatorUserName', blank=True)  # Field name made lowercase.
    lastmodifierusername = models.TextField(db_column='LastModifierUserName', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Approval_Template'


class Attachment(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True,verbose_name='附件名称')  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=200, blank=True,verbose_name='文件地址')  # Field name made lowercase.
    size = models.IntegerField(db_column='Size',verbose_name='附件大小')  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime')  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(db_column='CreatorUserId', blank=True, null=True)  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(db_column='LastModificationTime', blank=True, null=True)  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(db_column='LastModifierUserId', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId', blank=True, null=True)  # Field name made lowercase.
    creatorusername = models.CharField(db_column='CreatorUserName', max_length=50, blank=True)  # Field name made lowercase.
    lastmodifierusername = models.CharField(db_column='LastModifierUserName', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Attachment'
        verbose_name = '相关附件'
        verbose_name_plural = '相关附件'



class AttachmentExpense(models.Model):  #  改完
    id = models.ForeignKey(Attachment, db_column='Id', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    revenueid = models.ForeignKey('Revenue', db_column='RevenueId', blank=True, null=True,verbose_name='营业收入ID', on_delete=models.CASCADE)  # Field name made lowercase.
    expensetype = models.IntegerField(db_column='ExpenseType',verbose_name='费用类型')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Attachment_Expense'
        verbose_name = '费用相关附件'
        verbose_name_plural = '费用相关附件'


class AttachmentPay(models.Model):  # 改完
    id = models.ForeignKey(Attachment, db_column='Id', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    payrequestionid = models.ForeignKey('PayRequestion', db_column='PayRequestionId', blank=True, null=True,
                                        verbose_name='申请单支付ID', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'Attachment_Pay'
        verbose_name = '申请单支付附件'
        verbose_name_plural = '相关申请单支付附件'


class ContractExpense(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    contractid = models.ForeignKey('ContractInfo', db_column='ContractId', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    expenseitem = models.IntegerField(db_column='ExpenseItem')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=18, decimal_places=2)  # Field name made lowercase.
    paymentcycle = models.IntegerField(db_column='PaymentCycle', )  # Field name made lowercase.
    expenseusage = models.IntegerField(db_column='ExpenseUsage')  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime')  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(db_column='CreatorUserId', blank=True, null=True)  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(db_column='LastModificationTime', blank=True, null=True)  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(db_column='LastModifierUserId', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    creatorusername = models.CharField(db_column='CreatorUserName', max_length=50, blank=True)  # Field name made lowercase.
    lastmodifierusername = models.CharField(db_column='LastModifierUserName', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contract_Expense'


class ContractInfo(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)
    archiveid = models.IntegerField(db_column='ArchiveId', blank=True, null=True, verbose_name='长者档案ID')
    startdate = models.DateTimeField(db_column='StartDate', verbose_name = '合同开始日期')
    enddate = models.DateTimeField(db_column='EndDate', verbose_name='合同结束日期')
    settledstatus = models.IntegerField(db_column='SettledStatus', verbose_name = '结算状态')
    settledamount = models.DecimalField(db_column='SettledAmount', max_digits=18, decimal_places=2, blank=True,
                                        null=True, verbose_name='实际结算金额')  # Field name made lowercase.
    settlingtime = models.DateTimeField(db_column='SettlingTime', blank=True, null=True, verbose_name='合同需要结算时间')
    settledtime = models.DateTimeField(db_column='SettledTime', blank=True, null=True, verbose_name='财务结算时间')  # Field name made lowercase.
    settleduserid = models.BigIntegerField(db_column='SettledUserId', blank=True, null=True, verbose_name='结算人')  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime')  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(db_column='CreatorUserId', blank=True, null=True)  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(db_column='LastModificationTime', blank=True, null=True)  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(db_column='LastModifierUserId', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId', blank=True, null=True)  # Field name made lowercase.
    settledusername = models.CharField(db_column='SettledUserName', max_length=50, blank=True)  # Field name made lowercase.
    creatorusername = models.CharField(db_column='CreatorUserName', max_length=50, blank=True)  # Field name made lowercase.
    lastmodifierusername = models.CharField(db_column='LastModifierUserName', max_length=50, blank=True)  # Field name made lowercase.
    reasion = models.IntegerField(db_column='Reasion', verbose_name='离院结算原因')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contract_Info'
        verbose_name = '合同信息'
        verbose_name_plural = '合同信息'

    def __str__(self):
        return str(self.id)


class PayCostrecord(models.Model):  # 改完
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    paycost = models.DecimalField(db_column='PayCost', max_digits=18, decimal_places=2, verbose_name='支出金额')  # Field name made lowercase.
    payrequestionid = models.BigIntegerField(db_column='PayRequestionId', blank=True, null=True,verbose_name='申请单ID')  # Field name made lowercase.
    costtype = models.IntegerField(db_column='CostType', verbose_name='付费类型')  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime')  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(db_column='CreatorUserId', blank=True, null=True)  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(db_column='LastModificationTime', blank=True, null=True)  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(db_column='LastModifierUserId', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId', blank=True, null=True)  # Field name made lowercase.
    payrequestion = models.ForeignKey('PayRequestion', db_column='PayRequestion_Id', blank=True, null=True,
                                      verbose_name='申请单', on_delete=models.CASCADE)  # Field name made lowercase.
    creatorusername = models.CharField(db_column='CreatorUserName', max_length=50, blank=True)  # Field name made lowercase.
    lastmodifierusername = models.CharField(db_column='LastModifierUserName', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pay_CostRecord'
        verbose_name = '支出金额记录表'
        verbose_name_plural = '支出金额记录表'


class PayFinance(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, verbose_name='名称')  # Field name made lowercase.
    parentid = models.ForeignKey('self', db_column='ParentId', blank=True, null=True, verbose_name='父类别ID', on_delete=models.CASCADE)  # Field name made lowercase.
    cussourcetype = models.IntegerField(db_column='CusSourceType', blank=True, null=True, verbose_name='营销渠道来源')  # Field name made lowercase.
    costs = models.IntegerField(db_column='Costs', blank=True, null=True, verbose_name='运营成本')  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime')  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(db_column='CreatorUserId', blank=True, null=True)  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(db_column='LastModificationTime', blank=True, null=True)  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(db_column='LastModifierUserId', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId', blank=True, null=True)  # Field name made lowercase.
    creatorusername = models.CharField(db_column='CreatorUserName', max_length=50, blank=True)  # Field name made lowercase.
    lastmodifierusername = models.CharField(db_column='LastModifierUserName', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pay_Finance'
        verbose_name = '科目'
        verbose_name_plural = '科目'


class PayInformation(models.Model):
    id = models.ForeignKey('PayRequestion', db_column='Id', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    actualcost = models.DecimalField(db_column='ActualCost', max_digits=18, decimal_places=2, verbose_name='实际支付金额')  # Field name made lowercase.
    incomeway = models.TextField(db_column='IncomeWay', blank=True, verbose_name='支出类别 1 网银 2 现金')  # Field name made lowercase.
    voucherno = models.TextField(db_column='VoucherNo', blank=True, verbose_name='凭证号')  # Field name made lowercase.
    bankno = models.TextField(db_column='BankNo', blank=True, verbose_name='银行卡号')  # Field name made lowercase.
    manageruserid = models.BigIntegerField(db_column='ManagerUserId', blank=True, null=True, verbose_name='经办人ID')  # Field name made lowercase.
    paytime = models.DateTimeField(db_column='PayTime', blank=True, null=True, verbose_name='支出时间')  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime')  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(db_column='CreatorUserId', blank=True, null=True)  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(db_column='LastModificationTime', blank=True, null=True)  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(db_column='LastModifierUserId', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId', blank=True, null=True)  # Field name made lowercase.
    managerusername = models.TextField(db_column='ManagerUserName', blank=True, verbose_name='经办人')  # Field name made lowercase.
    creatorusername = models.CharField(db_column='CreatorUserName', max_length=50, blank=True)  # Field name made lowercase.
    lastmodifierusername = models.CharField(db_column='LastModifierUserName', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pay_Information'
        verbose_name = '支付信息'
        verbose_name_plural = '支付信息'



class PayProgres(models.Model):  # 改完
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime', blank=True, null=True, verbose_name='操作时间')  # Field name made lowercase.
    sysuserid = models.BigIntegerField(db_column='SysUserId', blank=True, null=True)  # Field name made lowercase.
    conclusion = models.TextField(db_column='Conclusion', blank=True)  # Field name made lowercase.
    suggestion = models.CharField(db_column='Suggestion', max_length=500, blank=True)  # Field name made lowercase.
    level = models.IntegerField(db_column='Level')  # Field name made lowercase.
    stepname = models.CharField(db_column='StepName', max_length=100, blank=True)  # Field name made lowercase.
    dictate = models.IntegerField(db_column='Dictate')  # Field name made lowercase.
    operatedate = models.DateTimeField(db_column='OperateDate', blank=True, null=True)  # Field name made lowercase.
    issubmit = models.BooleanField(db_column='IsSubmit')  # Field name made lowercase.
    requestionid = models.ForeignKey('PayRequestion', db_column='RequestionId', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    funlinkid = models.ForeignKey(ApprovalFunlink, db_column='FunLinkId', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId', blank=True, null=True)  # Field name made lowercase.
    sysusername = models.CharField(db_column='SysUserName', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pay_Progres'
        verbose_name = '申请单审核进度数据模型'
        verbose_name_plural = '支付审核进度数据模型'



class PayRequestion(models.Model):  # 改完
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    applytime = models.DateTimeField(db_column='ApplyTime', blank=True, null=True, verbose_name='申请时间')  # Field name made lowercase.
    paycost = models.DecimalField(db_column='PayCost', max_digits=18, decimal_places=2, verbose_name='支出金额')  # Field name made lowercase.
    paysubjectid = models.ForeignKey('PaySubject', db_column='PaySubjectId', blank=True, null=True,
                                     verbose_name='科目ID', on_delete=models.CASCADE)  # Field name made lowercase.
    count = models.CharField(db_column='Count', max_length=20, blank=True, verbose_name='数量')  # Field name made lowercase.
    receiveunit = models.CharField(db_column='ReceiveUnit', max_length=100, blank=True, verbose_name='收款单位')  # Field name made lowercase.
    backunit = models.CharField(db_column='BackUnit', max_length=100, blank=True, verbose_name='付款单位')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, verbose_name='备注')  # Field name made lowercase.
    confirmuserid = models.BigIntegerField(db_column='ConfirmUserId', blank=True, null=True, verbose_name='离开确认人ID')  # Field name made lowercase.
    payuserid = models.BigIntegerField(db_column='PayUserId', blank=True, null=True, verbose_name='申请人ID')  # Field name made lowercase.
    sharestartime = models.DateTimeField(db_column='ShareStarTime', blank=True, null=True, verbose_name='分摊开始月份')
    shareendtime = models.DateTimeField(db_column='ShareEndTime', blank=True, null=True, verbose_name='分摊结束月份')
    templateid = models.ForeignKey(ApprovalTemplate, db_column='TemplateId', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime')  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(db_column='CreatorUserId', blank=True, null=True)  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(db_column='LastModificationTime', blank=True, null=True)  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(db_column='LastModifierUserId', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId', blank=True, null=True)  # Field name made lowercase.
    cussourcetype = models.IntegerField(db_column='CusSourceType', blank=True, null=True, verbose_name='营销渠道来源')  # Field name made lowercase.
    costs = models.IntegerField(db_column='Costs', blank=True, null=True, verbose_name='运营成本')  # Field name made lowercase.
    payfinanceid = models.ForeignKey(PayFinance, db_column='PayFinanceId', blank=True, null=True, verbose_name='财务科目ID', on_delete=models.CASCADE)  # Field name made lowercase.
    confirmusername = models.CharField(db_column='ConfirmUserName', max_length=50, blank=True, verbose_name='离开确认人')  # Field name made lowercase.
    payusername = models.CharField(db_column='PayUserName', max_length=50, blank=True, verbose_name='申请人')  # Field name made lowercase.
    creatorusername = models.CharField(db_column='CreatorUserName', max_length=50, blank=True, verbose_name='创建人信息')  # Field name made lowercase.
    lastmodifierusername = models.CharField(db_column='LastModifierUserName', max_length=50, blank=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=60, blank=True, verbose_name='事项名称')  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptId', blank=True, null=True, verbose_name='申请部门ID')  # Field name made lowercase.
    depttext = models.CharField(db_column='DeptText', max_length=30, blank=True, verbose_name='申请部门名称')  # Field name made lowercase.
    duebank = models.CharField(db_column='DueBank', max_length=100, blank=True, verbose_name='收款银行')  # Field name made lowercase.
    collectionaccount = models.CharField(db_column='CollectionAccount', max_length=50, blank=True, verbose_name='收款账户')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pay_Requestion'
        verbose_name = '支出申请单'
        verbose_name_plural = '支出申请单'


class PaySharemonth(models.Model):  # 改完
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sharecostmonth = models.IntegerField(db_column='ShareCostMonth', verbose_name='分摊月份')  # Field name made lowercase.
    sharecostyear = models.IntegerField(db_column='ShareCostYear', verbose_name='分摊年份')  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime')  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(db_column='CreatorUserId', blank=True, null=True)  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(db_column='LastModificationTime', blank=True, null=True)  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(db_column='LastModifierUserId', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId', blank=True, null=True)  # Field name made lowercase.
    payrequestion = models.ForeignKey(PayRequestion, db_column='PayRequestion_Id', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    creatorusername = models.CharField(db_column='CreatorUserName', max_length=50, blank=True)  # Field name made lowercase.
    lastmodifierusername = models.CharField(db_column='LastModifierUserName', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pay_ShareMonth'
        verbose_name = '分摊月份'
        verbose_name_plural = '分摊月份'


class PaySubject(models.Model):  # 改完
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, verbose_name='名称')  # Field name made lowercase.
    parentid = models.ForeignKey('self', db_column='ParentId', blank=True, null=True, verbose_name='父类别ID', on_delete=models.CASCADE)  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime')  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(db_column='CreatorUserId', blank=True, null=True)  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(db_column='LastModificationTime', blank=True, null=True)  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(db_column='LastModifierUserId', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId', blank=True, null=True)  # Field name made lowercase.
    cussourcetype = models.IntegerField(db_column='CusSourceType', blank=True, null=True, verbose_name='营销渠道来源')  # Field name made lowercase.
    costs = models.IntegerField(db_column='Costs', blank=True, null=True, verbose_name='运营成本')  # Field name made lowercase.
    creatorusername = models.CharField(db_column='CreatorUserName', max_length=50, blank=True)  # Field name made lowercase.
    lastmodifierusername = models.CharField(db_column='LastModifierUserName', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pay_Subject'
        verbose_name = '科目'
        verbose_name_plural = '科目'


class PaySubjectPaythreshold(models.Model):  # 改完
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    paysubjectid = models.ForeignKey(PaySubject, db_column='PaySubjectId', blank=True, null=True, verbose_name='科目ID',
                                     on_delete=models.CASCADE)  # Field name made lowercase.
    paythresholdid = models.ForeignKey('PayThreshold', db_column='PayThresholdId', blank=True, null=True,
                                       verbose_name='父类别ID', on_delete=models.CASCADE)  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime')  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(db_column='CreatorUserId', blank=True, null=True)
    lastmodificationtime = models.DateTimeField(db_column='LastModificationTime', blank=True, null=True)
    lastmodifieruserid = models.BigIntegerField(db_column='LastModifierUserId', blank=True, null=True)
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId', blank=True, null=True)  # Field name made lowercase.
    creatorusername = models.CharField(db_column='CreatorUserName', max_length=50, blank=True)  # Field name made lowercase.
    lastmodifierusername = models.CharField(db_column='LastModifierUserName', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pay_Subject_PayThreshold'
        verbose_name = '科目'
        verbose_name_plural = '科目'


class PayThreshold(models.Model):  # 改完
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    smallpaycost = models.DecimalField(db_column='SmallPayCost', max_digits=18, decimal_places=2, verbose_name='金额（区间）小')  # Field name made lowercase.
    bigpaycost = models.DecimalField(db_column='BigPayCost', max_digits=18, decimal_places=2, verbose_name='金额（区间）大')  # Field name made lowercase.
    templateid = models.ForeignKey(ApprovalTemplate, db_column='TemplateId', blank=True, null=True,
                                   verbose_name='审核流程模板ID', on_delete=models.CASCADE)  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime', verbose_name='创建时间')  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(db_column='CreatorUserId', blank=True, null=True, verbose_name='创建人ID')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted', verbose_name='是否被删除')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId', blank=True, null=True)  # Field name made lowercase.
    creatorusername = models.CharField(db_column='CreatorUserName', max_length=50, blank=True, verbose_name='创建人信息')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pay_Threshold'
        verbose_name = '支出值'
        verbose_name_plural = '支出值'


class PaymentAddedservice(models.Model):
    id = models.ForeignKey('PaymentBase', db_column='Id', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payment_AddedService'


class PaymentBase(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)
    archiveid = models.IntegerField(db_column='ArchiveId', blank=True, null=True)
    revenueid = models.ForeignKey('Revenue', db_column='RevenueId', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(db_column='Name', max_length=200, blank=True)
    othername = models.TextField(db_column='OtherName', blank=True)  # Field name made lowercase.
    expenseitem = models.IntegerField(db_column='ExpenseItem')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=18, decimal_places=2)
    paymentcycle = models.IntegerField(db_column='PaymentCycle')  # Field name made lowercase.
    incurredstartdate = models.DateTimeField(db_column='IncurredStartDate')  # Field name made lowercase.
    incurredenddate = models.DateTimeField(db_column='IncurredEndDate')  # Field name made lowercase.
    paystartdate = models.DateTimeField(db_column='PayStartDate', blank=True, null=True)  # Field name made lowercase.
    payenddate = models.DateTimeField(db_column='PayEndDate', blank=True, null=True)  # Field name made lowercase.
    expenseusage = models.IntegerField(db_column='ExpenseUsage')  # Field name made lowercase.
    inorout = models.BooleanField(db_column='InOrOut')  # Field name made lowercase.
    issettled = models.BooleanField(db_column='IsSettled')  # Field name made lowercase.
    settleduserid = models.BigIntegerField(db_column='SettledUserId', blank=True, null=True)
    settledtime = models.DateTimeField(db_column='SettledTime', blank=True, null=True)
    creationtime = models.DateTimeField(db_column='CreationTime')  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(db_column='CreatorUserId', blank=True, null=True)  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(db_column='LastModificationTime', blank=True, null=True)  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(db_column='LastModifierUserId', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    settledusername = models.TextField(db_column='SettledUserName', blank=True)  # Field name made lowercase.
    creatorusername = models.CharField(db_column='CreatorUserName', max_length=50, blank=True)  # Field name made lowercase.
    lastmodifierusername = models.CharField(db_column='LastModifierUserName', max_length=50, blank=True)  # Field name made lowercase.

    def __unicode__(self):
        return str(self.id)

    class Meta:
        managed = False
        db_table = 'Payment_Base'
        verbose_name = '基本信息'
        verbose_name_plural = '基本信息'


class PaymentAdvance(models.Model):
    id = models.ForeignKey(PaymentBase, db_column='Id', related_name='payment_advance_id', on_delete=models.CASCADE)  # Field name made lowercase.
    syncpaymentid = models.TextField(db_column='SyncPaymentId', blank=True)  # Field name made lowercase.
    bedno = models.TextField(db_column='BedNo', blank=True)  # Field name made lowercase.
    bedstardate = models.DateTimeField(db_column='BedStarDate')  # Field name made lowercase.
    bedenddate = models.DateTimeField(db_column='BedEndDate')  # Field name made lowercase.
    relation = models.TextField(db_column='Relation', blank=True)  # Field name made lowercase.
    outadvancepaymentid = models.ForeignKey('self', db_column='OutAdvancePaymentId', blank=True, null=True,
                                            related_name='outadvancepaymentid', on_delete=models.CASCADE)  # Field name made lowercase.
    inadvancepaymentid = models.ForeignKey('self', db_column='InAdvancePaymentId', blank=True, null=True,
                                          related_name='inadvancepaymentid', on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payment_Advance'
        app_label = 'income_manage'


class PaymentAskleave(models.Model):
    id = models.ForeignKey('PaymentBase', db_column='Id', verbose_name='长者ID', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', verbose_name='请假年份')  # Field name made lowercase.
    month = models.IntegerField(db_column='Month', verbose_name='请假月份')  # Field name made lowercase.
    leavedate = models.DateTimeField(db_column='LeaveDate', verbose_name='离开时间')  # Field name made lowercase.
    backdate = models.DateTimeField(db_column='BackDate', verbose_name='返回时间')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payment_AskLeave'
        verbose_name = '长者请假情况'
        verbose_name_plural = '长者请假情况'

class PaymentContract(models.Model):
    id = models.ForeignKey(PaymentBase, db_column='Id', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    contractid = models.ForeignKey(ContractInfo, db_column='ContractId', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    originalprice = models.DecimalField(db_column='OriginalPrice', max_digits=18, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payment_Contract'


class PaymentDaily(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    archiveid = models.IntegerField(db_column='ArchiveId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=10)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId', blank=True, null=True)  # Field name made lowercase.
    expenseitem = models.IntegerField(db_column='ExpenseItem')  # Field name made lowercase.
    dailyprice = models.DecimalField(db_column='DailyPrice', max_digits=18, decimal_places=10)
    contractid = models.IntegerField(db_column='ContractId')  # Field name made lowercase.
    monthprice = models.DecimalField(db_column='MonthPrice', max_digits=18, decimal_places=10)
    days = models.IntegerField(db_column='Days')  # Field name made lowercase.
    stdamount = models.DecimalField(db_column='StdAmount', max_digits=18, decimal_places=10)
    stddailyprice = models.DecimalField(db_column='StdDailyPrice', max_digits=18, decimal_places=10)
    stdmonthprice = models.DecimalField(db_column='StdMonthPrice', max_digits=18, decimal_places=10)

    class Meta:
        managed = False
        db_table = 'Payment_Daily'


class PaymentDiscount(models.Model):
    id = models.ForeignKey(PaymentBase, db_column='Id', primary_key=True, on_delete=models.CASCADE)
    contractid = models.ForeignKey(ContractInfo, db_column='ContractId', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'Payment_Discount'


class PaymentPreferential(models.Model):
    id = models.ForeignKey(PaymentBase, db_column='Id', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payment_Preferential'


class PaymentRecord(models.Model):
    id = models.ForeignKey(PaymentBase, db_column='Id', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    paymentmethod = models.IntegerField(db_column='PaymentMethod', blank=True, null=True, verbose_name='支付方式')
    cardno = models.CharField(db_column='CardNo', max_length=50, blank=True, verbose_name='银行卡号')
    paymentamount = models.DecimalField(db_column='PaymentAmount', max_digits=18, decimal_places=2, verbose_name='支付金额')
    paymenttime = models.DateTimeField(db_column='PaymentTime', blank=True, null=True, verbose_name='支付日期')
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, verbose_name='备注')
    creationtime = models.DateTimeField(db_column='CreationTime')  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(db_column='CreatorUserId', blank=True, null=True)
    lastmodificationtime = models.DateTimeField(db_column='LastModificationTime', blank=True, null=True)
    lastmodifieruserid = models.BigIntegerField(db_column='LastModifierUserId', blank=True, null=True)
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId', blank=True, null=True)  # Field name made lowercase.
    creatorusername = models.CharField(db_column='CreatorUserName', max_length=50, blank=True)
    lastmodifierusername = models.CharField(db_column='LastModifierUserName', max_length=50, blank=True)
    arrivaltime = models.DateTimeField(db_column='ArrivalTime', blank=True, null=True, verbose_name='到账时间')
    costamount = models.DecimalField(db_column='CostAmount', max_digits=18, decimal_places=2, blank=True, null=True,
                                     verbose_name='财务费用金额（手续费）')  # Field name made lowercase.
    arrivalamount = models.DecimalField(db_column='ArrivalAmount', max_digits=18, decimal_places=2, blank=True,
                                        null=True, verbose_name='银行到账金额')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payment_Record'
        verbose_name='缴费记录'
        verbose_name_plural = '缴费记录'


class PaymentRefund(models.Model):
    id = models.ForeignKey(PaymentBase, db_column='Id', primary_key=True, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'Payment_Refund'


class Revenue(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)
    archiveid = models.IntegerField(db_column='ArchiveId', blank=True, null=True, verbose_name='长者档案ID')
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True, verbose_name='合同截止日期')
    expensetype = models.IntegerField(db_column='ExpenseType', verbose_name='费用类型')  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime')  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(db_column='CreatorUserId', blank=True, null=True)
    lastmodificationtime = models.DateTimeField(db_column='LastModificationTime', blank=True, null=True)
    lastmodifieruserid = models.BigIntegerField(db_column='LastModifierUserId', blank=True, null=True)
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId', blank=True, null=True)  # Field name made lowercase.
    creatorusername = models.CharField(db_column='CreatorUserName', max_length=50, blank=True)
    lastmodifierusername = models.CharField(db_column='LastModifierUserName', max_length=50, blank=True)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        managed = False
        db_table = 'Revenue'
        verbose_name = '营业收入'
        verbose_name_plural = '营业收入'


class ServiceMonths(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    archiveid = models.BigIntegerField(db_column='ArchiveId', blank=True, null=True)  # Field name made lowercase.
    contractid = models.BigIntegerField(db_column='ContractId', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId', blank=True, null=True)  # Field name made lowercase.
    paystartdate = models.DateField(db_column='PayStartDate', blank=True, null=True)  # Field name made lowercase.
    payenddate = models.DateField(db_column='PayEndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Service_Months'


class Settlements(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    contractid = models.ForeignKey(ContractInfo, db_column='ContractId', blank=True, null=True, verbose_name='合同ID',
                                   on_delete=models.CASCADE)  # Field name made lowercase.
    expenseitem = models.IntegerField(db_column='ExpenseItem', blank=True, null=True, verbose_name='费用项目')  # Field name made lowercase.
    mayprice = models.DecimalField(db_column='MayPrice', max_digits=18, decimal_places=2, verbose_name='应收（退）金额')  # Field name made lowercase.
    realprice = models.DecimalField(db_column='RealPrice', max_digits=18, decimal_places=2, verbose_name='实收（退）金额')  # Field name made lowercase.
    inorout = models.BooleanField(db_column='InOrOut', verbose_name='收费/退费')  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, verbose_name='备注')  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime')  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(db_column='CreatorUserId', blank=True, null=True)  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(db_column='LastModificationTime', blank=True, null=True)  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(db_column='LastModifierUserId', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId', blank=True, null=True)  # Field name made lowercase.
    creatorusername = models.TextField(db_column='CreatorUserName', blank=True)  # Field name made lowercase.
    lastmodifierusername = models.TextField(db_column='LastModifierUserName', blank=True)  # Field name made lowercase.

    def __str__(self):
        return self.expenseitem

    class Meta:
        managed = False
        db_table = 'Settlements'
        verbose_name = '收（退）费结算项目'
        verbose_name_plural = '收（退）费结算项目'


class SpecialIncome(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    incometime = models.DateTimeField(db_column='IncomeTime', blank=True, null=True, verbose_name='收入日期')  # Field name made lowercase.
    incometype = models.IntegerField(db_column='IncomeType', verbose_name='收入类型')  # Field name made lowercase.
    incomemoney = models.DecimalField(db_column='IncomeMoney', max_digits=18, decimal_places=2, verbose_name='收入金额')  # Field name made lowercase.
    incomeway = models.IntegerField(db_column='IncomeWay', verbose_name='收入方式')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=500, blank=True, verbose_name='备注')  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime')  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(db_column='CreatorUserId', blank=True, null=True)  # Field name made lowercase.
    lastmodificationtime = models.DateTimeField(db_column='LastModificationTime', blank=True, null=True)  # Field name made lowercase.
    lastmodifieruserid = models.BigIntegerField(db_column='LastModifierUserId', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId', blank=True, null=True)  # Field name made lowercase.
    creatorusername = models.CharField(db_column='CreatorUserName', max_length=50, blank=True)  # Field name made lowercase.
    lastmodifierusername = models.CharField(db_column='LastModifierUserName', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Special_Income'
        verbose_name = '专项收入'
        verbose_name_plural = '专项收入'


class SysMsgrecord(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    msgcontent = models.CharField(db_column='MsgContent', max_length=200, blank=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=200, blank=True)  # Field name made lowercase.
    progressid = models.IntegerField(db_column='ProgressId', blank=True, null=True)  # Field name made lowercase.
    progresstype = models.CharField(db_column='ProgressType', max_length=100, blank=True)  # Field name made lowercase.
    isunread = models.BooleanField(db_column='IsUnread')  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime')  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(db_column='CreatorUserId', blank=True, null=True)
    lastmodificationtime = models.DateTimeField(db_column='LastModificationTime', blank=True, null=True)
    lastmodifieruserid = models.BigIntegerField(db_column='LastModifierUserId', blank=True, null=True)
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId', blank=True, null=True)  # Field name made lowercase.
    creatorusername = models.TextField(db_column='CreatorUserName', blank=True)  # Field name made lowercase.
    lastmodifierusername = models.TextField(db_column='LastModifierUserName', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sys_MsgRecord'


class SysPrintinfo(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    orgname = models.CharField(db_column='OrgName', max_length=50, blank=True, verbose_name='机构名称')
    communityname = models.CharField(db_column='CommunityName', max_length=50, blank=True, verbose_name='社区名称')
    remittancename = models.CharField(db_column='RemittanceName', max_length=50, blank=True, verbose_name='转账汇款名称')
    remittanceaccount = models.CharField(db_column='RemittanceAccount', max_length=50, blank=True,
                                         verbose_name='转账汇款账号')
    paymentplace = models.CharField(db_column='PaymentPlace', max_length=50, blank=True, verbose_name='缴费地点')
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=50, blank=True, verbose_name='联系电话')
    presidentid = models.IntegerField(db_column='PresidentId', blank=True, null=True, verbose_name='养老社区院长ID')
    presidentname = models.CharField(db_column='PresidentName', max_length=50, blank=True, verbose_name='养老社区院长姓名')
    creationtime = models.DateTimeField(db_column='CreationTime')  # Field name made lowercase.
    creatoruserid = models.BigIntegerField(db_column='CreatorUserId', blank=True, null=True)
    lastmodificationtime = models.DateTimeField(db_column='LastModificationTime', blank=True, null=True)
    lastmodifieruserid = models.BigIntegerField(db_column='LastModifierUserId', blank=True, null=True)
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId', blank=True, null=True)  # Field name made lowercase.
    creatorusername = models.CharField(db_column='CreatorUserName', max_length=50, blank=True)
    lastmodifierusername = models.CharField(db_column='LastModifierUserName', max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'Sys_PrintInfo'
        verbose_name = '机构收费通知单打印信息配置项实体类'
        verbose_name_plural = '机构收费通知单打印信息配置项实体类'


class Migrationhistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', max_length=150)  # Field name made lowercase.
    contextkey = models.CharField(db_column='ContextKey', max_length=300)  # Field name made lowercase.
    model = models.BinaryField(db_column='Model')  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__MigrationHistory'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)
    permission = models.ForeignKey('AuthPermission', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.CASCADE)
    codename = models.CharField(max_length=100)

    class Meta:

        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(AuthPermission, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class IncomeManageAppStaff(models.Model):
    loginid = models.CharField(db_column='LoginID', max_length=20)
    name = models.CharField(db_column='Name', max_length=10)
    sex = models.BooleanField(db_column='Sex')
    birthday = models.CharField(db_column='Birthday', max_length=20, blank=True)
    jointime = models.DateTimeField(db_column='JoinTime')

    class Meta:
        managed = False
        db_table = 'income_manage_app_staff'
