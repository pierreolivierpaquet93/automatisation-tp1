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
		src	= os.path.join( self.getPath, self.__name )
		dst	= os.path.join( self.getPath, name )
		os.rename(src=src, dst=dst)
		self.setName( name )

	def resize( self ) -> int:
		path = os.path.join( self.getPath(), self.getName() )
		size = Path( path ).stat().st_size
		self.__size = size
