#!/usr/bin/python

import urllib2, os, re
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

INPUT_FILE_PATH = "" #File path
INPUT_VAR_NAME  = "" #Form input variable name 
URL             = "" #POST URL

register_openers()

datagen, headers = multipart_encode({INPUT_VAR_NAME : open(INPUT_FILE_PATH,"rb")})

request = urllib2.Request(URL, datagen, headers)

# Make a request
res = urllib2.urlopen(request).read()
