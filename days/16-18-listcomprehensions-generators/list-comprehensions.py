"""
Can you write a simple list comprehension to convert these names to title case (brad pitt -> Brad Pitt). Or reverse the first and last name?
Then use this same list and make a little generator, for example to randomly return a pair of names, try to make this work:

pairs = gen_pairs()
for _ in range(10):
    next(pairs)
Should print (values might change as random):

Arnold teams up with Brad
Alec teams up with Julian
Have fun!

"""

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

# convert to title case
convert_to_title_case = [actor.title() for actor in NAMES]
print(convert_to_title_case)

# reverse first and last names

reverse_first_and_lastnames = [' '.join([actor.split(' ')[1], actor.split(' ')[0]]) for actor in NAMES]
print(reverse_first_and_lastnames)

# Random team up
import random


def gen_pairs(some_list):
    name_one = 'start'
    name_two = 'start'
    while name_one == name_two:
        name_one = random.choice(some_list).split(' ')[0]
        name_two = random.choice(some_list).split(' ')[0]
        yield f'{name_one} teams up with {name_two}'


for _ in range(len(convert_to_title_case)):
    team = next(gen_pairs(convert_to_title_case))
    print(team)
