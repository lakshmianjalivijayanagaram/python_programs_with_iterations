def create_co():
    import sqlite3
    DBCO=sqlite3.connect('anjali.db')
    return DBCO
DBCO=create_co()
def create_table(DBCO):
    CRO=DBCO.cursor()
    CRO.execute('create table emp(emp integer primarykey,ename text)')
    DBCO.commit()
    print('table is created')
#create_table(DBCO)
def insert_data(DBCO):
    CRO=DBCO.cursor()
    CRO.execute('insert into emp values(1432,"guna")')
    CRO.execute('insert into emp values(1433,"mani")')
    CRO.execute('insert into emp values(1434,"suma")')
    CRO.execute('insert into emp values(1435,"sneha")')
    CRO.execute('insert into emp values(1436,"anjali")')
    DBCO.commit()
    print('data is inserted')
#insert_data(DBCO)
def retrieve_data(DBCO):
    CRO=DBCO.cursor()
    QUERYSET=CRO.execute('select * from emp')
    for i in QUERYSET:
        print(i)
#retrieve_data(DBCO)
def update_data(DBCO):
    CRO=DBCO.cursor()
    CRO.execute('update emp set emp=1000 where ename="mani"')
    DBCO.commit()
    print('updation is successfull')
#update_data(DBCO)
retrieve_data(DBCO)
def delete_data(DBCO):
    CRO=DBCO.cursor()
    #CRO.execute('delete from emp where ename="mani"')
    CRO.execute('delete from emp where ename="guna"')
    DBCO.commit()
    print('delection is succeful')
delete_data(DBCO)
retrieve_data(DBCO)


                
