import psycopg2

con = psycopg2.connect(
  database="app", 
  user="user", 
  password="user", 
  host="localhost", 
  port="5432"
)
cur = con.cursor() 
print("Database opened successfully")
def showAuthors():
	sql = "SELECT ID_AUTH, NAME FROM AUTHORS"
	try:
		cur.execute(sql)
		results = cur.fetchall()
		for row in results:
			id = row[0]
			name = row[1]
			print("%d\t%s" % (id, name))
	except Exception as e:
			print(e)
showAuthors()
def addAuthor(id, name):
	sql = "INSERT INTO AUTHORS (ID_AUTH, NAME) VALUES (%d, '%s')" %(id, name)
	try:
		cur.execute(sql)
		con.commit()
		print("Автора %s Успішно додано!" % name)
		return True
	except Exception as e:
			print(e)
			con.rollback()
			return False
addAuthor(id=3, name="LES_PODEREVIANSKYI")

def deleteAuthor(id):
	sql = "DELETE FROM AUTHORS WHERE ID_AUTH = %d" % id
	try:
		cur.execute(sql)
		con.commit()
		print("Автора з ідентифікатором %s успішно видалено!" % id)
		return True
	except Exception as e:
			print(e)
			con.rollback()
			return False
deleteAuthor(id=3)
