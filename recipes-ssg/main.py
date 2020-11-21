import os
from markdown2 import markdown
from jinja2 import Environment, PackageLoader

print(os.getcwd())

env = Environment(loader=PackageLoader("main","templates"))
template = env.get_template("test.html")


src = open("recipes-ssg/a.md","r")
base = open("recipes/home.html","w")

base.write(markdown("ughh"))

data = {
    'content': src,
    'title': src.metadata['title'],
    'date': src.metadata['date']
    }

src.close()
base.close()