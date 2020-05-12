# Tools: Aliases, Scripts, and Environment
This is a set of tools that should help do a variety of common operations quickly. It should be relatively platform agnostic.

This set of shortcuts, aliases, and scripts unapologetically shortens, overloads, and replaces existing terminal commands and tools. 
It tries to do so in a way that is not particularly confusing. 
However, to temporarily ignore any of these commands, use `\[cmd]` (e.g. `\ls` will use system default `ls` rather than the overloaded aliases). 
To learn more about an alias of any kind, use `command -v [cmd]`. Read more [here](https://www.cyberciti.biz/faq/ignore-shell-aliases-functions-when-running-command/).

Help for these tools can be found by running `h`, which prints all of the new aliases and descriptions.

There are some Plenty-specific tools; these won't work without Plenty tools installed properly.

## OS-Specific Setup Recommendations (Biased)
These are improvements I recommend making to development environments. They are quite opinionated.

### Mac
1. Run `defaults write com.apple.finder AppleShowAllFiles YES` to show hidden files; ⌥+click in Finder > `Relaunch`
1. Install iTerm2 and check out [styling](https://gist.github.com/kevin-smets/8568070)
1. Use Authy
1. Install [this plugin](https://github.com/yczeng/hackernews-newsfeed) on top of Google Chrome
1. Enable FileVault
1. Remap Caps Lock to Escape on all keyboards in `System Preferences` > `Keyboard` > `Modifier Keys...`
1. Open and update xcode, then run `xcode-select --install`
1. Rename the laptop
1. Add `auth sufficient pam_tid.so` as the second line of `/etc/pam.d/sudo`

### Windows
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
