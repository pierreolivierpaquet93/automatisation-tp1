import	datetime	as		dt
from	pathlib		import	Path
from	time		import 	time

class Item():
	def __init__(
		self,
		name:str, # Name of the item.
		path:str, # The parent path of the item.
		creation:dt.datetime # The creation date.
	) -> None:
		self.__name		= name
		self.__path		= path
		self.__creation	= creation
		self.__modified	= creation

	def setName(
		self,
		name:str # The new item name to be stored.
	) -> None: 
		self.__name = name
		self._setModified()

	def getName( self ) -> str:
		return self.__name

	def setPath(
		self,
		path:str # Item's new parent path to be stored.
	) -> None:
		self.__path = path
		self._setModified()

	def getPath( self ) -> str:
		return self.__path

	def getAbsolutePath( self ) -> str:
		return str( Path( self.__path, self.__name ).absolute() )

	def getCreation( self ) -> dt.datetime:
		return self.__creation

	def _setModified( self ) -> None:
		# Protected method to update self.__modified info.
		self.__modified = dt.datetime.fromtimestamp( time() )

	def getModified( self ) -> dt.datetime:
		return self.__modified
