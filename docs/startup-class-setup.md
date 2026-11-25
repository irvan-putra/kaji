# startup-class/setup: a 2013 EC2 setup script, read

Checked 25 November 2026. Public pages only. Read, not run.

Source: https://github.com/startup-class/setup (described as "AWS EC2 setup files for Startup Engineering MOOC"; homepage http://coursera.org/course/startup; created 1 July 2013; shell; top contributor balajis; 294 stars and 1,224 forks when checked).

## What is in it

Two files: `README.md` and `setup.sh` (1,346 bytes). No license file is in the tree, so we read it for ideas and copy nothing.

The README says to run it on a fresh EC2 instance with Ubuntu 12.04.2 LTS:

```sh
cd $HOME
sudo apt-get install -y git-core
git clone https://github.com/startup-class/setup.git
./setup/setup.sh
```

It points to a companion repo, https://github.com/startup-class/dotfiles, and to the course's lectures 4a/4b.

## What setup.sh does, in order

| Step | What it does |
| --- | --- |
| Basics | Installs git and curl with apt. |
| Node | Installs nvm with a `curl ... | sh` line, then installs and selects Node v0.10.12. |
| JS tooling | Installs jshint globally with npm, and rlwrap for a nicer node REPL. |
| Editor | Adds a PPA, then installs emacs24 (terminal-only build). |
| Deploy tool | Installs the Heroku toolbelt with `wget -qO- ... | sh`. |
| Dotfiles | Clones the dotfiles repo, moves any existing `dotfiles` and `.emacs.d` aside, then symlinks `.screenrc`, `.bash_profile`, `.bashrc`, `.bashrc_custom` and `.emacs.d` into `$HOME`. |

The idea worth keeping: the whole machine, tools and personal config, comes back from one repo and one command, so a throwaway cloud box is cheap to lose.

## What has aged (observed in the file, not tested)

- It targets one Ubuntu release from 2013 and Node 0.10.12. Both are far behind today's versions.
- The nvm install URL uses a `raw.github.com` address and an old project path. Heroku's toolbelt and the emacs PPA are third-party sources that may no longer exist.
- Two of the steps pipe a downloaded script straight into a shell, with no checksum or pinned version.
- The script has no `set -e`, so a failed step does not stop it, and nothing prints which steps worked.
- Backups use `mv dotfiles dotfiles.old`. On a second run, `dotfiles.old` already exists, so the move would behave differently from the first run. Not run, so this is a reading of the code.

## What we take from it

- Keep machine setup in a script in a repo, not in memory.
- Keep personal config (dotfiles) in a separate repo from the install script, so each changes at its own pace.
- Pin versions you depend on, and write down the OS version the script was written for.
- Make the script safe to run twice, and stop on the first error.
- Prefer a downloaded-then-read script to a pipe into a shell.

## Sanggup practice

- Coding: write a repeatable setup for a new machine: https://vanipy.com/sanggup/#coding/cd33

## Sources

- https://github.com/startup-class/setup
- https://raw.githubusercontent.com/startup-class/setup/master/setup.sh
- https://github.com/startup-class/dotfiles
