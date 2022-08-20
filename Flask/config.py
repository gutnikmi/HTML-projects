import os,uuid


class Config(object):
    secret = uuid.uuid4()
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
# uuid.uuid4()
