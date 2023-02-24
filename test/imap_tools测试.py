# _*_ coding : utf-8 _*_
# @Time : 2023-02-23 13:52
# @Author : wws
# @File : test_02
# @Project : python基础
import datetime
from imap_tools import MailBox, AND, OR, NOT
import re

mail_pass = 'MZquSz2dXuaTQ0ob'
with MailBox('imap.feishu.cn').login('wensong.wang@ziel.cn', mail_pass, initial_folder='INBOX') as mailbox:
    # 筛选邮件
    # criteria_01 = AND(NOT(OR(date=[dt.date(2020, 1, 11), dt.date(2020, 1, 12)])), flagged=True, subject='你好')
    start_time = datetime.date.today()
    end_time = start_time - datetime.timedelta(days=3)
    # criteria = AND(date=[start_time, end_time], from_='zhiyi.lin@ziel.cn')
    criteria = AND(date=[end_time, start_time])
    criteria01 = AND(date_gte=datetime.date(2023, 2, 21))
    # 正则表达式
    pattern = re.compile(r'(HBL |File_)((.*?)(,|\d$))')
    hbl_list = []
    uid_list = []
    for msg in mailbox.fetch(criteria01, charset='utf-8'):  # mailbox.uids() 保存所有mailbox的uid(str类型)  但是uid跟列表下标不一样
        if 'zhiyi.lin@ziel.cn' not in msg.from_:
            continue
        subject = msg.subject
        hbl_file = pattern.search(subject)
        if hbl_file is None:
            continue
        attach = msg.attachments
        print(type(attach), "========type(attach)")
        print(type(attach[0].filename), "========type(attach[0])", attach[0].filename)
        print(attach, "=======attach")
        uid = msg.uid
        uid_list.append(uid)
        # print(type(mailbox.uids()), "===mailbox")
        print(subject, "==", hbl_file.group(), "==", uid)  # <class 'str'>  <class 'str'>
    print(uid_list)
    for u in uid_list:
        # print(type(mailbox.uids()))
        # print(mailbox.uids())
        # print(type(mailbox.uids()[0]))
        # print(mailbox.uids()[0])

        mailbox_index = mailbox.uids().index(uid)
        print(mailbox_index, "=======mailbox_index")
        mailbox.move(mailbox.uids()[mailbox_index], 'HBL')

