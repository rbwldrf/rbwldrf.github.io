from markdown2 import markdown
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader(),autoescape=select_autoescape(['html','xml']))

src = open("recipes-ssg/a.md","r")
base = open("recipes/home.html","w")

base = 

markdown("")