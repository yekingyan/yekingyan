#-----------
# Name:        计算工资日薪与时薪
# Created:     22/04/2018
#coding:       utf-8
#------------

msalary = float(raw_input('please input your monthly salary:'))#月工资
days = float(raw_input('how many days do you work in a month?'))#工作天数
hours = float(raw_input('how many hours do you work in a day?'))#每天工作时长
dailypay = msalary / days
hourlypay = dailypay / hours
print 'daily pay , hourly pay',dailypay,hourlypay
