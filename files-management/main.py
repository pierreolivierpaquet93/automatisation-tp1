import	datetime	as		dt
from	pathlib		import	Path
import	os
import	Item
import	Dossier

# Absolute path to 'TP1'
#DIRECTORY='/home/user1/Documents/tp1/TP1/TP1'
DIRECTORY = '../TP1v2'

def getItems() -> list[Item.Item]:
	dir:str = ''
	if not DIRECTORY:
		dir = '../TP1/TP1'
	else:
		dir = DIRECTORY
	ListeItem:list[Item.Item] = []

	test = Path( dir )
	walk = test.walk()
	for r,d,f in walk:
		print( f"-----IMPORTING DIR AND FILES FROM [{r}]-----" )
		for directory in d:
			print( f"\tadding {directory} directory." )
		for file in f:
			print( f"\tadding {file} file." )

	return ListeItem

def main():
	ListeItem = getItems()

if __name__ == '__main__':
	main()
