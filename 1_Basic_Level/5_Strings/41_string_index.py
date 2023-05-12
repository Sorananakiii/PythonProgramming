# String index

string = 'We are the champion\nThe world will remember our'
print(string)
print('-'*30)
# Access to string index that start at index 0
# name[start : stop : step]
print('print string from index 0 to 4 or first 5 character')
print(string[:5])
print('-'*30)

print('print string from index n-4 to n or last 5 character')
print(string[-5:])
print('-'*30)

print('Number of characters of string')
print(len(string))
print('-'*30)

# add word or character to string 
new = string + '\nGG' # '\n' is newline syntax
print(new)
print('-'*30)

# example of string function
news = new.replace('We' , 'WE')
print(new)
print('-'*30)

print(news.find('GG')) # return index
print(new)
print('-'*30)