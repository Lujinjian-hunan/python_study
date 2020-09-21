#作业1、

# https://qun.qq.com/cgi-bin/qun_mgr/search_group_members
# gc: 1078641913
# st: 0
# end: 20
# sort: 0
# bkn: 1265428885

# cookie: pgv_pvi=6319469568; RK=3YYhxjp3YS; ptcz=af8ebcc734b1e327a1a097d11d75e8bb0607135a77048a18ac47e1ebc9f6d114; uin=o0511402865; skey=@0ofxhsvKW; p_uin=o0511402865; pt4_token=-QGBjgO*ckONXnbyec-oBbEwb*YOqz9CryFXU3JqrKc_; p_skey=yh-ajMda68Fez58iUMD13D1pmx1UTP7nN5RLT04g8jE_; traceid=f7a905269f
import requests,os

# if not os.path.exists('qq_pics'):
#     os.mkdir('qq_pics')
# os.chdir('qq_pics')

#0,20,20,40,40,60

# max_count = 1000
# gc = 1078641913
bkn = 1265428885
cookies='pgv_pvi=6319469568; RK=3YYhxjp3YS; ptcz=af8ebcc734b1e327a1a097d11d75e8bb0607135a77048a18ac47e1ebc9f6d114; uin=o0511402865; skey=@0ofxhsvKW; p_uin=o0511402865; pt4_token=-QGBjgO*ckONXnbyec-oBbEwb*YOqz9CryFXU3JqrKc_; p_skey=yh-ajMda68Fez58iUMD13D1pmx1UTP7nN5RLT04g8jE_; traceid=f7a905269f'

# group_member_url = 'https://qun.qq.com/cgi-bin/qun_mgr/search_group_members'
# size = 40
# count = 0
# for j in range(0,max_count+1,size):#0,20 3
#     #0,20, 21,41, 42:62  63:83   84:104
#     #0,20  20,40  40,60  60:80   80 :100
#     data = {'gc':gc,'st':j+count,'end':j+size+count,'bkn':bkn}
#     headers = {'cookie':cookies}
#     r = requests.post(group_member_url,data,headers=headers)
#     members = r.json()
#     count+=1
#     if 'mems' in members:
#         pic_url = 'https://q4.qlogo.cn/g?b=qq&nk=%s&s=140'
#         mems = members.get("mems")
#         for m in mems:
#             qq = m.get("uin")
#             name = m.get('card') if m.get('card') else m.get('nick')
#             r = requests.get(pic_url % qq )
#             with open(name+'.jpg','wb') as fw:
#                 fw.write(r.content)
#             print('下载完成 %s'%name)
#     else:
#         print('没有获取到群成员信息')
#         break

class DownLoadQQGroupMemberPic:
    group_member_url = 'https://qun.qq.com/cgi-bin/qun_mgr/search_group_members'
    pic_url = 'https://q4.qlogo.cn/g?b=qq&nk=%s&s=140'
    max_count = 1000
    size = 40
    dir_name = 'qq_pics'
    def __init__(self,gc):
        self.gc = gc
        self.mkdir()

    def mkdir(self):
        if not os.path.exists(self.dir_name):
            os.mkdir(self.dir_name)


    def get_member_info(self,gc,st,end):
        '''获取群成员的信息'''
        data = {'gc': gc, 'st':st, 'end': end, 'bkn': bkn}
        headers = {'cookie': cookies}
        r = requests.post(self.group_member_url, data, headers=headers)
        members = r.json()
        return members

    def save_pic(self,name,content):
        with open(name + '.jpg', 'wb') as fw:
            fw.write(content)

    def down_pic(self,qq):
        r = requests.get(self.pic_url % qq)
        return r.content

    def down_qq_pic(self,mems):
        for m in mems:
            qq = m.get("uin")
            name = m.get('card') if m.get('card') else m.get('nick')
            content = self.down_pic(qq)
            self.save_pic(name,content)

    def main(self):
        count = 0
        for j in range(0, self.max_count + 1,self.size ):  # 0,20 3
            mems = self.get_member_info(self.gc,j+count,j+self.size+count)
            if 'mems' in mems:
                self.down_qq_pic(mems)


##多线程、多进程
#自己实现一个自动化
#