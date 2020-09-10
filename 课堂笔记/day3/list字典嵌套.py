# coding=utf-8
info = {
    'lgy':{
        'age':'18',
        'addr':'beijing',
        'cars':['bmw','ben-z','audi']
    },
    'fd':{
        'house':{
            'bj':['海淀区','昌平区','朝阳区','西城区'],
            'sh':['静安区','闸北区']
        },
        'money':500
    }
}

# lgy,又买了一辆五菱宏光
# fd，卖了北京昌平的房子，资金又增加了4000000
info['lgy']['cars'].append('五菱宏光')
info['fd']['house']['bj'].remove('昌平区')
info['fd']['money'] += 4000000
print(info)