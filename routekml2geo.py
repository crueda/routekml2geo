#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# autor: Carlos Rueda
# fecha: 2015-12-15
# mail: carlos.rueda@deimos-space.com

import time
import datetime
import os
import sys
import utm
import logging, logging.handlers


# obtenemos la hora actual
now_time = datetime.datetime.now()

# establecemos el formato segun el formato de los logs
format = "%H:%M:%S"

now = now_time.strftime(format)

print (now , ' -> routekml2geo - START')


with open('./rutas.txt') as fp:
	for line in fp:
		print line


# obtenemos la hora actual
now_time = datetime.now()
format = "%H:%M:%S"
now = now_time.strftime(format)
print (now , ' -> routekml2geo - FINISH')