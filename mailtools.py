import imaplib
import email
import re
from bs4 import BeautifulSoup

mail = imaplib.IMAP4_SSL('imap.qiye.aliyun.com', 993)

mail.login('qiang.wang@hznovi.com', 'Wang1989')

mail.select('HZYUN')

status, email_ids = mail.search(None, 'ALL')


def mail_parse():
    for email_id in email_ids[0].split():
        # 获取邮件内容
        status, email_data = mail.fetch(email_id, "(RFC822)")
        email_message = email.message_from_bytes(email_data[0][1])

        content = ''
        for part in email_message.walk():
            if part.get_content_type() == 'text/html':
                body = part.get_payload(decode=True).decode('utf-8')
                content = BeautifulSoup(body, 'html.parser').get_text()
                print(content)

        # 匹配链接
        url_pattern = re.compile(r'http://192\.168\.12\.165:8980/xhw_camera_android/.\S+apk')
        urls = url_pattern.findall(content)

        if len(urls) > 0:
            for url in urls[:1]:
                version = re.findall(r"tt_\S+_[0-9]+", content)[0]
                print(version)
                url = url.replace("file", "raw")
                print(url)
                down = {'url': url, 'version': version}
            break
    return down






