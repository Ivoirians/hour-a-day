import sqlite3
import code
import utils
import json

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
		return json.dumps(utils.query("SELECT * FROM tb_Comments WHERE chvPage = ?", page_id))

	@staticmethod
	def addComment(page_id, username, comment_text):
		"""
		Adds one to the current value of the global counter.

		Returns the new value of the counter.
		"""
		first_row = utils.query("SELECT intCommentNumber FROM tb_Comments WHERE intCommentNumber = (SELECT MAX(intCommentNumber) FROM tb_Comments WHERE chvPage = ?) AND chvPage = ?", (page_id, page_id), True)
		highestCommentNumber = 0
		if first_row:
			highestCommentNumber = int(first_row['intCommentNumber'])
		utils.query("INSERT INTO tb_Comments VALUES (?, ?, CURRENT_TIMESTAMP, ?, ?, 0, NULL)", (page_id, highestCommentNumber + 1, username, comment_text))
		return 'Success'

	@staticmethod
	def deleteComment(page_id, page_number):
		"""Deletes the page_number-th column from comments of page_id."""
		utils.query("UPDATE tb_Comments SET bIsDeleted=1, dtmDeleted=CURRENT_TIMESTAMP WHERE chvPage=? AND intCommentNumber=?", (page_id, page_number))
		return 'Success'

	@staticmethod
	def getAllComments():
		"""Returns all comments."""
		return utils.query("SELECT * FROM tb_Comments")