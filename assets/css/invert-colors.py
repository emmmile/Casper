#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import re
import math
from colour import Color

def process(c, i, k):
	# i is the amount of inversion: 0 preserves, 1 is totally inverted
	# k is the amount of desaturation: 0 preserves, 1 totally desaturated, 2 doubles the saturation
	c.red   = (1.0 - i) * c.red + i * (1.0 - c.red)
	c.green = (1.0 - i) * c.green + i * (1.0 - c.green)
	c.blue  = (1.0 - i) * c.blue + i * (1.0 - c.blue)

	intensity = 0.3 * c.red + 0.59 * c.green + 0.11 * c.blue
	c.red   = intensity * k + c.red * (1.0 - k)
	c.green = intensity * k + c.green * (1.0 - k)
	c.blue  = intensity * k + c.blue * (1.0 - k)
	return c

def tostr(c, alpha):
	t = [str(int(round(x * 255.0))) for x in [c.red, c.green, c.blue]]
	return "rgba(" + t[0] + ", " + t[1] + ", " + t[2] + ", " + str(alpha) + ")"

def colorrepl(m):
	cstr = s[m.start():m.end()]
	if cstr.startswith("rgba"):
		print(cstr)
		pp = re.compile(r"rgba\((?P<r>\d+),\s*(?P<g>\d+),\s*(?P<b>\d+),\s*(?P<a>\d+(\.\d+)?)\)")
		mm = pp.match(cstr)
		alpha = float(mm.group('a'))
		c = Color(rgb=(int(mm.group('r'))/255.0,int(mm.group('g'))/255.0, int(mm.group('b'))/255.0 ))
	else:
		c = Color(cstr)
		alpha = 1.0

	c = process(c, 0.95, 0.4)

	print(cstr + " -> " + tostr(c, alpha))
	return tostr(c,alpha)



s = codecs.open("screen.css", "r", "utf-8").read()
#replaces hex formats and rgba format
p = re.compile(r"(#\w{6}\b)|(#\w{3}\b)|(rgba[^\)]+\))")
f = codecs.open("screen-dark.css", "w", "utf-8")
f.write(p.sub(colorrepl, s))
f.close()