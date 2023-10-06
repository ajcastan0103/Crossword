def crossword(L):
    blank = ' '
    # 20x20 matrix for board
    board = [[blank] * 20 for i in range(20)]

    # function to create & print board for matrix.
    def printboard(board):
        # mapping for top of horizontal part of grid
        print(end=' ')
        for i in range(len(board)):
            if i >= 10:
                print(i - 10, end=' ')
            else:
                print(i, end=' ')
        print()
        print(end=' ')
        for i in range(len(board)):
            print('_', end=' ')
        print()
        for i in range(len(board)):
            print('|', end=' ')
            for j in range(len(board[i])):
                print(board[i][j], end=' ')
            print('|', i)
        print(end=' ')  # mapping for bottom of horizontal part of grid
        for i in range(len(board)):
            print('_', end=' ')
        print()
        print(end=' ')
        for i in range(len(board)):
            if i >= 10:
                print(i - 10, end=' ')
            else:
                print(i, end=' ')

    # function to print first word of list L, horizontally
    def addFirstWord(board, word):
        m = len(board)
        n = len(word)
        # Check if out of bounds
        if len(word) > len(board):
            return False
        else:
            # print first word horizontally in the middle of the board
            for i in range(n):
                column = m // 2 - n // 2 + i
                board[m // 2][column] = word[i]
            return True

    def checkVertical(board, word, row, col):  # function to check if word can be added vertically
        m = len(word)
        n = len(board)
        # if statement to check if out of bounds
        if m > n:
            return False
        '''for loop containing  if statements to check if word placement is legal
                 ( word1 shares a letter with word2 & all surrounding spaces are empty).
                 If so, function returns true, returns false otherwise.'''
        for i in range(m):
            if board[row][col] == word[i]:
                if (row and col) < n - 1:
                    if board[row + 1][col] == ' ' and board[row - 1][col] == ' ' and board[row + 1][col + 1] == ' ' \
                            and board[row + 1][col - 1] == ' ' and board[row - 1][col + 1] == ' ' and board[row - 1][
                        col - 1] == ' ':
                        return True
        return False

    '''Function checks if word placed makes a new word when placed vertically'''

    def checkVerticalAround(board, letter, row, col):
        if board[row][col] == letter:
            if board[row + 1][col + 1] == ' ' and board[row - 1][col + 1] == ' ' and board[row + 1][col - 1] == ' ' and \
                    board[row - 1][col - 1] == ' ':
                return True
        elif board[row][col + 1] == ' ' and board[row][col - 1] == ' ' and (
                board[row + 1][col] == ' ' or board[row - 1][col] == ' '):
            return True
        else:
            return False

    # function to add word to board vertically
    def addVertical(board, word):
        m = len(word)
        n = len(board)
        # if statement to check if out of bounds
        if m > n:
            return False
        # if not out of bounds, run for loop to add each character to board.
        # If in illegal word/letter is placed, remove all the letters.
        for i in range(n):
            for j in range(1, len(board[i])):
                for k in range(1, m):
                    if checkVertical(board, word[k], i, j):
                        above = i
                        under = i
                        error = None  # variable detecting if letter put on board makes it illegal
                        letters = []  # list for every letter put onto the board

                        if i - len(word[:k]) < 0 or i + len(word[k:]) >= n:
                            return False
                        # for loops for putting letters to board and adding them to the list.
                        for a in range(k - 1, -1, -1):
                            above = above - 1
                            if checkVerticalAround(board, word[a], above, j):
                                letters.append(above)
                                board[above][j] = word[a]
                            else:
                                error = True

                        for u in range(k + 1, len(word)):
                            under = under + 1
                            if checkVerticalAround(board, word[u], under, j):
                                letters.append(under)
                                board[under][j] = word[u]
                            else:
                                error = True

                        # if the variable error is true, remove all letters that were initially put onto board for the word.
                        if error:
                            for letter in letters:
                                board[letter][j] = ' '
                        else:
                            return True
        return False

    # function to check if word can be added horizontally
    def checkHorizontal(board, word, row, col):
        m = len(word)
        n = len(board)
        # if statement to check if out of bounds
        if m > n:
            return False
        '''for loop containing  if statements to check if word placement is legal
            (word1 shares a letter with word2 & all surrounding spaces are empty).
            If so, function returns true, returns false otherwise.'''
        for i in range(m):
            if board[row][col] == word[i]:
                if (row and col) < n - 1:
                    if board[row][col + 1] == ' ' and board[row][col - 1] == ' ' and board[row + 1][col + 1] == ' ' \
                            and board[row + 1][col - 1] == ' ' and board[row - 1][col + 1] == ' ' and board[row - 1][
                        col - 1] == ' ':
                        return True
        return False

    '''Function checks if word placed makes a new word when placed horizontally'''

    def checkHorizontalAround(board, letter, row, col):
        if board[row][col] == letter:
            if board[row + 1][col + 1] == ' ' and board[row + 1][col - 1] == ' ' and board[row - 1][col + 1] == ' ' and \
                    board[row - 1][col - 1] == ' ':
                return True

        elif board[row + 1][col] == ' ' and board[row - 1][col] == ' ' and (
                board[row][col + 1] == ' ' or board[row][col - 1] == ' '):
            return True
        else:
            return False

    # function to add word to board horizontally
    def addHorizontal(board, word):
        m = len(word)
        n = len(board)
        # if statement to check if out of bounds
        if m > n:
            return False
        # if not out of bounds, run for loop to add each character to board.
        # If in illegal word/letter is placed, remove all the letters.
        for i in range(n):
            for j in range(len(board[i])):
                for k in range(m):
                    if checkHorizontal(board, word[k], i, j):
                        left = j
                        right = j
                        error = None  # variable detecting if letter put on board makes it illegal
                        letters = []  # list for every letter put onto the board

                        if j - len(word[:k]) < 0 or j + len(word[k:]) >= len(board[i]):
                            return False

                        # for loops for putting letters to board and adding them to the list.
                        for l in range(k - 1, -1, -1):
                            left = left - 1
                            if checkHorizontalAround(board, word[l], i, left):
                                letters.append(left)
                                board[i][left] = word[l]
                            else:
                                error = True

                        for r in range(k + 1, m):
                            right = right + 1
                            if checkHorizontalAround(board, word[r], i, right):
                                letters.append(right)
                                board[i][right] = word[r]
                            else:
                                error = True
                        # if the variable error is true, remove all letters that were initially put onto board for the word.
                        if error:
                            for letter in letters:
                                board[i][letter] = ' '
                        else:
                            return True
        return False

    def addwords(board, L):
        '''for loop to check if each word in list not more than 20 characters. if so, remove
        that word for the list and print that it can't be implemented into the board.'''
        for j in range(len(L) - 1):
            if len(L[j]) > 20:
                print('The word, <', L[j], '> could not be added to the board as it is too long.')
                L.remove(L[j])

        addFirstWord(board, L[0])  # add first word in list to the middle of the board

        '''for loop to add words in modified list to the board. It adds words vertically first, horizontally otherwise.'''
        for i in range(1, len(L), 1):
            a = addVertical(board, L[i])
            if a == False:
                b = addHorizontal(board, L[i])
                if b == False:
                    print('The word, <', L[i], '> could not be added to the board due to illegal reasons.')
        printboard(board)

    addwords(board, L)
    print(end='\n')


L = []
string = str(input("Enter a string. To end, enter a non-letter: "))
while string.isalpha():
    L.append(string)
    string = str(input("Enter a string. To end, enter a non-letter: "))
if L != []:
    crossword(L)
else:
    print("List of strings is empty")
