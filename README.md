Open Settings; go to Update & Security > For Developers; enable Developer Mode
Search 'Turn Windows Features On or Off' and enable 'Windows Subsystem for Linux (Beta)'
Reboot
Open Command Prompt and run 'bash'
Pin the 'Bash on Ubuntu on Windows' program to the taskbar
Right Click > Defaults > Layout; Colors

Do 'sudo passwd -d root' and 'sudo passwd -d zacks'
Copy 'bin/' and '.bash_aliases' from '{/mnt/c/Users/zacks/Google\ Drive | /mnt/d/Google\ Drive}/Records/Linux\ Config\ Files/' to Linux's '~/'
Add the lines 'export PATH=~/bin:$PATH' and 'export DISPLAY=localhost:0.0' to '.bashrc'
Update the 'google_drive_path' variable at the top of '.bash_aliases'
Do 'sudo vi /etc/hosts' and add '127.0.1.1 [computer name].localdomain [computer name]' as the second line

https://gist.github.com/kevin-smets/8568070


defaults write com.apple.finder AppleShowAllFiles YES
Option + click Finder > Relaunch


Add to '.zshrc':
ZSH_THEME="powerlevel9k/powerlevel9k"

plugins=(git zsh-autosuggestions)

DEFAULT_USER=zackswafford
prompt_context(){}

POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(virtualenv context dir rbenv vcs)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status root_indicator background_jobs history command_execution_time)
POWERLEVEL9K_SHORTEN_DIR_LENGTH=1
POWERLEVEL9K_SHORTEN_DELIMITER=""
POWERLEVEL9K_SHORTEN_STRATEGY="truncate_from_right"
POWERLEVEL9K_COMMAND_EXECUTION_TIME_THRESHOLD=0

export PATH=~/bin:$PATH

if [ -f ~/.zsh_aliases ]; then
. ~/.zsh_aliases
fi