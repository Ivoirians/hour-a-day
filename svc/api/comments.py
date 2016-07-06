import sqlite3

class Comments:
	"""
	A very simple global comment application.

	Does not do any sort of authentication or validation.
	"""
	@staticmethod
	def getComments(page_id):
		"""
		Returns the current value of the global counter.
		"""
		conn = sqlite3.connect('ivoirians.db')
		cur = conn.cursor()
		cur.execute("SELECT * FROM tb_Comments WHERE page_id = ?", page_id)
		ret = cur.fetch()
		print ret
		conn.close()	
		return ret

	@staticmethod
	def addComment(page_id, username, comment_text):
		"""
		Adds one to the current value of the global counter.

		Returns the new value of the counter.
		"""
		conn = sqlite3.connect('ivoirians.db')
		cur = conn.cursor()
		cur.execute("SELECT intPageNumber FROM tb_Comments WHERE intPageNumber = (SELECT MAX(intPageNumber) FROM tb_Comments WHERE chvPage = ?) AND chvPage = ?", page_id, page_id)
		highestCommentNumber = cur.fetchone()[0]
		cur.execute("INSERT INTO tb_Comments VALUES (?, ?, CURRENT_TIMESTAMP, ?, ?, 0, NULL)", page_id, highestCommentNumber + 1, username, comment_text)
		conn.commit()
		conn.close()
		return 'Success'

	@staticmethod
	def deleteComment(page_id, page_number):
		"""Deletes the page_number-th column from comments of page_id."""
		conn = sqlite3.connect('ivoirians.db')
		cur = conn.cursor()
		cur.execute("UPDATE tb_Comments SET bIsDeleted=1, dtmDeleted=CURRENT_TIMESTAMP WHERE chvPage=? AND intCommentNumber=?", page_id, page_number)
		conn.commit()
		conn.close()
		return 'Success'