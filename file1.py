import hashlib
from hashlib import blake2b

def looping(x, y):
  done = 0
  i = 0
  while i <= y:
    if i == y:
      done += 1
      break
    print(str(x))
    i += 1
  if done == 1:
    return str(y)

def looping2(x, y):
  done = 0
  i = 0
  while i <= y:
    if i == y:
      done += 1
      break
    print(str(i+1)+". "+str(x))
    i += 1
  if done == 1:
    return "\nlooped "+str(y)+" times"

whereruningvar = 0

def whererunning(y):
  x = whereruningvar
  if x == 1:
    print('code: '+str(y))
  elif x == 0:
    pass
  else:
    print('ERROR code: 6 ')

# wr is the shortened function of 'whererunning'
def wr(y):
  x = whereruningvar
  if x == 1:
    print('code: '+str(y))
  elif x == 0:
    pass
  else:
    print('ERROR code: 6 ')

ns= "\n\n"

#m = hashlib.sha256()
#m.update(b"Nobody inspects")
#m.update(b" the spammish repetition")
#m.digest()
#m.digest_size
#m.block_size

#print(m)

s = hashlib.sha224(b"Nobody inspects the spammish repetition").hexdigest()
s2 = hashlib.sha256(b"Nobody inspects the spammish repetition").hexdigest()
s3 = hashlib.sha512(b"Nobody inspects the spammish repetition").hexdigest()
#s4 = hashlib.sha1024(b"Nobody inspects the spammish repetition").hexdigest()
dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
dk2 =dk.hex()






h = blake2b(digest_size=64)
h.update(b'Nobody inspects the spammish repetition')
h2 = h.hexdigest()
h3 = len(h.digest())
h4 = len(h2)

def hashed(x):
  hashs = blake2b(digest_size=64)
  hashs.update(x.encode('utf-8'))
  hashs = hashs.hexdigest()
  return hashs
  pass

# x is what you want to loop y is how many times you want to loop it z is 0 or 1 if you want it in a var then you could use 0 or if you dont want it to show it if its in a var and 1 will make that so it does show in a var. a means that if you want to see all the gens of the looped hash or if you want the frist a lassed hash 0 = all gens 1 = frist and last gen or if you want a specific gen then type in the numer exsapel "hashlooping(x,y,z, 5) output gen 1:.... gen 5:....." 

def hashlooping(x, y, z, a):
  done = 0
  i = 0
  hasprintedonce = False
  lasshash = ""
  show = a
  var6 = 1
  var5 = y-1 # if loop=30 then this should be 29
  var7 = a
  var8 = 2
  wr(1)
  while i <= y:
    var4 = "\nGen "+str(i+1)+":\n"
    if i == y: #would tell how many times looped
      done += 1
      wr(2)
      break
    if z==1 or z=="on" or z=="n":
      if hasprintedonce == False:
        var2 = (str(x))
        print(var4+var2)
        lasshash += var2
        hasprintedonce = True
      elif hasprintedonce == True:
        var3 = hashed(lasshash)
        if show == 0:
          print(var4+var3)
          lasshash += var3
        elif show == 1:
          if var6 == var5:
            print(var4+var3)
            wr(8)
          elif var6 < var5:
            var6 += 1
          else:
            print('ERROR code: 1 ')
          lasshash += var3
        elif show >= 2:
          wr(3)
          if i == var7 and i <= var5 and i >=var8: # if 0..y == y-1
          #if 6 >= 2 and 6 <= 29
          #when i == 6 and i <= 29 and i >=2
          #when i == var7 and i <= var5 and i >=var8
            return var4+var3 #output: Gen y:....
            wr(4)
          elif var6 < var5: # is 0..y less then y-1
            wr(5)
            var6 += 1 # var6 = n -> var6 = n+1
          else:
            wr(6)
            print('ERROR code: 5 ')#print('code: 1 ')
          lasshash += var3
          wr(7)
        else:
          print('ERROR code: 2')
      else:
        print('ERROR code: 3')
    elif z==0 or z=="off" or z=="f":
      pass
    else:
      print('ERROR code: 4')
    i += 1
  if done == 1:
    return ""#var6


getspace = "\n\n\n\n\n\n\n\n"
gs = getspace

#print(s+ns+s2+ns+s3+ns+str(h2)+ns+str(h3)+ns+dk2+ns+str(h4))


#print(h2)
hashing1 = "hello"
hashing2 = hashed(hashing1)


var1 = hashlooping(hashing2, 30, 1, 6)


print(str(var1)+gs)