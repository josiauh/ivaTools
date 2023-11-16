# ivaTools
import argparse
from vars import Vars
from tools.projectTracking import projTracking
from yachalk import chalk
#region Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument("--tool",  type=str, default="help", help="The tool to launch")
options = parser.parse_args()
#endregion
if (options.tool == "trackProject"):
    projTracking.track()
elif (options.tool == "help"):
    print(Vars.helpText)
else:
    print(chalk.red("Invalid option."))
    print(Vars.helpText)