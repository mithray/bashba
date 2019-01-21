#!/usr/bin/python3

import os
import cmd
import argparse

class bashba(cmd.Cmd):
	intro = 'welcome to the bashba shell!'
	prompt = '> '

	def do_r(self, args):
		'read from the file system'
		filenames = os.listdir()
		print(filenames)
		print(args)

bashba().cmdloop("type help for help")
