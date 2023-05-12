# Even the loop is Infinite loops. U can use break to exits the loop
# when the continue is executed, it ends the current iteration and back to the while statement to start the next iteration

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
    
print('Done!')