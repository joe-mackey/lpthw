formatter = " {} {} {} {} {} {}"

print (formatter.format (1, 2, 3, 4, 5, 6))
print (formatter.format ("one", "two", "three", "four", "five", "six"))
print (formatter.format (True, False, False, True, True, True))
print (formatter.format (formatter, formatter, formatter, formatter , formatter, formatter))
print (formatter.format (
    "Try your",
    "own text here",
    "Maybe a poem",
    "Or a song about fear",
    "I fear sending this file",
    "to github"
))
