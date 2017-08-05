grid_filename = '/Users/taranraghuram/Documents/Project Euler/10 - Grid of numbers.txt'
grid_file = open(grid_filename, 'r')
line = grid_file.readline()
while line != '':
    print(line)
    line = grid_file.readline()
