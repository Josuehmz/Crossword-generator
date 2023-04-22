import random

def generate_crossword(words, length, height):
    # Create the empty grid
    grid = [[' ' for _ in range(length)] for _ in range(height)]

    # Try to place each word in the grid
    for word in words:
        placed = False
        while not placed:
            # Choose a random starting position and direction
            start_x = random.randint(0, length-1)
            start_y = random.randint(0, height-1)
            direction_x, direction_y = random.choice([(1,0), (0,1)])

            # Check if the word fits in the chosen starting position and direction
            if direction_x == 1 and length - start_x >= len(word) or \
                direction_y == 1 and height - start_y >= len(word):
                fits = True
                for i in range(len(word)):
                    x = start_x + i * direction_x
                    y = start_y + i * direction_y
                    if grid[y][x] != ' ' and grid[y][x] != word[i]:
                        fits = False
                        break

                # If the word fits, place it in the grid
                if fits:
                    for i in range(len(word)):
                        x = start_x + i * direction_x
                        y = start_y + i * direction_y
                        grid[y][x] = word[i]
                    placed = True

    # Fill the remaining spaces with random letters
    for y in range(height):
        for x in range(length):
            if grid[y][x] == ' ':
                grid[y][x] = chr(random.randint(65, 90))

    # Convert the grid to a string
    crossword = ''
    for row in grid:
        crossword += ' '.join(row) + '\n'

    return crossword


if __name__ == '__main__':
    while True:
        # Ask for the number of words, their length and the dimensions of the grid
        num_words = int(input('How many words do you want to include? '))
        word_length = int(input('What should be the maximum length of the words? '))
        grid_length = int(input('What should be the length of the grid? '))
        grid_height = int(input('What should be the height of the grid? '))

        # Generate the words
        words = []
        for i in range(num_words):
            word = input('Enter word #{}: '.format(i+1))
            while len(word) > word_length:
                print('The word should be at most {} letters long'.format(word_length))
                word = input('Enter word #{}: '.format(i+1))
            words.append(word.upper())

        # Generate the crossword and print it
        crossword = generate_crossword(words, grid_length, grid_height)
        print(crossword)

        # Ask the user if they want to generate another crossword
        answer = input('Do you want to generate another crossword? (yes or no) ')
        if answer.lower() != 'yes':
            break
