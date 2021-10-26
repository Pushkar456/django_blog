from django import template 

register = template.Library() 

@register.filter(name='dictkey') 
def dictkey(dict1,key):
    return dict1.get(key)

