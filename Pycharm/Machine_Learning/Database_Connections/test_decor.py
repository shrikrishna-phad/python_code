from decorator import connect_to_mysql

@connect_to_mysql
def add_1employee(conn,cur,*args):
    if len(args) == 1:
        var = args
        cur.execute(var)
        try:
            data = cur.fetchall()
        except:
            pass
        else:
            for i in data:
                print(i)

        conn.commit()
    elif len(args) == 2:
        q,values = args[0],args[1]
        cur.executemany(q,values)
        conn.commit()
    else:
        pass
var = "insert into employee values (116,'sanna','6000')"
q = "insert into employee values (%s,%s,%s)"
values = [(104,'surendar',2345),
          (106,'arnav',7654)]
fetch = "select * from employee"

add_1employee(var)