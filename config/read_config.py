import os
import configparser
from config import getpathinfo

path = getpathinfo.get_path()

config_path = os.path.join(path,'config.ini')

config = configparser.ConfigParser()

config.read(config_path,encoding='utf-8')


class ReadConfig():

    def get_link(self,name):
        value = config.get('LINK',name)
        return value
    def get_email(self,name):
        value = config.get('EMAIL',name)
        return value


if __name__ == '__main__':
    print(ReadConfig().get_link('baseurl'))
    print(ReadConfig().get_email('on_off'))
