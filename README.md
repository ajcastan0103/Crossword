# Crossword
 Python program that generates a crossword puzzle on a 20x20 matrix </br >
 
<b>Functions:</b> </br >

● class crossword(L): takes a list of words L. </br >

● printboard(board): prints the crossword board with row and column labels. </br >

● addwords(board, L) function iterates through the list of words, checking if each word exceeds the boundaries (i.e it's too long (more than 20 characters) or overlaps with other words on the board). Helper functions are called to check these boundaries:
 
    ○ checkVertical(board, word, row, col): This function checks if a word can be added vertically.</br >
   
    ○ checkVerticalAround(board, letter, row, col): This function checks if placing a letter vertically creates a new word. It checks if the surrounding spaces are empty.</br >
   
    ○ addVertical(board, word): This function attempts to add a word to the board in a vertical orientation.</br >
   
    ○ checkHorizontal(board, word, row, col): Similar to checkVertical, this function checks if a word can be added horizontally. </br >
   
    ○ checkHorizontalAround(board, letter, row, col): This function checks if placing a letter horizontally creates a new word.</br >
   
    ○ addHorizontal(board, word): This function attempts to add a word to the board in a horizontal orientation.
