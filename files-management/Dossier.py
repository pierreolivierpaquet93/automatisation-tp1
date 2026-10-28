from	Item		import	Item
import	datetime	as		dt
from	pathlib		import	Path

SIZE_MAX	= 3000

class Dossier( Item ):
	def __init__(
		self,
		name:str,
		path:str,
		creation:dt.datetime,
		size_max:int=SIZE_MAX, # TP1: 'tailleMaximale'
		size:int=0 # TP1: 'taille'
	) -> None:
		super().__init__( 
			name,
			path,
			creation,
		)
		self.__size_max	= size_max*1024 # KiloBytes*1024=bytes
		self.__size		= size

	def getSize( self ) -> int:
		return self.__size

	def getSizeMax( self ) -> int:
		return self.__size_max

	def adjustSize(
		self,
		add:bool=True,
		size=0
	) -> int:
		if add:
			self.__size += size
		else:
			self.__size -= size
		self._setModified()
		return self.__size

	# TP1: Checks if the file size added to the current directory size
	# 	fits within the established limit (self.__size_max).
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
		src.rename( dst ) # TP1: Modifies the name of the directory on disk.
		self.setName( name ) # TP1: Modifies the Item 'name' attribute.
