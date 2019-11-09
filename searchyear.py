#encoding:utf-8
import  sxtwl
 
#日历中文索引
ymc = [u"十一", u"十二", u"正", u"二", u"三", u"四", u"五", u"六", u"七", u"八", u"九", u"十" ]
rmc = [u"初一", u"初二", u"初三", u"初四", u"初五", u"初六", u"初七", u"初八", u"初九", u"初十",
 u"十一", u"十二", u"十三", u"十四", u"十五", u"十六", u"十七", u"十八", u"十九",
  u"二十", u"廿一", u"廿二", u"廿三", u"廿四", u"廿五", u"廿六", u"廿七", u"廿八", u"廿九", u"三十", u"卅一"]
 
 
lunar = sxtwl.Lunar()  #实例化日历库
 
##阴历转阳历
#day = lunar.getDayByLunar(2019, 10, 8  , False)
# 
#print  u"公历:", day.y, u"年", day.m, u"月", day.d, u"日"
#if day.Lleap:
#    print u"阴历:润", ymc[day.Lmc], u"月", rmc[day.Ldi], u"日"
#else:
#    print u"阴历:", ymc[day.Lmc], u"月", rmc[day.Ldi], u"日"
# 
# 
# 
##同理，阳历转阴历
# 
#day = lunar.getDayBySolar(2019, 11, 04) 
#print  u"公历:", day.y, u"年", day.m, u"月", day.d, u"日"
#if day.Lleap:
#    print u"阴历:润", ymc[day.Lmc], u"月", rmc[day.Ldi], u"日"
#else:
#    print u"阴历:", ymc[day.Lmc], u"月", rmc[day.Ldi], u"日"
#

def checkdate(year,month,day, f_month, f_day):
	tempday = lunar.getDayByLunar(year, month, day, False)
	if int(tempday.y) == year and int(tempday.m) == f_month and int(tempday.d) == f_day:
		return True
	else:
		return False

def searchYear(year, month, day):
	print "========================================="
	#cycle from 1981 ----2019
	
	tempday = lunar.getDayByLunar(year, month, day, False)
	for i in range(year, year+100):
		if checkdate(i, month, day, tempday.m, tempday.d):
			print i
	print "========================================="
	
def main():
	print u"请按照提示输入<enter>"
	year = input("请输入年:")
	month = input("请输入阴历月:")
	day = input("请输入阴历日:")
	print u"输入", year, u"年", month, u"月", day, u"日"
	
	searchYear(int(year), int(month), int(day))	

if __name__ == "__main__":
	main()
