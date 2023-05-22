import os


adb_path = '/Users/wangqiang/Library/Android/sdk/platform-tools/'


def get_device_list():
    result = os.popen(adb_path + 'adb devices').readlines()
    devices = []
    for r in result:
        if '\tdevice' in r:
            devices.append(r.split('\t')[0])
    return devices


def install_apk(device, apk_path):
    os.system(adb_path + 'adb -s %s install -r %s' % (device, apk_path))


