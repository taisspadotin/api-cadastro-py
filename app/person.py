from flask import Blueprint, current_app, request, jsonify
import sqlite3
import json

bp_person = Blueprint('person', __name__)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@bp_person.route('/', methods=['GET'])
def home():
	print('teste')
	return 'home'

@bp_person.route('/person', methods=['GET'])
def all():
	try:
		sqliteConnection = sqlite3.connect('register.db')
		cursor = sqliteConnection.cursor()
		print("Successfully Connected to SQLite")

		sqlite_insert_query = """SELECT id, name, email, cpf, rg FROM person"""
		count = cursor.execute(sqlite_insert_query)
		records = cursor.fetchall()
		data = {'people': [],'info':[{"records":  len(records)}]}
		#sqliteConnection.commit()
		#print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
		for row in records:
			id = row[0]
			name = row[1]
			email = row[2]
			cpf = row[3]
			rg = row[4]
			person = {'id': id, "name": name, "email": email, "cpf": cpf, "rg": rg}
			data['people'].append(person)
		cursor.close()
		print(data)
	except sqlite3.Error as error:
		print("Failed to insert data into sqlite table", error)
	finally:
		if (sqliteConnection):
			sqliteConnection.close()
			print("The SQLite connection is closed")

	return jsonify(data)

