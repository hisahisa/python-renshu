import re


def remove_punctuation(value):
    return re.sub('[!#?]', '', value)


def mod_one_space(value):
    return re.sub('\s+', ' ', value).strip()


states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south carolina##', 'West virginia?']
clean_ops = [str.strip, remove_punctuation, str.title, mod_one_space]


def clean_strings(strings, ops):
    result = []
    for value in strings:
        for func in ops:
            value = func(value)
        result.append(value)
    # return result
    yield result


gen = clean_strings(states, clean_ops)
print("gen")
print(gen)
for x in gen:
    print(x)
