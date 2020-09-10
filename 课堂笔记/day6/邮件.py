import yagmail  # 发附件如果是中文，会乱码
import yamail
smtp = yamail.SMTP(host= 'smtp.qq.com',  # 邮箱服务器
       user='■■■■■■■■■■■',  # 邮箱账号
       password='■■■■■■■■■■■'  # 如果是163、qq等邮箱，填授权码，公司邮箱填密码
       )

smtp.send(to=['■■■■■■■■■■■'],  # 收件人，发送给多人写list
          subject='你好，请查收附件',  # 主题
          cc=['■■■■■■■■■■■'],  # 抄送人，发送给多人写list
          contents='邮箱正文',  # 邮箱正文
          attachments=['笔记.txt']  # 附件，发送给多人写list
          )
