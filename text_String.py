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