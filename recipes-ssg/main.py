import os
from markdown2 import markdown
import jinja2 as j

print(os.getcwd())

env = j.Environment(loader=j.FileSystemLoader("templates"))
template = env.get_template("test.html")

src = open("recipes-ssg/a.md","r")
base = open("recipes/home.html","w")

recipeDictArray =[{"href":"a.com","desc":"hello"}]

base.write(template.render(
    bla=markdown("#welcome to my site \n _hello_"),
    recipes=recipeDictArray
    )
)

src.close()
base.close()