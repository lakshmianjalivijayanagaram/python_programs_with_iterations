def create_co():
    import sqlite3
    co=sqlite3.connect('an.db')
    return co
dbco=create_co()
def create_table(dbco):
    cro=dbco.cursor()
    ab=cro.execute('create table emp1(empno int primarykey,ename text)')
    dbco.commit()
    print('table is created')
#create_table(dbco)
def insert_data(dbco):
    cro=dbco.cursor()
    cro.execute('insert into emp1 values(1234,"anjali")')
    cro.execute('insert into emp1 values(2345,"amma")')
    dbco.commit()
    print('values are inserted')
#insert_data(dbco)
def retrieve_data(dbco):
    cro=dbco.cursor()
    queryset=cro.execute('select * from emp1')
    for i in queryset:
        print(i)
#retrieve_data(dbco)
def update_data(dbco):
    cro=dbco.cursor()
    cro.execute('update emp1 set empno=5678 where empno=1234')
    dbco.commit()
#update_data(dbco)
retrieve_data(dbco)
def del_data(dbco):
    cro=dbco.cursor()
    cro.execute('delete from emp1 where ename="anjali" ')
    print('deleteon done')
del_data(dbco)
retrieve_data(dbco)
