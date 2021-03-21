import imapclient
from datetime import date

# 参数
qq_site = 'imap.qq.com'
qq_account = '****@qq.com'
qq_code = '****'
qq_box_name = 'INBOX'
mai_state = 'UNSEEN'

# 创建一个IMAPClient对象，大多数邮件提供商要求SSL加密，传入ssl = True关键字参数
imapObj = imapclient.IMAPClient(qq_site, ssl=True)
imapObj.login(qq_account, qq_code)
imapObj.select_folder(qq_box_name, readonly=True)

# 读取 指定日期后（包含）的未读邮件 注意写法
today = date.today()
print(today)
UIDs = imapObj.search([u'SINCE', date(today.year, today.month, today.day), mai_state])
# UIDs = imapObj.search([u'SINCE', date(2021, 3, 12), mai_state])

# 记录邮件条数
count = 0
for i in UIDs:
    count += 1

# 结果
print('今日未读邮件数',count,sep=":")

