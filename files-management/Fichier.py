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
		if dst.peutAjouter( file_size=self.__size ):
			file = Path( self.getAbsolutePath() )
			target = Path(dst.getAbsolutePath(),self.getName())
			file.move( target=target )

			self.__parent_directory.adjustSize( size=self.__size, add=False )
			self.__parent_directory = dst
			self.__parent_directory.adjustSize( size=self.__size )
			self.setPath( dst.getAbsolutePath() )

	def Copier( self ) -> None:
		ext = '.txt'
		timestamp = dt.datetime.now().strftime( "%Y-%m-%d_%H:%M:%S" )
		new_name = f"{self.getName()}_{timestamp}{ext}"

		if self.__parent_directory.peutAjouter( self.__size ):
			file = Path( self.getPath() )
			copy = Path( self.__parent_directory.getPath(), new_name )
			file.copy( target=copy )
			self.__parent_directory.adjustSize( self.__size )

	def getParentDirectory( self ) -> Dossier:
		return self.__parent_directory

	def getSize( self ) -> int:
		return self.__size
