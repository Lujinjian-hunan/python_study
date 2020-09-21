import tools


def main():
    table_name = input('请输入你要导出的表名：').strip()
    table_exist_sql = "SELECT table_name FROM information_schema.TABLES WHERE table_name ='%s';" % table_name
    if tools.execute_sql(table_exist_sql):
        query_sql = 'select * from %s;' % table_name
        data = tools.execute_sql(query_sql)
        if data:
            tools.write_excel(table_name,data)
            print('导出完成')
        else:
            print('表中无数据，无法导出')
    else:
        print('表不存在！')



if __name__ == '__main__':
    main()



