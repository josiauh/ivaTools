chmod +x ./ivaTools
mkdir -p ivaTools.app/Contents/MacOS
mkdir -p ivaTools.app/Contents/Resources
cp Info.plist ivaTools.app/Contents/Info.plist
mv ivaTools ivaTools.app/Contents/MacOS/ivaTools
cp icon.icns ivaTools.app/Contents/Resources/icon.icns
echo Bundled!