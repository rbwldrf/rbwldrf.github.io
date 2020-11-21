import os
from markdown2 import markdown
import jinja2 as j

print(os.getcwd())

env = j.Environment(loader=j.FileSystemLoader("templates"))
template = env.get_template("test.html")


src = open("recipes-ssg/a.md","r")
base = open("recipes/home.html","w")

base.write(markdown("er ennþá að reyna að læra á þetta"))

src.close()
base.close()