import	datetime	as		dt
from	pathlib		import	Path
import	Item
import	Dossier

FILENAME='README.md'
FILEPATH='/home/user1/Documents/tp1/'

FOLDERNAME='tp1'
FOLDERPATH='/home/user1/Documents/'

def main():
	new_item = Item.Item(
		name=FILENAME,
		absolute_path=FILEPATH,
		creation=dt.datetime.fromtimestamp(
			Path( f"{FILEPATH}{FILENAME}" ).stat().st_ctime
		)
	)
	print( f"ITEM_CREATED={new_item._creation}" )
	print( f"ITEM_NAME={new_item._name}" )
	print( f"ITEM_PATH={new_item._path}" )

	new_folder = Dossier.Dossier(
		name=FOLDERNAME,
		absolute_path=FOLDERPATH,
		creation=dt.datetime.fromtimestamp(
			Path( f"{FOLDERPATH}{FOLDERNAME}" ).stat().st_ctime
		)
	)
	print( f"FOLDER_CREATED={new_folder._creation}" )
	print( f"FOLDER_NAME={new_folder._name}" )
	print( f"FOLDER_PATH={new_folder._path}" )

if __name__ == '__main__':
	main()
