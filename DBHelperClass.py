import sqlite3

class connection():
	@staticmethod
	def connect():
		global sqliteConnection
		sqliteConnection = sqlite3.connect('fonts.db')
		global cursor
		cursor = sqliteConnection.cursor()
		return 'connection established!'

	@staticmethod
	def close():
		if sqliteConnection:
			sqliteConnection.close()
			return 'SQL connection closed'

class all():
	@staticmethod
	def alltags():
		connection.connect()

		sqlite_select_Query = 'SELECT * FROM tTags;'
		cursor.execute(sqlite_select_Query)
		record = cursor.fetchall()
		print('SQL tTags answered with: ', record)
		cursor.close()

		connection.close()
		return

	@staticmethod
	def allcategories():
		connection.connect()
		sqlite_select_Query = 'SELECT * FROM tcategorys;'
		cursor.execute(sqlite_select_Query)
		record = cursor.fetchall()
		print('SQL tcategorys answered with: ', record)
		cursor.close()

		connection.close()
		return

class search:

	@staticmethod
	def tags(chosentags):
		connection.connect()
		stringify = ' OR '.join(chosentags)
		sqlite_select_Query = ("""SELECT tfonts.cfont, tTags.ctags 
		FROM font_tag 
		INNER JOIN tfonts ON font_tag.font_id=tfonts.font_id
		INNER JOIN tTags ON font_tag.tag_id=tTags.tags_id
		WHERE ctags =""") 
		cursor.execute(sqlite_select_Query + stringify)
		record = cursor.fetchall()
		print('SQL chosentags answered with: ', record)

	
	@staticmethod
	def category(chosencategory):
		connection.connect()
		stringify = ' OR '.join(chosencategory)
		sqlite_select_Query = ("""SELECT tfonts.cfont, tcategorys.ccategory 
		FROM category_font 
		INNER JOIN tfonts ON category_font.font_id=tfonts.font_id
		INNER JOIN tcategorys ON category_font.category_id=tcategorys.category_id
		WHERE ccategory = """) 
		cursor.execute(sqlite_select_Query + stringify)
		record = cursor.fetchall()
		print('SQL chosencategory answered with: ', record)
		