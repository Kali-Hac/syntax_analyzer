#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
☆*°☆*°(∩^o^)~━━ 2016/12/31 10:30:43        
      (ˉ▽￣～) ~~ 一捆好葱 (*˙︶˙*)☆*°
      Fuction：构造界面 √ ━━━━━☆*°☆*°
"""
import Tkinter as t
import tkFont
import follow_first
import copy
from prettytable import PrettyTable
import  time
from pylsy import pylsytable
global dic,dic2,input_0
input_0=''
dic={}
dic2={}
def output():
	cnt=2
	t.Label(root, text="文法产生式读取如下：", font=fttt).grid(row=0,column=1,rowspan=2)
	# ff=t.Frame(height=100, width=400,bg='blue').grid(row=10,column=10)
	for line in s:
		line = line[:-1]
		t.Label(root, text=line, justify=t.CENTER, font=ft).grid(sticky='N',column=1,row=cnt,rowspan=2)
		cnt = cnt + 1
	t.Button(root, text="下一步产生FOLLOW和FIRST集合0 √", width=32, command=output_2).grid(sticky='N',column=1,row=8)

def output_2():
	first=[]
	follow=[]
	for key in follow_first.dic_key:
		name.append(key)
		first.append(follow_first.dic_first.get(key))
		follow.append(follow_first.dic_follow.get(key))
	table.add_data("Name", name)
	table.add_data("FIRST", first)
	table.add_data("FOLLOW", follow)
	t.Label(root, text=table, justify=t.CENTER, font=ft).grid(row=0,column=3,rowspan=9)
	print table
	t.Label(root, text="文法的FIRST集合和FOLLOW集合产生完毕",justify=t.CENTER, font=ftt2).grid(sticky='S', column=1, row=7)
	t.Button(root, text="构造表达式的语法分析表 √", width=32,command=output_3,font=ft).grid(sticky='N', column=3,columnspan=3)

def output_3():
	global dic,dic2,input_0
	b=['Nonterminal']
	end_str=['id','+','*','(',')','$']
	for i in end_str:
		dic[i]=[' ',' ',' ',' ',' ']
		dic2[i]=[[],[],[],[],[]]
	b.extend(end_str)
	table = pylsytable(b)
	table.add_data('Nonterminal',follow_first.dic_key)
	for key in follow_first.dic_key:
		for i in follow_first.dic_first[key]:
			if i!='e':
				for line in follow_first.list_sum:
					if key in line and line[len(line)-1]==key and line[len(line)-2]!='e':
						n=0
						s=''
						list=[]
						while n<len(line)-1:
							s+=str(line[n])
							list.append(str(line[n]))
							n=n+1
						sss=str(line[0])
						if sss==i or (sss!=i and sss not in end_str):
							# print sss
							num=follow_first.dic_key.index(key)
							dic[i][num]=(key+'->'+s)
							dic2[i][num].extend(list)
							# print dic2[i][num]
							# print s
							# print i,num,':',key+'->'+s
	for strs in end_str:
		for key in follow_first.dic_key:
			if strs in follow_first.dic_follow[key] and strs not in follow_first.dic_first[key]:
				if 'e' in follow_first.dic_first[key]:
					num = follow_first.dic_key.index(key)
					dic[strs][num]=(key+'-> e')
					list_2=[key,'->','e']
					dic2[strs][num].extend(list_2)
				else:
					num = follow_first.dic_key.index(key)
					dic[strs][num] = ('synch')
					dic2[strs][num]=['synch']
	for strs in end_str:
		table.add_data(strs,dic[strs])
	t.Label(root, text="表达式的语法分析表构造完毕 ", justify=t.CENTER, font=ftt2).grid(sticky='W',row=9, column=0,columnspan=1)
	t.Label(root, text="如果查看M[A,a]是synch,在继续分析时栈顶的非终结符号被弹出",justify=t.CENTER, font=ftt2).grid(sticky='W',row=9, column=1,columnspan=3)
	t.Label(root, text=table, justify=t.CENTER, font=ft).grid(row=12, column=0, rowspan=8,columnspan=4)
	u=t.StringVar()
	u.set(' id + id * id')
	input_0=u.get()
	print input_0
	t.Label(root, text="如果M[A,a]是error（相应的语法分析表条目为空时）",justify=t.CENTER, font=ftt2).grid(sticky='N', column=0,columnspan=3)
	t.Label(root, text="预测语法分析过程->检测到错误",justify=t.CENTER, font=ftt2).grid(sticky='N', column=0,columnspan=3)
	t.Entry(root, textvariable=u, state = 'normal').grid(row=23, column=0,sticky='N',columnspan=2)
	t.Button(root, text="进行语法预测分析（包含错误恢复） √", width=32, command=analysis,default='active').grid(sticky='N', column=0,columnspan=2)
	t.Label(root, text="文法表达式完全匹配成功，过程如右", justify=t.CENTER, font=ftt2).grid(sticky='N', column=0, columnspan=3)
	label = t.Label(root, text='Copyright © 2017 ', font=ftt).grid(columnspan=2, column=0, rowspan=2,	                                                                             sticky='N')
	label = t.Label(root, text='All rights reserved by Haocong ', font=ftt).grid(columnspan=2, column=0, rowspan=2, sticky='N')
	# 	analysis('E',u.get())
	# print dic
	# print dic2

def list_to_str(s):
	ss=''
	for i in s:
		ss+=str(i)
	return ss

def analysis():
	global input_0,u
	start='E'
	# input_0=u.get()
	# print input_0
	s=input_0.split()
	print s
	s.append('$')
	x = PrettyTable(["[已匹配]", "[栈]", "[输入]", "[动作]"])
	x.align["[动作]"] = "l"
	x.padding_width = 1
	# x.add_row(["Adelaide", 1295, 1158259, 600.5])
	# print x
	cnt=0
	stack=[]
	stack_already=[]
	stack.append(start)
	s1=list_to_str(stack)
	s2=list_to_str(s)
	s3 = list_to_str(stack_already)
	x.add_row([s3, s1+'$',s2,' '])
	# print '1'
	while s[cnt]!='$':
		if follow_first.dic_first.has_key(stack[0]):
			# print stack[0]
			num=follow_first.dic_key.index(stack[0])
			if dic2[s[cnt]][num]:
				ssss=dic2.get(s[cnt])
				if 'e' in ssss[num]:
					stack=stack[1:]
				else:
					st=copy.deepcopy(dic2[s[cnt]][num])
					st.extend(stack[1:])
					stack=st
				s1 = list_to_str(stack)
				s2 = list_to_str(s)
				s3 = list_to_str(stack_already)
				# ssss=dic2.get(s[cnt])
				# print stack[0]
				if 'synch' in ssss[num]:
					print '2'
					sttemp=stack[0]+','+s[cnt]
					stack = stack[1:]
					x.add_row([s3, s1 + '$', s2 + '$', '[错误] '+sttemp+'= synch'])
				else:
					x.add_row([s3, s1 + '$', s2 + '$','[输出] '+dic[s[cnt]][num]])
				# print s3,s1,s2
				# print '1'
			else:
				s1 = list_to_str(stack)
				s2 = list_to_str(s)
				s3 = list_to_str(stack_already)
				x.add_row([s3, s1 + '$', s2 + '$', '[错误] 预测分析表为空，略过'])
				cnt = cnt + 1
		else:
			stack_already.append(stack[0])
			pipei=stack[0]
			stack=stack[1:]
			sss=s[cnt+1:]
			# print sss
			s1 = list_to_str(stack)
			s2 = list_to_str(sss)
			s3=list_to_str(stack_already)
			x.add_row([s3, s1 + '$', s2 , '[匹配] ' + pipei])
			# print s3, s1, s2
			# print s[cnt]
			cnt=cnt+1
			# print s[cnt]
			# print cnt
			# print stack_already,stack,s
			# print s[cnt]
			# print '2'
	while stack and stack[0]!='$':
		if 'e' in follow_first.dic_first[stack[0]]:
			stemp=stack[0]+'->'+'e'
			stack = stack[1:]
			s1 = list_to_str(stack)
			s2 = list_to_str(sss)
			s3 = list_to_str(stack_already)
			x.add_row([s3, s1 + '$', s2, '[输出] ' + stemp])
	if len(stack)==0 and s[0]=='$':
		print "完全匹配成功"
	print x
	t.Label(root, text=x, justify=t.CENTER, font=ft).grid(row=20, column=2, rowspan=9, columnspan=4)


if __name__ =='__main__':
	root=t.Tk()
	root.title("表达式的文法FIRSR/FOLLOW,语法预测分析表的构建及过程")
	menu=t.Menu(root)
	ft = tkFont.Font(family='Fixdsys', size=10, weight=tkFont.BOLD)
	ftt = tkFont.Font(family='Comic Sans MS', size=30, weight=tkFont.BOLD)
	ftt2 = tkFont.Font(family='Comic Sans MS', size=15, weight=tkFont.BOLD)
	fttt = tkFont.Font(family='Fixdsys', size=14,weight=tkFont.BOLD)
	submenu=t.Menu(menu,tearoff=0)
	submenu.add_command(label="Open")
	submenu.add_command(label="Save")
	submenu.add_separator()
	submenu.add_command(label="Close")
	menu.add_cascade(label="Hc->File",menu=submenu)
	submenu = t.Menu(menu, tearoff=0)
	submenu.add_command(label="Copy")
	submenu.add_command(label="Paste")
	submenu.add_separator()
	submenu.add_command(label="Cut")
	menu.add_cascade(label="Hc->Edit", menu=submenu)
	submenu = t.Menu(menu, tearoff=0)
	submenu.add_command(label="Haocong")
	submenu.add_command(label="Python")
	submenu.add_separator()
	submenu.add_command(label="About")
	menu.add_cascade(label="Hc->Log", menu=submenu)
	menu.add_cascade(label="Hc->Manage", menu=submenu)
	menu.add_cascade(label="Hc->Help", menu=submenu)
	# menu.add_cascade(label="HC->Help", menu=submenu)
	root.config(menu=menu)
	# edit1=t.Text(root)
	# edit1.pack()
	a = ['Name', 'FIRST', 'FOLLOW']
	table = pylsytable(a)
	name = []
	f = open('d:\\python\\test.txt','r')
	s = f.readlines()
	t.Label(root,text="   请输入文法产生式：",font=fttt).grid(sticky='W',rowspan=2)
	u=t.StringVar()
	u1 = t.StringVar()
	u2 = t.StringVar()
	u3 = t.StringVar()
	u4 = t.StringVar()
	e1 = t.Entry(root,textvariable=u)
	u.set("E -> T E'")
	e2 = t.Entry(root,textvariable=u1)
	u1.set("T' -> * F T' | e")
	e3 = t.Entry(root,textvariable=u2)
	u2.set("E' -> + T E' | e")
	e4 = t.Entry(root,textvariable=u3)
	u3.set("F -> ( E ) | id")
	e5 = t.Entry(root,textvariable=u4)
	u4.set("T -> F T' ")
	e6 = t.Entry(root)
	e1.grid(sticky='N')
	e2.grid(sticky='N')
	e3.grid(sticky='N')
	e4.grid(sticky='N')
	e5.grid(sticky='N')
	e6.grid(sticky='N')
	t.Button(root,text="确定 √",width=10,command=output).grid(sticky='N')
	follow_first.entry()
	temp=10
	# for fm in ['red', 'blue', 'yellow', 'green', 'white', 'black']:
	# 	# 注意这个创建Frame的方法与其它创建控件的方法不同，第一个参数不是root
	# 	t.Frame(height=20, width=400, bg=fm).grid(row=cnt,column=10)
	# 	cnt=cnt+1
	root.mainloop()
