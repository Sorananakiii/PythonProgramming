
# list comprehension

heights = [144, 180, 165, 120, 199]
tall = [h for h in heights]
print(tall)


tall = [h for h in heights if h > 160]
print(tall)