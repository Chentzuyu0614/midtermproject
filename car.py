#!C:\Python39\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi #import goods as gb


from dbConfig import conn, cur
#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>完成</title>
</head>
<body>
""")

#查詢
"""form = cgi.FieldStorage()
id=form.getvalue('i')
amount=form.getvalue('j')
sql="insert into goods (name,price,amount) values (%s,%s,%s);"
cur.execute(sql,(name,price,amount))

print("商品已加入!")"""


sql="select id, name, price, amount from goods order by amount desc;"
cur.execute(sql)
records = cur.fetchall()
for (name, price, amount) in records:
	print(f"<p>商品:{name} 標題:{price} 數量:{amount}</p>")
conn.commit()
print("<br><a href='main.html'>回商城</a>")
print("</body></html>")

"""
id, name, price, amount
id, title,msg, nickname,likes"""