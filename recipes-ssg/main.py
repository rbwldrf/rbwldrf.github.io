import os
from markdown2 import markdown
import jinja2 as j
import shutil

print(os.getcwd())

env = j.Environment(loader=j.FileSystemLoader("templates"))
template = env.get_template("test.html")

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



recipes = [{"href":"a.com","desc":"hello"}]
contentDictArray = [
    {"def":"center","ct":title},
    {"def":"bla","ct":''.join(map(str, f))},
    {"def":"gallery","ct":recipes}
    ]


base.write(template.render(
    content=contentDictArray
    )
)

src.close()
base.close()