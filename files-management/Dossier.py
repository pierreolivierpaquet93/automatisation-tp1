from	Item		import	Item
import	datetime	as		dt
import	os

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
		self._size_max	= size_max
		self._size		= size

	def peutAjouter(
		self,
		file_size:int
	) -> bool:
		new_size = self._size + file_size
		if new_size <= self._size_max:
			return True
		return False

	def renommer(
		self,
		name:str
	) -> None:
		src	= os.path.join( self._path, self._name )
		dst	= os.path.join( self._path, name )
		os.rename(src=src, dst=dst)
		self._name = name

