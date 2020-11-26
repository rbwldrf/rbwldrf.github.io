import os
from markdown2 import markdown
import jinja2 as j
import shutil

print(os.getcwd())

env = j.Environment(loader=j.FileSystemLoader("templates"))

template = env.get_template("test.html")
recipe_template = env.get_template("recipe.html")

imgpath = "./recipes-ssg/img"

for bla in os.listdir(imgpath):
    shutil.copyfile(
        os.path.join(
            os.getcwd()+imgpath,bla),
        os.path.join("./img/",bla))

src = open("recipes-ssg/a.md","r")
base = open("recipes/home.html","w")

title = markdown("#"+"welcome to my recipe site!")

mdpath = "./recipes-ssg/mds"

f = list()

for md in os.listdir(mdpath):
    f.append(markdown(open(os.path.join(mdpath+"/"+md)).read()))

rd_rec = list()

recipes = list()
contentDictArray = [
    {"def":"center","ct":title},
        
    
]

for aa in f:
    recipes.append( recipe_template.render(content=aa) )

contentDictArray.append({"def":"gallery","ct":recipes})

base.write(template.render(
    content=contentDictArray,
    rec=recipes
    )
)

src.close()
base.close()