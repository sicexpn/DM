#encoding=utf-8
#import psyco
#psyco.full()
import jieba
import sys
import re
import os
import jieba.posseg as pseg
reload(sys)
sys.setdefaultencoding( "utf-8" )

documentNumber = 0
documentList = []
def document(file_name):
	global documentNumber
	d = file(file_name).read().decode("euc-cn", 'ignore')
	documentList.append(d)		
    	documentNumber += 1

#    	fp = open(file_name,"w")	
#    	fp.write(tmp.encode("euc-cn"))
#    	fp.close()
#    print tmp.encode('utf-8')
#    print "================================"
#s3 = open("41.TXT").read().decode("euc-cn")
#print s3
#cuttest("41.TXT")
def cutDir(path):
	text_lists = os.listdir(path)
	text_numbers = len(text_lists)
	for i in range(0,text_numbers):
		text_path = path + '/' + text_lists[i]
		document(text_path)
pwd = os.getcwd()
#cuttext(pwd +'/' +'交通214'+'/'+'42.TXT')
cutDir(pwd +'/' + '交通214')
cutDir(pwd +'/' + '体育450')
cutDir(pwd +'/' + '军事249')
cutDir(pwd +'/' + '医药204')
cutDir(pwd +'/' + '政治505')
cutDir(pwd +'/' + '教育220')
cutDir(pwd +'/' + '环境200')
cutDir(pwd +'/' + '经济325')
cutDir(pwd +'/' + '艺术248')
cutDir(pwd +'/' + '计算机200')

print documentNumber