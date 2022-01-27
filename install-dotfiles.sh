if [ ! "$(echo $0)" = "zsh" ]; then
  echo Current login shell is $(echo $0). Changing to zsh.
  sudo chsh -s $(which zsh) $(whoami)
fi

if [ -n "$SSH" ]; then
  git clone --bare git@github.com:jaywonchung/dotfiles $HOME/.dotfiles
else
  git clone --bare https://github.com/jaywonchung/dotfiles.git $HOME/.dotfiles
fi
git --git-dir=$HOME/.dotfiles --work-tree=$HOME checkout master
source .dotmodules/init.sh

dotfiles checkout ubuntu-server
zsh $HOME/.dotmodules/install/all.sh
