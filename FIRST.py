#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
☆*°☆*°(∩^o^)~━━ 2016/12/31 10:32:36        
      (ˉ▽￣～) ~~ 一捆好葱 (*˙︶˙*)☆*°
      Fuction：FIRST构造函数√ ━━━━━☆*°☆*°
"""
import  copy
import follow_first as z

z.entry()
def first(a):
	if not z.dic.has_key(a):
		return [a,]
	if not z.dic_first.has_key(a):
		z.dic_first[a]=[]
	s=z.dic.get(a)
	for i in s:
		ss=first(i[0])
		z.dic_first[a].extend(ss)
	return z.dic_first[a]

def first_second(a):
	temp=[]
	z.all_has=False
	s=z.dic.get(a)
	ss=z.dic_first.get(a)
	for i in s:
		for j in i:
			if z.dic_first.has_key(j):
				ttt=z.dic_first.get(j)
				if 'e' not in ttt:
					break
				else:
					num=i.index(j)
					# print num
					if num<len(i)-1 and z.dic_first.has_key(i[num+1]):
						getfirst=z.dic_first.get(i[num+1])
						temp=copy.deepcopy(getfirst)
						ss.extend(temp)
						# print temp
					if num+1==len(i)-1 and 'e' in temp:
						all_has=True
	if all_has:
		ss.append('e')
first_set=z.dic_first