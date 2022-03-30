echo "Changing login shell to $(which zsh)"
sudo chsh -s $(which zsh) $(whoami)

if [ -n "$SSH" ]; then
  git clone --bare git@github.com:jaywonchung/dotfiles $HOME/.dotfiles
else
  git clone --bare https://github.com/jaywonchung/dotfiles.git $HOME/.dotfiles
fi
git --git-dir=$HOME/.dotfiles --work-tree=$HOME checkout master
source .dotmodules/init.sh

if [[ -f "/etc/redhat-release" ]]; then
  dotfiles checkout rhel-server
else
  dotfiles checkout ubuntu-server
fi
zsh $HOME/.dotmodules/install/all.sh
