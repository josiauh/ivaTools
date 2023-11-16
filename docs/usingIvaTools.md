# 2. Using ivaTools
When you get ivaTools, you can run it in your command line.
Use the commands:
```bash
# Linux
chmod +x ./ivaTools
./ivaTools
# macOS (darwin for you nerds)
ivaTools.app
```
```bat
REM Windows
ivaTools
```
When you first run it without telling it the tool you want to use, you'll get a help text. To use a tool, use the following commands:
```bash
# Linux
./ivaTools --tool trackProject
# macOS (darwin for you nerds)
ivaTools.app --tool trackProject
```
```bat
REM Windows
ivaTools --tool trackProject
```
If you launch a tool and you get looped into a terminal-like command prompt, you can type "help" to find the commands you can use. You can also look in the source code of the tool by looking in the "tools" directory.