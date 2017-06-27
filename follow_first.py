#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
☆*°☆*°(∩^o^)~━━ 2016/12/30 20:35:30        
      (ˉ▽￣～) ~~ 一捆好葱 (*˙︶˙*)☆*°
      Fuction：语法分析 √ ━━━━━☆*°☆*°
"""
import  copy
import UI
global dic,dic_key,dic_first,dic_follow,list_sum
dic={}
dic_key=[]
list_sum=[]
dic_first={}
dic_follow={}

def first(a):
	global dic,dic_key,dic_first,dic_follow,list_sum
	if not dic.has_key(a):
		return [a,]
	if not dic_first.has_key(a):
		dic_first[a]=[]
	s=dic.get(a)
	for i in s:
		ss=first(i[0])
		dic_first[a].extend(ss)
	return dic_first[a]

def first_second(a):
	global dic, dic_key, dic_first, dic_follow
	temp=[]
	all_has=False
	s=dic.get(a)
	ss=dic_first.get(a)
	for i in s:
		for j in i:
			if dic_first.has_key(j):
				ttt=dic_first.get(j)
				if 'e' not in ttt:
					break
				else:
					num=i.index(j)
					# print num
					if num<len(i)-1 and dic_first.has_key(i[num+1]):
						getfirst=dic_first.get(i[num+1])
						temp=copy.deepcopy(getfirst)
						ss.extend(temp)
						# print temp
					if num+1==len(i)-1 and 'e' in temp:
						all_has=True
	if all_has:
		ss.append('e')

def follow(a):
	global dic, dic_key, dic_first, dic_follow,list_sum
	if not dic_follow.has_key(a) :
		dic_follow[a]=[]
		if a==dic_key[0]:
			dic_follow[a].append('$')
	else:
		return dic_follow[a]
	for line in list_sum:
		# print line
		if a in line:
			# print len(line)
			num=line.index(a)
			if  num<len(line)-2 :
				if dic_first.has_key(line[num+1]):
					temp=copy.deepcopy(dic_first.get(line[num+1]))
					# print temp
					# print temp
					dic_follow[a].extend(temp)
					# print dic_follow[a]
					if num == len(line)-3 and 'e' in temp:
						# print '123'
						get_follow = copy.deepcopy(follow(line[len(line) - 1]))
						# print '123'
						dic_follow[a].extend(get_follow)
				else:
					dic_follow[a].append(line[num+1])
					# print line[num+1]
			elif num==len(line)-2:
				# print line[len(line)-1]
				get_follow=copy.deepcopy(follow(line[len(line)-1]))
				dic_follow[a].extend(get_follow)
			else:
				continue  #这一步要特别注意
	return dic_follow[a]

def entry():
	f=open('d:\\python\\test.txt')
	s=f.readlines()
	for line in s:
		line=line.split('->')
		start=line[0].strip()
		dic_key.append(start)
		dic[start]=[]
		strs=line[1].split('|')
		for str in strs:
			single_strs=str.split()
			dic[start].append(single_strs)
			single_strs.append(start)
			list_sum.append(single_strs)
	# s=dic.get('E')
	# print s
	for key in dic_key:
		first(key)
	for key in dic_key:
		dic_first[key] = list(set(dic_first[key]))
	for key in dic_key:
		first_second(key)
	for key in dic_key:
		dic_first[key] = list(set(dic_first[key]))
	for key in dic_key:
		follow(key)
	for key in dic_key:
		dic_follow[key] = list(set(dic_follow[key]))
		if 'e' in dic_follow[key]:
			dic_follow[key].remove('e')
	# s=dic.get('E')
	# for i in s:
	# 	print i[0]
	print dic_first
	# s = dic.get("T'")
	# for i in s:
	# 	if 'e' in i:
	# 		print 'e has existed'
	# print list_sum
	print dic_key
	# for line in list_sum:
	# 	print line
	print dic_follow
entry()
"""
☆*°☆*°(∩^o^)~━
      (ˉ▽￣～) ~~ 一捆好葱 (*˙︶˙*)☆*°
      Fuction：语法分析 √ ━━━━━☆*°☆*°
"""

