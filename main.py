#!/usr/bin/env python3
import argparse
import sqlite3

class Note:
	def __init__(self,title:str="",data:str=""):
		assert isinstance(title,str)
		assert isinstance(data,str)
		self.title = title
		self.data  = data
		self.id = str(id(self))

class Notes:
	def __init__(self,*w,**kw):
		pass
	def new_note(self,title:str,data:str):
		return Note(title,data)
	def edit_note(self,id:str,title:str,data:str):
		pass
	def del_note(self,id:str):
		pass


