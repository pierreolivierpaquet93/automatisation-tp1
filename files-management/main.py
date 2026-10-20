import	datetime	as		dt
from	pathlib		import	Path
import	os
import	Item
import	Dossier

FILENAME='README.md'
FILEPATH='/home/user1/Documents/tp1/'

FOLDERNAME='delete'
FOLDERPATH='/tmp/'

def test_directory_rename():

	dirpath = os.path.join(FOLDERPATH,FOLDERNAME)
	if Path( dirpath ).exists():
		os.remove( dirpath )
	os.makedirs(name=dirpath,exist_ok=True)

	new_dir = Dossier.Dossier(
		absolute_path=FOLDERPATH,
		name=FOLDERNAME,
		creation=dt.datetime.fromtimestamp(
			Path( os.path.join( FOLDERPATH,FOLDERNAME )).stat().st_ctime
		),
		size=Path( os.path.join(FOLDERPATH,FOLDERNAME)).stat().st_size
	)
	print(
		f"FOLDER_NAME={new_dir._name}",
		f"FOLDER_PATH={new_dir._path}",
		f"FOLDER_SIZE={new_dir._size}",
		f"CREATED={new_dir._creation}",
		sep='\n'
	)
	new_dir.renommer('delete-renamed')


def main():
	test_directory_rename()

if __name__ == '__main__':
	main()
