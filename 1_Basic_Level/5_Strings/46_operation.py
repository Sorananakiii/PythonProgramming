# string operations
movie = '$I supposed that coming from MTV Films I should expect no less$'

# Convert to lowercase and print the result
movie_lower = movie.lower()
print(movie_lower)

# Convert to lowercase and print the result
movie_upper = movie.upper()
print(movie_upper)

# Remove whitespaces and print the result
movie_no_space = movie_lower.strip("$")
print(movie_no_space)

# Split the string into substrings and print the result
movie_split = movie_no_space.split()
print(movie_split)