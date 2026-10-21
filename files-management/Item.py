# https://docs.python.org/3/library/datetime.html
import datetime as dt

class Item():
	def __init__(
		self,
		name:str,
		absolute_path:str,
		creation:dt.datetime
	) -> None:
		self.__name		= name
		self.__path		= absolute_path
		self.__creation	= creation
		self.__modified	= creation

	def setName(
		self,
		name:str
	) -> None: 
		self.__name = name

	def getName( self ) -> None:
		return self.__name

	def setPath(
		self,
		absolute_path:str
	) -> None:
		self.__path = absolute_path

	def getPath( self ) -> None:
		return self.__path

	def getCreation( self ) -> dt.datetime:
		return self.__creation
