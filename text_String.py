#Ejercicio 1

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest"""
texts_array = text.split('.')

keywords = ['average','temperature', 'distance']

for text in texts_array:
    for keyword in keywords:
        if keyword in text:
            print(text.replace(' C', ' celsius'))
            break

#Ejercicio 2
# Datos con los que vas a trabajar
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

title = f"About the {name}".title();

data = """The distance between the {0} and the {1} is {2} mts""".format(name,planet, gravity*1000)

template = f"""{title} 
{data}
"""
print(template)

# Nuevos datos muestra
planet = 'Marte '
gravity  = 0.00143
name = 'Ganímedes'

title = f"About the {name}".title();

data = """The distance between the {0} and the {1} is {2} mts""".format(name,planet, gravity*1000)

template = f"""{title} 
{data}
"""
print(template)