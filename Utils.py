import os, base64, string, random

def gen_key():
  key = os.urandom(256/8)
  return base64.b64encode(key)

def formStrMacro(varstr, instr):
  holder = []
  str1 = ''
  str2 = ''
  str1 = varstr + ' = "' + instr[:54] + '"'
  for i in xrange(54, len(instr), 48):
    holder.append(varstr + ' = '+ varstr +' + "'+instr[i:i+48])
    str2 = '"\r\n'.join(holder)

  str2 = str2 + "\""
  str1 = str1 + "\r\n"+str2
  return str1

def formStr(varstr, instr):
  holder = []
  str1 = ''
  str2 = ''
  str1 = varstr + ' = "' + instr[:56] + '"'
  for i in xrange(56, len(instr), 48):
    holder.append('"'+instr[i:i+48])
    str2 = '"\r\n'.join(holder)

  str2 = str2 + "\""
  str1 = str1 + "\r\n"+str2
  return "%s;" % str1

def randomuri(size = 15, chars=string.ascii_letters + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))