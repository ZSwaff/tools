# Personal Scripts and Environment Setup

## Windows
1. Open `Settings` > `Update & Security` > `For Developers` > `Enable Developer Mode`
1. Search `Turn Windows Features On or Off` and enable `Windows Subsystem for Linux (Beta)`
1. Reboot
1. Open Command Prompt and run `bash`
1. Pin the `Bash on Ubuntu on Windows` program to the taskbar
1. Optionally reset colors with `right click` > `Defaults` > `Layout` > `Colors`
1. Do 'sudo passwd -d root' and 'sudo passwd -d zacks'
1. Copy 'bin/' and '.bash_aliases' from '{/mnt/c/Users/zacks/Google\ Drive | /mnt/d/Google\ Drive}/Records/Linux\ Config\ Files/' to Linux's '~/'
1. Add the lines 'export PATH=~/bin:$PATH' and 'export DISPLAY=localhost:0.0' to '.bashrc'
1. Update the 'google_drive_path' variable at the top of '.bash_aliases'
1. Do 'sudo vi /etc/hosts' and add '127.0.1.1 [computer name].localdomain [computer name]' as the second line

## Mac
1. Run `defaults write com.apple.finder AppleShowAllFiles YES` to show hidden files
1. ⌥+click in Finder > `Relaunch`
1. Install iTerm2 and check out [styling](https://gist.github.com/kevin-smets/8568070)
---
Use the rest of the files in the repo as needed.
