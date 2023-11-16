import yaml
from yaml import Loader
from yachalk import chalk
from vars import Vars
import os
defaultDoc = """
projectName: myProject
done:
  - screw it all up
inProgress:
  - go to france
todo:
  - beanie baby frog
"""
try:
    with open(os.environ.get("TMP") + "\\ivaTools\\project.yml", "r") as f:
        doc = f.read()
except FileNotFoundError:
    open(os.environ.get("TMP") + "\\ivaTools\\project.yml", "x")
    with open(os.environ.get("TMP") + "\\ivaTools\\project.yml", "w") as f:
        f.write(defaultDoc)
        doc = defaultDoc
except:
    print(chalk.red("Error while reading " + os.environ.get("TMP") + "\\ivaTools\\project.yml, maybe does not exist?"))
    doc = defaultDoc



def printTasks(ls: dict):
    for i in ls:
        print(i)
class projTracking:
    

    def track():
        
        projectTasks = yaml.load(doc, Loader=Loader)
        print("ivaTools Project:")
        print(projectTasks["projectName"])
        print("---------")
        while True:
            print(chalk.green("Done"))
            print("---------")
            printTasks(projectTasks["done"])
            print("---------")
            print(chalk.yellow("In Progress"))
            print("---------")
            printTasks(projectTasks["inProgress"])
            print("---------")
            print(chalk.red("To Do"))
            print("---------")
            printTasks(projectTasks["todo"])
            william = input("projectManagement> ")
            if (william.startswith("todo")):
                taskName = input("todo Name>")
                projectTasks["todo"].insert(len(projectTasks["todo"]),taskName)
            if (william.startswith("inProg")):
                taskName = input("inProg Name>")
                projectTasks["inProgress"].insert(len(projectTasks["inProgress"]),taskName)
            if (william.startswith("done")):
                taskName = input("done Name>")
                projectTasks["done"].insert(len(projectTasks["done"]),taskName)
            if (william.startswith("removeInProg")):
                taskName = input("which Name>")
                del(projectTasks["inProgress"][projectTasks["inProgress"].index(taskName)])
            if (william.startswith("removeToDo")):
                taskName = input("which Name>")
                del(projectTasks["todo"][projectTasks["todo"].index(taskName)])
            if (william.startswith("removeDone")):
                taskName = input("which Name>")
                del(projectTasks["done"][projectTasks["done"].index(taskName)])
            if (william.startswith("renameProject")):
                taskName = input("project Name>")
                print("Renamed " + projectTasks["projectName"] + " to " + taskName)
                projectTasks["projectName"] = taskName
            if (william.startswith("help")):
                print(Vars.projTrackHelp)
            with open(os.environ.get("TMP") + "\\ivaTools\\project.yml", "w") as f:
                yaml.dump(projectTasks, f, allow_unicode=True)