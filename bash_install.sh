echo "Installing Sheffari Browser..."
cd ~/Downloads
git clone "https://github.com/arghyagod-coder/Sheffari"
cd Sheffari
echo "Adding Sheffari to PATH..."

mkdir -p ~/.mko

chmod u+x ./dist/sheffari

cp -r ./dist/* ~/.mko/

echo "export PATH=$PATH:~/.mko" >> ~/.bashrc
cd ~/.local/share/applications
echo "
[Desktop Entry]
Name=Sheffari Web Browser
Exec=bash -c 'sheffari' 
Comment=Sheffari Web Browser
Terminal=false
Icon=$HOME/.mko/icon.png
Type=Application" > Sheffari.desktop
echo "installation is completed!"
rm -rf ~/Downloads/Sheffari
echo "Deleting unnecessary files"