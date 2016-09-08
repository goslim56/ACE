import os
print os.path.realpath(__file__)
print os.path.dirname(__file__)
print os.path.abspath(os.path.realpath(__file__))