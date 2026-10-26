from	Item		import	Item
from	Dossier		import	Dossier
import	datetime	as		dt
from	pathlib		import	Path

class Fichier( Item ):
	def __init__(
		self,
		name:str,
		absolute_path:str,
		creation:dt.datetime,
		size:int,
		parent_directory:Dossier
	) -> None:
		super().__init__(
			name			= name,
			absolute_path	= absolute_path,
			creation		= creation
		)
		self.__size				= size
		self.__parent_directory	= parent_directory

	def DeplacerDansDossier(
		self,
		dst:Dossier
	) -> None:
		ref_directory = self.__parent_directory
		self.__parent_directory.adjustSize( size=self.__size, add=False )
		if dst.peutAjouter( file_size=self.__size ):
			self.__parent_directory = dst
			self.__parent_directory.adjustSize( size=self.__size )
			self.setPath( dst.getPath() )
			file = Path( self.getPath() )
			file.move( target=dst.getPath() )

	def Copier( self ):
		pass
