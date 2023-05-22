import urllib.request


header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Cookie': ''
}


def down_file(url, file):
    response = httprequest(url=url, header=header)
    data = response.read()
    with open(file, 'w') as f:
        f.write(data)


def httprequest(url, header):
    req = urllib.request.Request(url=url, header=header)
    response = urllib.request.urlopen(req)
    return response