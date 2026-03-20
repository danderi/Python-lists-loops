all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

# Your code here
def filter_colors(colors):
    list=[]
    for color in colors:
        if color["sexy"]==True:
            list.append(color)
    return list

def generate_li(items):
    list=[]
    for item in items:
        list.append('<li>'+item["label"]+'</li>')
    return list
        

print(generate_li(filter_colors(all_colors)))  