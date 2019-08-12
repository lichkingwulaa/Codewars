def get_planet_name(id):
	id_name = { '1': "Mercury", '2': "Venus",   '3': "Earth",   '4': "Mars",
				'5': "Jupiter", '6': "Saturn",  '7': "Uranus",  '8': "Neptune", }
	return id_name[str(id)]



# 大佬鼠
def get_planet_name1(id):
	return {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }.get(id, None)


def get_planet_name2(id):
	return ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"][id-1]


get_planet_name3 = lambda id:["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"][id-1]