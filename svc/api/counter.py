import sqlite3

class Counter:
	"""
	A very simple global counter application.
	"""
	@staticmethod
	def getCounterValue():
		"""
		Returns the current value of the global counter.
		"""
		conn = sqlite3.connect('ivoirians.db')
		cur = conn.cursor()
		cur.execute("SELECT * FROM tb_Counter")
		ret = cur.fetchone()[0]	
		conn.close()	
		return ret

	@staticmethod
	def addCounterValue():
		"""
		Add one to the current value of the global counter.

		Returns the new value of the counter.
		"""
		conn = sqlite3.connect('ivoirians.db')
		cur = conn.cursor()
		cur.execute("SELECT * FROM tb_Counter")
		prev = cur.fetchone()[0]
		cur.execute("UPDATE tb_Counter SET intCounterValue=?", (int(prev) + 1,))
		conn.commit()
		conn.close()
		return int(prev) + 1