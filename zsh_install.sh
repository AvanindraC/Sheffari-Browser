echo "Installing Sheffari Browser..."
cd ~/Downloads
wget "https://github.com/XApple-Team/Sheffari-Browser/releases/download/0.1.4/sheffari"
wget https://cdn1.iconfinder.com/data/icons/hawcons/32/700146-icon-62-compass-512.png
echo "Adding Sheffari to PATH..."

mkdir -p ~/.mko

chmod u+x ./sheffari

cp ./sheffari ~/.mko/
mv ./700146-icon-62-compass-512.png ~/.mko/sheffari.png
echo "export PATH=$PATH:~/.mko" >> ~/.zshrc
cd ~/.local/share/applications
echo "
[Desktop Entry]
Name=Sheffari Web Browser
Exec=zsh -c 'sheffari' 
Comment=Sheffari Web Browser
Terminal=false
Icon=$HOME/.mko/sheffari.png
Type=Application" > Sheffari.desktop
echo "installation is completed!"
rm -rf ~/Downloads/sheffari
echo "Deleting unnecessary files"