import re
import sys

output = ''

while True:
  line = sys.stdin.readline()
  if not line: break
  if line[0] == '#':
    if output:
      print output
      output = ''
    print line.strip()
  else:
    x = re.findall('\w+|\W',line)
    for u in x:
      if not u.isspace():
        if len(output) + len(u) > 140:
          print output
	  output = ''
        if (re.match('\w',output[-1:]) and re.match('\w',u[:1])) or (output[-1:] == '=' and u[:1] == '-'):
          if len(output) + 1 + len(u) > 140:
	    print output
	    output = ''
	  else:
            output += ' '
        output += u

print output
