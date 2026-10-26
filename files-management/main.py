import	datetime	as		dt
from	pathlib		import	Path
import	Item
import	Dossier
import	Fichier

# Absolute path to 'TP1'
DIRECTORY = ''
#DIRECTORY='/home/user1/Documents/tp1/TP1/TP1'

def getItems() -> list[Item.Item]:
	dir:Path = None
	if not DIRECTORY:
		script_root = Path( __file__ ).parent
		dir = Path( script_root, '../TP1v2' )
	else:
		dir = Path( DIRECTORY )

	ListeItem:list[Item.Item] = []
	
	walk = dir.walk()
	for root,dirs,files in walk:
		root_path = Path( root )
		r = Dossier.Dossier(
			absolute_path	= root_path.absolute(),
			creation		= dt.datetime.fromtimestamp(
				root_path.stat().st_ctime
			),
			name			= root_path.name
		)
		ListeItem.append( r )

		for file in files:
			file_path = Path( root, file )
			f = Fichier.Fichier(
				name				= file_path.name,
				absolute_path		= file_path.absolute(),
				creation			= dt.datetime.fromtimestamp(
					file_path.stat().st_ctime
				),
				parent_directory	= r,
				size				= file_path.stat().st_size
			)
			ListeItem.append( f )
 
	return ListeItem

def main():
	ListeItem = getItems()
	for it in ListeItem:
		if isinstance( it, Dossier.Dossier ):
			print( f"DOSSIER --> {it.getName()}" )
		elif isinstance( it, Fichier.Fichier ):
			print( f"FICHIER --> {it.getName()}" )

if __name__ == '__main__':
	main()
