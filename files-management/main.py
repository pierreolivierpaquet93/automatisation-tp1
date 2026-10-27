import	datetime	as		dt
from	pathlib		import	Path
from	Item		import	Item
from	Dossier		import	Dossier
from	Fichier		import	Fichier
from	time		import	sleep
import	argparse	as		ap

# Path to 'TP1'
DIRECTORY = ''

#-----------------------------------------------------------------[ FUNCTION.S ]

def getItems(
	args_path:str=''
) -> list[Item]|None:
	dir:Path = None
	if args_path:
		# Provided '--path' arg to 'main.py' program.
		dir = Path( args_path )
	elif not DIRECTORY:
		# '__file__' is the script's absolute path
		# If using Path('TP1/').absolute() uses the working directory.
		script_root = Path( __file__ ).parent
		# Relative path from the script.
		dir = Path( script_root, '../TP1/TP1' )
	else:
		dir = Path( DIRECTORY )

	if not dir.exists():
		raise ValueError( f"invalid directory: '{dir.absolute()}'." )

	# Declaration of en empty 'Item' list.
	ListeItem:list[Item] = []

	walk = dir.walk()

	# Requested 'for' loop.
	# Iterates throught every directory and files
	# Instanticates the corresponding object type: Fichier|Dossier
	for root,dirs,files in walk:
		root_path = Path( root )
		r = Dossier(
			absolute_path	= root_path.parent,
			creation		= dt.datetime.fromtimestamp(
				root_path.stat().st_ctime
			),
			name			= root_path.name
		)
		ListeItem.append( r )

		for file in files:
			file_path = Path( root, file )
			f = Fichier(
				name				= file_path.name,
				absolute_path		= file_path.parent,
				creation			= dt.datetime.fromtimestamp(
					file_path.stat().st_ctime
				),
				parent_directory	= r,
				size				= file_path.stat().st_size
			)
			f.getParentDirectory().adjustSize( size=file_path.stat().st_size )
			ListeItem.append( f )
	return ListeItem

def findItem(
	items:list[Item],
	name:str,
	instance_type:type
) -> Item|None:
	for it in items:
		if isinstance( it, instance_type ) and it.getName() == name:
			return it
	return None

def findItemsByExtension(
	items:list[Item],
	extension:str,
	instance_type:type=Item
) -> list[Item]|None:
	found:list[Item] = []
	for it in items:
		path = Path( it.getPath(), it.getName() )
		if path.suffix == extension and isinstance( it, instance_type ):
			found.append( it )
	return found

def deplacerMusique(
	items:list[Item]
) -> None:
	directory:Dossier = findItem(
		items			= items,
		name			= "Image",
		instance_type	= Dossier
	)
	directory.renommer( "Musique" )

	found:list[Fichier] = findItemsByExtension(
		items			= items,
		extension		= ".mp3",
		instance_type	= Fichier
	)
	dst = findItem(
		items			= items,
		name			= "Musique",
		instance_type	= Dossier
	)
	for it in found:
		it.DeplacerDansDossier( dst=dst )

def deplacerVideo(
	items:list[Item]
) -> None:
	dst:Dossier = findItem(
		items			= items,
		name			= 'Musique',
		instance_type	= Dossier
	)
	vid:Fichier = findItem(
		items			= items,
		name			= 'Vidéo3.mp4',
		instance_type	= Fichier
	)
	vid.DeplacerDansDossier( dst=dst )

def nCopy(
	src_name:str,
	items:list[Item],
	n:int		= 1,
	seconds:int	= 0
) -> None:
	src:Fichier = findItem(
		name			= src_name,
		items			= items,
		instance_type	= Fichier
	)
	for i in range(n):
		src.Copier()
		sleep( seconds )

#-----------------------------------------------------------------------[ MAIN ]

def main():
	parser = ap.ArgumentParser(
		description="TP1 script: manage files and "
					"directories throught a list of items."
	)
	parser.add_argument(
		'--path','-p',
		type=str,
		help="Path to the desired root directory."
	)
	args = parser.parse_args()

	try:
		ListeItem = getItems( args.path )
		'''
		deplacerMusique( items=ListeItem )
		deplacerVideo( items=ListeItem )
		nCopy(
			src_name	= 'Test3.txt',
			items		= ListeItem,
			n			= 10,
			seconds		= 1
		)
		'''
	except Exception as e:
		print( f"error: {e}" )
	
if __name__ == '__main__':
	main()
