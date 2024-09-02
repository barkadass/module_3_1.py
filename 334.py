calls = 0


def count_calls():
    global calls
    calls += 1
    print(calls)


def string_info(string):
    count_calls()
    return (len(string), string.upper(),string.lower())


def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [str.upper() for str in list_to_search]


print(string_info('Barkadas'))
print(string_info('Scaramucha'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls)



