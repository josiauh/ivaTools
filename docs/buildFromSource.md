# 1. Building from source
If you want to build from the source, maybe because you want to contribute to ivaTools, you can do so!
## Installing the requirements
To install the requirements, make sure you have [Python](https://www.python.org/downloads/) installed.

Then, install the requirements using the command:
```sh
pip install -r requirements.txt
```
When you have done that, you can now package up ivaTools!
## Packaging with PyInstaller
Now you can package with PyInstaller!

Run this command in the command line for linux/darwin (darwin is macOS):
```bash
python -m PyInstaller main.spec
```
But if you're on windows, you can run this command:
```bat
python -m PyInstaller win.spec
```
## Bundling for macOS
If you use darwin/macOS, you can create a .app file for macOS.

Move your ./build/main/ivaTools file into the "macOS" directory first.

When done, you can make it by doing this:
```bash
cd ./macOS
./bundleMac.sh
```
This does the following:
* Make the "./build/main/ivaTools" file actually executable because you gotta
* Creates all the directories for the ivaTools app
* Copy the icon.icns, Info.plist, and the file in 1st step mentioned into the app
