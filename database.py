import sqlite3
from internet import check_connection

def create_conn():
    
    conn = sqlite3.connect("mem.db")
    return conn

def get_qna():

    con = create_conn()
    cur = con.cursor()

    cur.execute("SELECT * FROM que")

    return cur.fetchall()

#for feedind into the data base
def insert_qna(question,answer):

    con = create_conn()
    cur = con.cursor()
    query = "INSERT INTO que values('"+question+"','"+answer+"')"

    cur.execute(query)
    con.commit()



def get_answer(question):

    r = get_qna()
    answer = ""
    for row in r:
        if row[0] in question:
            answer = row[1]
            break
    
    return answer



def get_name():

    con = create_conn()
    cur = con.cursor()
    query = "select value from assist_mem where name = 'assistant name'"

    cur.execute(query)
    return cur.fetchall()[0][0]


def update_name(new_name):

    con = create_conn()
    cur = con.cursor()
    query = "update assist_mem set value = '"+new_name+"' where name = 'assistant name'"

    cur.execute(query)
    con.commit()
    
#update_name("friday")
#print(get_name())

def update_last_seen(last_seen_date):

    con = create_conn()
    cur = con.cursor()
    query = "update assist_mem set value = '"+str(last_seen_date)+"' where name = 'last_seen_date'"

    cur.execute(query)
    con.commit()


def get_last_seen():

    con = create_conn()
    cur = con.cursor()
    query = "select value from assist_mem where name = 'last_seen_date'"

    cur.execute(query)
    return (cur.fetchall()[0][0])



def turn_on_speech():

    if (check_connection):

        con = create_conn()
        cur = con.cursor()
        query = "update assist_mem set value = 'on' where name = 'speech'"

        cur.execute(query)
        con.commit()

        return "speech turned on"

    else:

        return "please turn on internet !"

def turn_off_speech():

    con = create_conn()
    cur = con.cursor()
    query = "update assist_mem set value = 'off' where name = 'speech'"

    cur.execute(query)
    con.commit()
    return "ok i won't speak"

def speak_is_on():

    con = create_conn()
    cur = con.cursor()
    query = "select value from assist_mem where name = 'speech'"

    cur.execute(query)
    ans = (cur.fetchall()[0][0])

    if ans == "on":
        return True
    
    else:
        return False