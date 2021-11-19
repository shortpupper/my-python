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

ns= "\n\n"

#m = hashlib.sha256()
#m.update(b"Nobody inspects")
#m.update(b" the spammish repetition")
#m.digest()
#m.digest_size
#m.block_size
#
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


#print(s+ns+s2+ns+s3+ns+str(h2)+ns+str(h3)+ns+dk2+ns+str(h4))


#print(h2)
hashing1 = "hello"
hashing2 = hashed(hashing1)

h = looping(hashing2, 4)


