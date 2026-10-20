from	Item		import	Item
import	datetime	as		dt

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
