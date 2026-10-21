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

	dirpath = Path(FOLDERPATH,FOLDERNAME)
	dirpath.mkdir( parents=True, exist_ok=True)

	new_dir = Dossier.Dossier(
		absolute_path=FOLDERPATH,
		name=FOLDERNAME,
		creation=dt.datetime.fromtimestamp(
			Path( FOLDERPATH,FOLDERNAME ).stat().st_ctime
		),
		size=Path( FOLDERPATH,FOLDERNAME ).stat().st_size
	)
	print(
		f"FOLDER_NAME={new_dir.getName()}",
		f"FOLDER_PATH={new_dir.getPath()}",
		f"FOLDER_SIZE={new_dir.getSize()}",
		f"CREATED={new_dir.getCreation()}",
		sep='\n'
	)
	new_dir.renommer('delete-renamed')


def main():
	test_directory_rename()

if __name__ == '__main__':
	main()
