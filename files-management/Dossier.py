from	Item		import	Item
import	datetime	as		dt
import	os
from	pathlib		import	Path

SIZE_MAX		= 3000
SIZE_MAX_UNIT	= 'KB'

class Dossier( Item ):
	def __init__(
		self,
		name:str,
		absolute_path:str,
		creation:dt.datetime,
		size_max:int=SIZE_MAX,
		size:int=0
	) -> None:
		super().__init__( 
			name,
			absolute_path,
			creation,
		)
		self.__size_max	= size_max
		self.__size		= size

	def getSize( self ) -> int:
		return self.__size

	def peutAjouter(
		self,
		file_size:int
	) -> bool:
		new_size = self.__size + file_size
		if new_size <= self.__size_max:
			return True
		return False

	def renommer(
		self,
		name:str
	) -> None:
		src	= Path( self.getPath(), self.getName() )
		dst	= Path( self.getPath(), name )
		src.rename( dst )
		self.setName( name )
