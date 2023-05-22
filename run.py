import adbtools
import downtools
import mailtools

path = '/Users/wangqiang/PycharmProjects/python3/'
url = ''
version = ''

down = mailtools.mail_parse()
url = down['url']
version = down['version']
file = path+'app-xiaohongwu-staging'+version+'.apk'
downtools.down_file(url, file)
devices = adbtools.get_device_list()
for device in devices:
    adbtools.install_apk(device, file)




