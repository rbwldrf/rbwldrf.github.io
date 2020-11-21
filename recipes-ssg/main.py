import os
from markdown2 import markdown
from jinja2 import Environment, PackageLoader

print(os.getcwd())

env = Environment(loader=PackageLoader("main", "templates"))

src = open("recipes-ssg/a.md","r")
base = open("recipes/home.html","w")

base = "what the fuck"