# _*_ coding : utf-8 _*_
# @Time : 2023-02-24 9:12
# @Author : wws
# @File : 荷兰关单RPA
# @Project : python基础
import datetime
import re
from imap_tools import MailBox, AND, OR, NOT

def filter_message(attachment, send):
    if send == 'OFR':
        for a in attachment:
            # if ('Duty' in a.filename) or ('Clearance' in a.filename):
            if ('DGF' in a.filename) or ('Clearance' in a.filename):  # 测试
                return 'OFR'
    elif send == 'DGF':
        if len(attachment) == 1:
            return 'DGF'
    elif send == 'EMDO' or send == 'MERGED':
        emdo_number = 0
        merged_number = 0
        for a in attachment:
            file = a.filename
            if 'EMDO' in file:
                emdo_number += 1
            elif 'Merged' in file:
                merged_number += 1
        if emdo_number == 3:
            return 'EMDO'
        elif merged_number == 1:
            return 'MERGED'



mail_pass = 'MZquSz2dXuaTQ0ob'
with MailBox('imap.feishu.cn').login('wensong.wang@ziel.cn', mail_pass, initial_folder='INBOX') as mailbox:
    criteria = AND(date_gte=datetime.date(2023, 2, 21))
    pattern = re.compile(r'(HBL |File_)((.*?)(,|\d$))')
    uid_list = []
    for msg in mailbox.fetch(criteria, charset='utf-8'):
        sender = msg.from_
        uid = msg.uid
        subject = msg.subject
        attachments = msg.attachments
        # zhiyi.lin@ziel.cn
        # if 'noreply.edmemea@dhl.com' in sender:  # 根据发件人筛选
        if 'zhiyi.lin@ziel.cn' in sender:  # 测试
            if ('OFR' in subject) and ('HBL' in subject) and ('NLRTM' in subject):
                file_name = filter_message(attachments, send='OFR')
                if file_name is None:
                    continue
                item = {file_name: uid}
                uid_list.append(item)
            elif ('DGF' in subject) or ('CDZ' in subject):
                file_name = filter_message(attachments, send='DGF')
                if file_name is None:
                    continue
                item = {file_name: uid}
                uid_list.append(item)
        # if ('attila.lorincz@dhl.com' in sender) or ('viktoria.lovacsi@dhl.com' in sender):
        if ('zhiyi.lin@ziel.cn' in sender) or ('zhiyi.lin@ziel.cn' in sender):
            file_name = filter_message(attachments, send='EMDO')
            if file_name is None:
                continue
            item = {file_name: uid}
            uid_list.append(item)

    print(uid_list)
    for uid_item in uid_list:
        # print(type(uid_item), "===type(uid_item)", uid_item, "=====uid_item")
        keys = dict(uid_item).keys()
        # print(type(keys), "=====type(keys)", keys, "==keys")
        for file_name in keys:
            print(mailbox.uids())
            mail_index = mailbox.uids().index(uid_item[file_name])
            mailbox.move(mailbox.uids()[mail_index], file_name)


