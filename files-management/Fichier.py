from	Item		import	Item
from	Dossier		import	Dossier
import	datetime	as		dt
from	pathlib		import	Path
import	time
class Fichier( Item ):
	def __init__(
		self,
		name:str,
		path:str,
		creation:dt.datetime,
		size:int,
		parent_directory:Dossier
	) -> None:
		super().__init__(
			name		= name,
			path		= path,
			creation	= creation
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
		else:
			size = int(self.getSize()/1024)
			storage_left = int(dst.getSize()/1024)
			size_max = int(dst.getSizeMax()/1024)
			print( f"Warning: can't move '{self.getName()}' to '{dst.getName()}'" )
			print( "----------------------------------------------" )
			print( f"MAX_SIZE\t= {size_max}" )
			print( f"FILE_SIZE\t= {size}" )
			print( f"AVAILABLE\t= {storage_left}" )
 
	def Copier( self ) -> None:
		suffix		= Path( self.getAbsolutePath() ).suffix
		stem		= Path( self.getName() ).stem
		timestamp	= dt.datetime.now().strftime( "%Y-%m-%d_%H:%M:%S" )
		new_name	= f"{stem}_{timestamp}{suffix}"

		if self.__parent_directory.peutAjouter( self.__size ):
			file = Path( self.getAbsolutePath() )
			copy = Path( self.getPath(), new_name )
			file.copy( target=copy )
			self.__parent_directory.adjustSize( self.__size )

	def getParentDirectory( self ) -> Dossier:
		return self.__parent_directory

	def getSize( self ) -> int:
		return self.__size
