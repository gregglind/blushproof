#!/usr/bin/python
# Create blushlist.js from a list a domain names.
# Usage: make_blushlist.py <input_file> <category>

# TODO: Add support for creating from multiple files
import sys
if len(sys.argv) != 3:
  sys.exit("Usage: make_blushlist.py <input_file> <category>")

category = sys.argv[2]

try:
  f_in = open(sys.argv[1], "r")
  f_out = open("blushlist.js", "a")
except:
  sys.exit("Can't find file")

f_out.write("// This file is automatically generated by make_blushlist.py\n")
f_out.write("let blushlist = {\n");
for l in f_in.readlines():
  l = l.strip()
  f_out.write("  \"%s\" : \"%s\", \n" % (l, category));
f_out.write("};\n");
f_out.write("module.exports = blushlist;\n");

f_out.close()
