# _*_ coding : utf-8 _*_
# @Time : 2023-02-22 17:45
# @Author : wws
# @File : test_01
# @Project : python基础
import datetime
import datetime as dt
from imap_tools import MailBox, AND, OR, NOT
mail_pass = 'MZquSz2dXuaTQ0ob'  # 使用的邮箱密码，如果有授权码，填写授权码
mailbox = MailBox('imap.feishu.cn')
with mailbox.login('wensong.wang@ziel.cn', mail_pass, initial_folder='INBOX') as mailbox:
    start_time = datetime.datetime.now()
    for msg in mailbox.fetch(reverse=True, bulk=True):
        """"
            mailbox.fetch() parameters that can be placed
            criteria='ALL' message search criteria
            limit=None  limit on the number of read emails,useful for actions with a large number of messages
            miss_no_uid=True miss emails without uid
            mark_seen=True  mark emails as seen on fetch
            reverse=False in order from eht larger date to the smaller
            headers_only=False  get only email headers(without text,html,attachments)
            bulk=False False-fetch each message separately per N commands-low memory consumption,slow
                        True-fetch all messages per 1 command-high memory consumption,fast
        """
        """
            MailBox().fetch().attributes or email attributes 
            for msg in mailbox.fetch():
                msg.uid  # str | None:'123'
                msg.subject  # str: 'some subject'
                msg.from_  # str: 'Bartölke@ya.ru'
                msg.to  # tuple: ('iam@goo.ru', 'friend@ya.ru', )
                msg.cc  # tuple: ('cc@mail.ru', )
                msg.bcc  # tuple: ('bcc@mail.ru', )
                msg.reply_to  # tuple: ('reply_to@mail.ru', )
                msg.date  # datetime.datetime:
                msg.date_str  # str: original date
                msg.text  # str: 'Hello name'
                msg.flags  # tuple: ('\\Seen', '\\Flagged', 'ENCRYPTED')
                msg.headers  # dict:{'': ''}
                msg.size_rfc822  # int: 20664 bytes
                msg.size  # int: 20377 bytes
        """
        """
           you can use 3 types for "criteria" argument of mailbox methods:fetch, uid, numbers:
            from imap_tools import AND
            mailbox.fetch(AND(subject='weather'))  # query, the str-like object
            mailbox.fetch('TEXT "hello"')  # str
            mailbox.fetch(b'TEXT "\xd1\x8f"' ) # bytes, #charset arg is ignored
            
            from imap_tools import A, AND, OR NOT
            A(text='hello', new=True)
            OR(text='helo', date=datetime.date(2000, 3, 15))
            Not(text='hello', new=True)
            A(OR(from_='from@ya.ru', text='the text'), NOT(OR(A(answered=False), A(new=True))), to='to@ya.ru')
        """
        """
            for actions with a large number of messages imap command may be too larger and will
            cause exception at server side, use 'limit' argument for fetch in this case
            with MailBox('imap.mail.com').login('test@mail.com', 'pwd', initial_folder='INBOX') as mailbox:
                # COPY messages with uid in 23,27 from current folder to folder1
                mailbox.copy('23,27', 'folder1')
                # MOVE all messages from current folder to INBOX/folder2
                mailbox.move(mailbox.uids(), 'INBOX/folder2')
                # DELETE message with 'cat' word in its html from current folder
                mailbox.delete([msg.uid for msg in mailbox.fetch() if 'cat' in msg.html])
        """
        mailbox.uids()
        print(type(mailbox.fetch()))  # <class 'generator'> 生成列表和元组的时候 常常使用生成器
        print(msg.date, "=========date")
        # print(msg.subject, "=========subject")
        # print(msg.text, "==========text")
        # print(msg.html, "=======html")
    end_time = datetime.datetime.now()
    print(end_time-start_time)



