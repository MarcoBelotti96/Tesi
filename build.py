#!/usr/bin/env python

import zipfile
import os

def build():
	if not os.path.exists("../data/tmp/prepared_data_capoluoghi"):
		with zipfile.ZipFile("data.zip", "r") as zip_ref:
			zip_ref.extractall()

build()
