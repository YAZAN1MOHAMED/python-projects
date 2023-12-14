#Some test cases to check that the regex works well
#using the comma (,) as a fill for the empty spaces
#Using capturing groups to know every position so that I can change the background of the winning cells correctly




diagonalPattern1X = r"^..(x).(x).(x)"#stars with any two characters (^..) then must find (x) followed by any character (.) three times in a row
CheckDiagonalPattern1X1=['X', 'O', ',', ',', 'X', 'O', ',', ',', 'X']

diagonalPattern2X = r"(x)...(x)...(x)"
CheckDiagonalPattern2X=[',', 'O', 'X', 'O', 'X', ',', 'X', ',', ',']

columnPatternsX=r"(x)..(x)..(x)"
CheckColumnPatternsX=['X', 'O', ',', 'X', 'O', ',', 'X', ',', ',']
CheckColumnPatternsX2=[',', 'X', 'O', ',', 'X', 'O', ',', 'X', ',']
CheckColumnPatternsX3=[',', ',', 'X', ',', 'O', 'X', ',', 'O', 'X']

rowPatternsX=r"(^XXX)|((?<=^.{3})XXX)|(XXX$)"#I can't just check for a three X's in a sequence because of the last test
CheckRowPatternsX1=['X', 'X', 'X', ',', 'O', 'O', ',', ',', ',']
CheckRowPatternsX2=[',', 'O', 'O', 'X', 'X', 'X', ',', ',', ',']
CheckRowPatternsX3=[',', ',', ',', ',', 'X', 'X', 'O', 'O', 'O']
CheckRowPatternsX4=[',', 'X', 'X', 'X', 'O', ',', ',', 'O', ',']#Must fail
'''
the bellow is a visualization for a xo board for the (CheckRowPatternsX4)
, x x
x o ,
o , ,

'''
