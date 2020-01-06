
cols = "ABCDEFGHI"
row = "123456789"
digits = row

build1D = lambda A,B: [ a+b  for b in B for a in A] # O(A * B)
build2D = lambda A,B: [[ a+b  for b in B ] for a in A] # O(A * B)
pop = lambda lst: list(lst).pop()

sudokuBoard = build2D(row, cols)

all_cells = build1D(row,cols) 

squares = [ build1D(r,c) for r in  ('123','456','789') 
                   for c in ('ABC', 'DEF', 'GHI')]

dataStructure = { cell : ( set(build1D(cell[0],cols)) - set([cell]), 
                  set( build1D(row,cell[1])) - set([cell]), 
                  set( pop(filter(lambda square: cell in square, squares)))) 
                  for cell in all_cells }

def parseGrid(grid):
   board = [ char for char in grid if char in digits + "0." ]
   assert len(board) == 81, "Error grid Number Len"

   mapping = lambda i: i if i in digits else '0'

   return { key: mapping(board[index]) 
            for index,key in enumerate(all_cells) }

def filter_cells(cell):
   return dataStructure[cell][0].union(dataStructure[cell][1])
   
def setGridAdjacency(grid):
   select = list(filter( lambda key: grid[key] == '0', grid))
   scouts = [ [ grid[key] for key in filter_cells(cell) ] for cell in select ] 
   values = [ "".join(set(digits) - set(scout)) for scout in scouts ]
   indexs = zip(select, values)

   for key, value  in indexs:
      grid[key] = value

   return grid

def test_case():
   assert len(squares) == 9
   assert len(dataStrcutre) == 81
   


def displaySudokuGrid(board):
   line1 ='{0} {1} {2} | {3} {4} {5} | {6} {7} {8}'
   
   for i in board:
      print(i)

grid = "4.....8.5.3..........7..........................................................."

grid2 = """
.........
.........
.........
.........
.........
.........
.........
.........
........."""

grid3 = """
4 . . | . . . | 8 . 5
. 3 . | . . . | . . .
. . . | 7 . . | . . .
------+-------+------
. 2 . | . . . | . 6 .
. . . | . 8 . | 4 . .
. . . | . 1 . | . . .
------+-------+------
. . . | 6 . 3 | . 7 .
5 . . | 2 . . | . . .
1 . 4 | . . . | . . .
"""

if __name__ == '__main__':
   
   g1 = parseGrid(grid3)
   g1 = setGridAdjacency(g1)
   print(g1)
   #displaySudokuGrid(sudokuBoard)
