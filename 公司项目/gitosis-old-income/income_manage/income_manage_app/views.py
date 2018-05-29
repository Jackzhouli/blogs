# -*- coding:utf-8 -*-
# from django.shortcuts import render
#
# # Create your views here.
# from django.shortcuts import render, HttpResponse
# from models import Staff
# from datetime import datetime

# def home(req):
#     QuerySet = Staff.objects.all()
#     Info = 'World'
#     for Item in QuerySet:
#         print Item.Name
#         Info = Item.Name
#     return HttpResponse('Hello %s!' % Info)
#
#
# def insertdata(req):
#     try:
#         s = Staff(LoginID='aa', Name=u'测试人员', Sex=True, Birthday='2016-03-30', JoinTime=datetime.now())
#         s.save()
#         Info = u'插入成功'
#     except:
#         Info = u'插入失败'
#     return HttpResponse(Info)
