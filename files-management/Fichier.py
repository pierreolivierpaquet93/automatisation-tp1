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
		self.__size:int					= size
		self.__parent_directory:Dossier	= parent_directory
		self.__extension:str			= Path( name ).suffix # TP1: Keeping the suffix.
		self.__backup_path:str			= self.getAbsolutePath() # TP1: latest backup full path.

	def getBackupPath( self ) -> str:
		return self.__backup_path

	def DeplacerDansDossier(
		self,
		dst:Dossier
	) -> None:
		ref_directory = self.__parent_directory
		if dst.peutAjouter( file_size=self.__size ): # TP1: Uses the method to verify if the file can be moved.
			file = Path( self.getAbsolutePath() )
			target = Path(dst.getAbsolutePath(),self.getName())
			file.move( target=target )

			self.__parent_directory.adjustSize( size=self.__size, add=False ) # TP1: Deducts the  size to the OLD parent directory.
			self.__parent_directory = dst # TP1: Modifies the current file's parent directory.
			self.__parent_directory.adjustSize( size=self.__size ) # Adds the size to the NEW parent directory.
			self.setPath( dst.getAbsolutePath() ) # TP1: Stores the parent full path into the file's path.
		else: # TP1: If not possible, error message displayed on STDOUT.
			size = int(self.getSize()/1024)
			storage_left = int(dst.getSize()/1024)
			size_max = int(dst.getSizeMax()/1024)
			print( f"Warning: can't move '{self.getName()}' to '{dst.getName()}'" )
			print( "----------------------------------------------" )
			print( f"MAX_SIZE\t= {size_max}" )
			print( f"FILE_SIZE\t= {size}" )
			print( f"AVAILABLE\t= {storage_left}" )
 
	def Copier( self ) -> None:
		suffix		= Path( self.getAbsolutePath() ).suffix # [example]-->[.txt]<--
		stem		= Path( self.getName() ).stem # -->[example]<--[.txt]
		timestamp	= dt.datetime.now().strftime( "%Y-%m-%d_%H:%M:%S" ) # Builds the timestamp component to append to the stem.
		new_name	= f"{stem}_{timestamp}{suffix}"

		if self.__parent_directory.peutAjouter( self.__size ): # TP1: Uses the method to verify if the file can be cppied.
			file = Path( self.getAbsolutePath() )
			copy = Path( self.getPath(), new_name )
			file.copy( target=copy ) # TP1: Makes a copy of the current file.
			self.__parent_directory.adjustSize( self.__size )
			self.__backup_path = str( copy )
		else:
			print( f"Warning: can't copy '{self.getName()}'." ) # TP1: If not possible, error message displayed on STDOUT.

	def getParentDirectory( self ) -> Dossier:
		return self.__parent_directory

	def getSize( self ) -> int:
		return self.__size
