import jieba
import sys
import re
import os
import jieba.posseg as pseg
reload(sys)
sys.setdefaultencoding("utf-8")

import math
from operator import itemgetter

def freq(word,document):
	return document.split(None).count(word)

def wordCount(document):
	return len(document.split(None))

def numDocsContaining(word,documentList):
	count = 0
	for document in documentList:
		if freq(word,document) > 0:
			count += 1
	return count

def tf(word,document):
	return (freq(word,document) / float(wordCount(document)))

def idf(word,documentList):
	return math.log(len(documentList) / numDocsContaining(word,documentList))

def tfidf(word,document,documentList):
	return (tf(word,document) * idf(word,documentList))


documentList = []
d1 = file("41.TXT").read().decode("euc-cn",'ignore')
d2 = file("42.TXT").read().decode("euc-cn",'ignore')
 
documentList.append(d1)
documentList.append(d2)
words = {}
documentNumber = 1
for word in documentList[documentNumber].split(None):
    words[word] = tfidf(word,documentList[documentNumber],documentList)
itemList = []
for item in sorted(words.items(), key=itemgetter(1), reverse=True):
    itemList.append( "%f <= %s" % (item[1], item[0]))
print "\r\n".join(itemList)