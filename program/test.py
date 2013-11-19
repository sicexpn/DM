import jieba
import sys
import re
import os
import jieba.posseg as pseg
reload(sys)
sys.setdefaultencoding("utf-8")

text = file("41.TXT").read().decode("euc-cn",'ignore')
#seg_list = jieba.cut(text,cut_all = True)
words = pseg.cut(text)
#print "Full Mode:", "/".join(seg_list)
word_lists = []
file_stopwords = open("stopwords.txt").readlines()
stopword_lists = []
for word in file_stopwords:
	stopword_lists.append(word.strip('\r\n').decode("euc-cn",'ignore'))
stopword_len = len(stopword_lists)
word_len = len(word_lists)
for w in words:
	if w.flag=="n" and w.word not in stopword_lists:
#		print w.flag, w.word
		word_lists.append(w.word)

print "/".join(word_lists)#.encode("euc-cn")

#stop_words = file("stopwords.txt").read().decode("euc-cn",'ignore')
#print stop_words[1]
#file_stopwords = open("stopwords.txt").readlines()#.decode("euc-cn",'ignore')
#print file1[177].decode("euc-cn")
#print len(file_stopwords)
#stopword_len = len(file_stopwords)
#for i in range(0,stopword_len):
#	print file_stopwords[i].decode("euc-cn",'ignore')

for i in range(0,word_len):
	for j in range(0,stopword_len):
		if stopword_lists[j] == word_lists[i]:
			print "okay"
#			del word_lists[i]
#for term in word_lists:
#	for stop_word in stopword_lists:
#		if term == stop_word:
#			print "okay"
#			word_lists.remove(term)
#print stopword_lists
#print "/".join(word_lists)

#print "/".join(word_lists)
#print "/".join(file1)
#global a
a = 0
def do():
	global a 
	a += 1
do()
do()
print a
print a
