#!/usr/bin/python
# -*- coding: UTF-8 -*-
print('nlp2 test')
import nltk
from nltk.tokenize import sent_tokenize
import re
from nltk.corpus import brown
file = open('2.textile')
lines = file.read()#读取全部内容
'''text = lines
sent = sent_tokenize(text)
words = []
for i in sent:
	words.append(nltk.word_tokenize(sent))
	print(words)'''
text = 'PathonTip.com is a very good website. We can learn a lot from it.'
#将文本拆分成句子列表
sens = nltk.sent_tokenize(text)
print(sens)
#将句子进行分词,nltk的分词是句子级的,因此要先分句,再逐句分词,否则效果会很差.
#nf = open("./" + new_file, "wb")
key_work = 'is'
for line in sens:
        rs = re.search(key_work, line)
        if rs:
        	print(line)
        print(rs)


''''
words = []
for sent in sens:
    words.append(nltk.word_tokenize(sent))
#print(words)
for i in str(sens).replace('\n',''):
	name = 'it'
	results = re.findall(r'[^。]*?{}[^。]*?。'.format(name), str(sens))
for i in enumerate(results):
	print(i)#一定要缩进，按一个空格键


keyStart = '<He was an old man>'
keyEnd = '<in some way.">'
buff = file.read()
pat = re.compile(keyStart+'(.*?)'+keyEnd, re.S)
result = pat.findall(buff)
file.close()
print(result)


for i in sent_tokenize(str(text).replace('\n','')):
	#print([i])
	name = 'fished' # 选择这个词 作为特定词
	results = re.findall(r'[^。]*?{}[^。]*?。'.format(name), text)
for i, r in enumerate(results, 1):
	print(i,r)#一定要缩进，按一个空格键

patterns = [ (r'.*ing$', 'VBG'), # gerunds
 (r'.*ed$', 'VBD'), # simple past
 (r'.*an$', 'VBZ'), # 3rd singular present
 (r'.*ould$', 'MD'), # modals
 (r'.*\'s$', 'NN$'), # possessive nouns
 (r'.*s$', 'NNS'), # plural nouns
 (r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
 (r'.*', 'NN') # nouns (default)
 ]

reg = nltk.RegexpTagger(patterns)
for i in range(len(words)):
	#tag = reg.tag(words[i])
	#print(reg.tag(words[i]))
	for i in range(len(words[1])):
		tag = str(reg.tag(words[1]))
		#print(len(words[1]))
		if tag[i] == 'VBZ':
			print(words[1])
'''