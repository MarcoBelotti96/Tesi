#! /usr/bin/env python3

import zipfile
import os

def build():
	print("Building project...")
	with zipfile.ZipFile("data.zip", "r") as zip_ref:
		zip_ref.extractall()
	print("Build done!")

build()
