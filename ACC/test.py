import os
print os.path.realpath(__file__)
print os.path.abspath(os.path.realpath(__file__)+"/python-oauth2") #+ '/../../../'
# print os.path.abspath(os.path.realpath(__file__)+"/../../python-oauth2") #+ '/../../../'
print os.path.abspath(os.path.realpath(__file__) + '/CoAPthon')
print os.path.abspath(os.path.realpath(__file__))
print os.path.basename(__file__)