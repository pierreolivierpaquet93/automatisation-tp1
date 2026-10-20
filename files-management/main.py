import datetime as dt
from pathlib import Path
import Item

FILENAME='README.md'
FILEPATH='/home/user1/Documents/tp1/'

def main():
	new_item = Item.Item(
		name=FILENAME,
		absolute_path=FILEPATH,
		creation=dt.datetime.fromtimestamp(
			Path( f"{FILEPATH}{FILENAME}" ).stat().st_ctime
		)
	)
	print( new_item._creation )
	print( new_item._name )
	print( new_item._path )

if __name__ == '__main__':
	main()
