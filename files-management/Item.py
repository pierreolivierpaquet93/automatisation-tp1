# https://docs.python.org/3/library/datetime.html
import datetime as dt

class Item():
	'''
		NAME: piss
	'''
	def __init__(
		self,
		name:str,
		absolute_path:str,
		creation:dt.datetime
	) -> None:
		self._name		= name
		self._path		= absolute_path
		self._creation	= creation
		self._modified	= creation
