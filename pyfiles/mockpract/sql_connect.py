def create_co():
    import sqlite3
    dbco=sqlite3.connect('anju.db')
    return dbco
co=create_co()
def create_table(co):
    cro=co.cursor()
    cro.execute('create table emp(empno integer primarykey,ename text)')
    co.commit()
    print('table is created')
#create_table(co)
def insert_data(co):
    cro=co.cursor()
    cro.execute('insert into emp values(1432,"guna")')
    cro.execute('insert into emp values(1234,"sum")')
    co.commit()
    print('data insertion is done')
#insert_data(co)
def retrieve(co):
    cro=co.cursor()
    queryset=cro.execute('select * from emp')
    for i in queryset:
        print(i)
retrieve(co)
def update_data(co):
    cro=co.cursor()
    cro.execute('update emp set ename="anjali" where ename="guna" ')
    co.commit()
    print('updation done')
#update_data(co)
#retrieve(co)
def delete_data(co):
    cro=co.cursor()
    cro.execute('delete from emp where ename="sum"')
    co.commit()
delete_data(co)
retrieve(co)





    
