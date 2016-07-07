import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = str(row[idx])
    return d

def query(string_query, params_tuple, one = False):
	conn = sqlite3.connect('ivoirians.db')
	conn.row_factory = dict_factory
	cur = conn.cursor()
	cur.execute(string_query, params_tuple)
	ret = cur.fetchone() if one else cur.fetchall()
	conn.commit()
	conn.close()	
	return ret
	