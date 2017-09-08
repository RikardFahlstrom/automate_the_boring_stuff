import json
from country_codes import get_country_code
from pygal.maps.world import World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

# Load the data into a list.
filename = 'C:/Users/rikfah/PycharmProjects/Learning_Python/population_data.json'
with open(filename) as f:
    pop_data = json.load(f)  # json.load skapar en lista av .json-filen

# Listan består utav dictionaries.

# Build a dictionary of population data
cc_populations = {}  # Skapar en ny dict som ska innehålla landskod:population i det format som Pygal förväntar sig landskod som str och population som int.
for pop_dict in pop_data:  # Varje item i pop_data är en dictionary
    if pop_dict['Year'] == '2010':  # När man skriver pop_dict['Year'] så får man valuet tillhörande key:n pop_dict['Year']
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population  # Här skapas den nya key:n code, med population som value
        else:
            print('ERROR - ' + country_name)

# Group the countries into 3 population levels.
cc_pops_1, cc_pops_2, cc_pops_3 = {},{}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# See how many countries are in each level.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')
