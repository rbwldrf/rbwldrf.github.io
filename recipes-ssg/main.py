import os
from markdown2 import markdown
import jinja2 as j

print(os.getcwd())

env = j.Environment(loader=j.FileSystemLoader("templates"))
template = env.get_template("test.html")

src = open("recipes-ssg/a.md","r")
base = open("recipes/home.html","w")

title = markdown("#"+"welcome to my recipe site!")

recipeDictArray =[{"href":"a.com","desc":"hello"}]
contentDictArray = [{"def":"center","ct":title}]


base.write(template.render(
    content=contentDictArray,
    recipes=recipeDictArray
    )
)

src.close()
base.close()