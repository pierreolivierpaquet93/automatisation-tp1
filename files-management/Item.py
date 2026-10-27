# https://docs.python.org/3/library/datetime.html
import	datetime	as		dt
from	pathlib		import	Path

class Item():
	def __init__(
		self,
		name:str,
		path:str,
		creation:dt.datetime
	) -> None:
		self.__name		= name
		self.__path		= path
		self.__creation	= creation
		self.__modified	= creation

	def setName(
		self,
		name:str
	) -> None: 
		self.__name = name

	def getName( self ) -> str:
		return self.__name

	def setPath(
		self,
		path:str
	) -> None:
		self.__path = path

	def getPath( self ) -> str:
		return self.__path

	def getAbsolutePath( self ) -> str:
		return str( Path( self.__path, self.__name ).absolute() )

	def getCreation( self ) -> dt.datetime:
		return self.__creation
