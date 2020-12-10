import os
from markdown2 import markdown
import jinja2 as j
import shutil

print(os.getcwd())

env = j.Environment(loader=j.FileSystemLoader("templates"))

template = env.get_template("test.html")
recipe_template = env.get_template("recipe.html")
table_template = env.get_template("table.html")

imgpath = "./recipes-ssg/img"

for bla in os.listdir(imgpath):
    shutil.copyfile(
        os.path.join(
            os.getcwd()+imgpath,bla),
        os.path.join("./img/",bla))

src = open("recipes-ssg/a.md","r")
base = open("myrecipes/index.html","w")

#title = markdown("#"+"welcome to my recipe site!")

mdpath = "./recipes-ssg/mds"

f = list()
f2 = list()


for md in os.listdir(os.path.join(mdpath+"/recipes")):
    f.append(markdown(open(os.path.join(mdpath+"/recipes/"+md)).read()))

for md in os.listdir(os.path.join(mdpath+"/foods")):
    f2.append(markdown(open(os.path.join(mdpath+"/foods/"+md)).read()).splitlines())

rd_rec = list()

recipes = list()
foodlist = list()

contentDictArray = [
    {"def":"center"},
        
    
]

for aa in f:
    recipes.append( recipe_template.render(content=aa) )

for aa in f2:
    foodlist.append( table_template.render(type=aa[0],size=aa[1],cost=aa[2]) )



base.write(template.render(
    content=contentDictArray,
    rec=recipes,
    foods=foodlist,
    about=markdown(open(os.path.join(mdpath+"/about.md")).read())
    )
)

src.close()
base.close()