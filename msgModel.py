#連線DB
from dbConfig import conn, cur

def getList():
	#查詢 select id, title,msg, nickname,likes from guestbook order by likes desc;
	sql="select id, name, price, amount from goods order by likes desc;"
	cur.execute(sql)
	
	records = cur.fetchall()
	#return records
	ret=[]
	
	for (id, name, price, amount) in records:
		temp={
			'id': id,
			'name': name,
			'price': price,
			'amount': amount
		}
		#print(temp)
		ret.append(temp)
		
	return ret
	
def like(id):
	global cur,conn
	sql="update goods set amount=amount-1 where id=%s;"
	cur.execute(sql,(id,))
	conn.commit()

def kill(id):
	global cur,conn
	sql="update goods set amount=amount+1 where id=%s;"
	#sql="delete from goods where id=%s;"
	cur.execute(sql,(id,))
	conn.commit()