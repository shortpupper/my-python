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
    print('ERROR code: 7 ')

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


# x is what you want to loop y is how many times you want to loop it z is 0 or 1 if you want it in a var then you could use 0 or if you dont want it to show it if its in a var and 1 will make that so it does show in a var. a means that if you want to see all the gens of the looped hash or if you want the frist a lassed hash 0 = all gens 1 = frist and last gen or if you want a specific gen then type in the numer exsapel "hashlooping(x,y,z, 5) output gen 1:.... gen 5:....." 

#hashed_256("hello")
def hashed_blake2b(x):
  hashs = blake2b(digest_size=64)
  hashs.update(x.encode('utf-8'))
  hashs = hashs.hexdigest()
  return hashs
  pass

#print(hashlib.sha256(b"Nobody inspects the spammish repetition").hexdigest())

def hashlooping(wordtohash, howmanytimestohash, unused, whatgen, whathash):
  import hashlib
  from hashlib import blake2b
  from random import randrange
  getspace = "\n\n\n\n\n\n\n\n"
  gs = getspace
  #from random import randrange
  #from random import random, randrange
  #wordtohash = x
  #howmanytimestohash = y
  #unused = z
  #whatgen = a
  #whathash = h
  x = wordtohash
  y = howmanytimestohash
  z = unused
  a = whatgen
  h = whathash
  
  def hashed_blake2b(x):
    hashs = blake2b(digest_size=64)
    hashs.update(x.encode('utf-8'))
    hashs = hashs.hexdigest()
    return hashs
    pass
  def hashed_512(x):
    hashs = hashlib.sha512(x.encode('utf-8')).hexdigest()
    return hashs
    pass
  def hashed_256(x):
    hashs = hashlib.sha256(x.encode('utf-8')).hexdigest()
    return hashs
    pass
  def hashed_224(x):
    hashs = hashlib.sha224(x.encode('utf-8')).hexdigest()
    return hashs
    pass
  def hashed_128(x):
    hashs = hashlib.sha128(x.encode('utf-8')).hexdigest()
    return hashs
    pass
  def hashed_384(x):
    hashs = hashlib.sha384(x.encode('utf-8')).hexdigest()
    return hashs
    pass
  def hashed_1(x):
    hashs = hashlib.sha1(x.encode('utf-8')).hexdigest()
    return hashs
    pass
  def hashed_none(x):
    return x
    pass
  hasher = "ERROR no input"
  if h=="-1" or h=="1" or h=="224" or h=="256" or h=="384" or h=="blake2b" or h=="512":
    lasshash = ""
    if h =="256":
      hasher = hashed_256(x)
      lasshash += hasher
      hasher2 = hashed_256(lasshash)
    elif h =="512":
      hasher = hashed_512(x)
      lasshash += hasher
      hasher2 = hashed_512(lasshash)
    elif h =="1":
      hasher = hashed_1(x)
      lasshash += hasher
      hasher2 = hashed_1(lasshash)
    elif h =="128":
      hasher = hashed_128(x)
      lasshash += hasher
      hasher2 = hashed_128(lasshash)
    elif h =="224":
      hasher = hashed_224(x)
      lasshash += hasher
      hasher2 = hashed_224(lasshash)
    elif h =="384":
      hasher = hashed_384(x)
      lasshash += hasher
      hasher2 = hashed_384(lasshash)
    elif h =="-1":
      hasher = hashed_none(x)
      lasshash += hasher
      hasher2 = hashed_none(lasshash)
    pass
    pass
  else:
    print('ERROR code: 9 ')
  done = 0
  if z == -1:
    i = -1
  elif z == 1:
    i = 0
  hasprintedonce = False
  lasshash = ""
  show = a
  var6 = 1
  var5 = y-1 # if loop=30 then this should be 29
  if a == "r" or a == "random":
    var7 = ""
  elif a >= 0:
    var7 = a
  var8 = 2
  failsafe = 0
  var9 = randrange(var8, y) #cange random.randrange to randrange
  wr(1)
  while i <= y:
    if failsafe == 32:
      return  "FAILSAFE INGAED STOPING NOW"
    if z == (-1):
      var4 = "\nGen "+str(i)+":\n"
      var3 = hasher2
      return var4+var3
    elif z==1 or z=="on" or z=="n":
      if hasprintedonce == False:
        var4 = "\nGen "+str(i+1)+":\n"
        var2 = (str(hasher))
        print(var4+var2)
        lasshash += var2
        hasprintedonce = True
      elif hasprintedonce == True:
        var4 = "\nGen "+str(i)+":\n"
        var3 = hasher2
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
        elif show == "random" or show == "r":
          wr(11)
          if i == var9 and i <= y and i >= var8: # if 0..y == y-1
            return var4+var3 #output: Gen y:....
            wr(9)
          elif var6 < var5: # is 0..y less then y-1
            #print(i)
            wr(10)
            var6 += 1 # var6 = n -> var6 = n+1
          else:
            wr(12)
            print('ERROR code: 8 ')#print('code: 1 ')
          lasshash += var3
          wr(13)
        elif show > 1:
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
          elif var7 > var8:
            wr(6)
            print('ERROR code: "exceeds max gen" ')
          else:
            wr(14)
            print('ERROR code: 5 ')#print('code: 1 ')
          lasshash += var3
          wr(7)
        else:
          print('ERROR code: 2')
      else:
        print('ERROR code: 3')
    elif z==0 or z=="off" or z=="f":
      pass
    failsafe += 1
  if done == 1:
    return ""#var6
#

getspace = "\n\n\n\n\n\n\n\n"
gs = getspace

#print(s+ns+s2+ns+s3+ns+str(h2)+ns+str(h3)+ns+dk2+ns+str(h4))


#print(h2)

hashing1 = "hello"
hashing2 = hashed_blake2b(hashing1)

#var1 = hashlooping("hello", 400, 1, 3, "256")
#
#print(var1)

#var1 = hashlooping("hello", 600, 1, 2, "256")
#p1 = str(hashlooping("hello", 600, 1, 2, "256"))+gs

#xs = str(hashlooping("hello", 600, 1, 2, "256"))+gs
#print(xs)