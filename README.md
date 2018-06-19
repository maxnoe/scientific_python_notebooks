# e2_hardskill_seminar
Introduction to Scientific Python for Solid State Physicists at TU Dortmund 2018


## Installation

For python, we will use anaconda. We will be using python 3.6.

### Windows

Please think about installing either the Windows Subsystem for Linux, this will make things much easier:

https://docs.microsoft.com/en-us/windows/wsl/install-win10

If you did this already, continue with the Linux installation guide.

If you do not want to use the WSL, download the windows version of Anaconda here:
https://www.anaconda.com/download/#windows

** When asked if you want to add anaconda to PATH, answer yes, although it's not recommended**

For git, install https://github.com/git-for-windows/git/releases/download/v2.17.1.windows.2/Git-2.17.1.2-64-bit.exe

### Linux

1. Install required distribution packages :
  - Ubuntu/Debian: `sudo apt-get install -y git bzip2 wget`
  - Fedora 25: `sudo dnf install -y git wget bzip2`
  - CentOS/RHEL: `sudo yum install -y git bzip2 wget`

1. Run the following two commands in the terminal to download and install anaconda:
  ```
  $ wget https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh
  $ bash Anaconda3-5.2.0-Linux-x86_64.sh
  ```

1. Accept the License by pressing `<Enter>`, then scrolling down to the bottom using `<space>` and writing `yes`

1. Choose the install location, I recommend `~/.local/anaconda3` instead of `~/anaconda3` to not mess up you home too much.

1. After the installation, you are asked if you want to add conda to the `PATH`. Answer `no`.

    ```
    Do you wish the installer to prepend the Anaconda3 install location
    to PATH in your /home/username/.bashrc ? [yes|no]
    [no] >>> no
    ```

1. Edit your `.bashrc` to include these two lines at the end:

  ```
  . "$HOME/.local/anaconda3/etc/profile.d/conda.sh" 
  conda activate
  ```


### MacOS

1. Open a terminal and install git:

  ```
  $ xcode-select --install
  ```

1. Run the following two commands in the terminal to download and install anaconda:
  ```
  $ curl -LO https://repo.anaconda.com/archive/Anaconda3-5.2.0-MacOSX-x86_64.sh
  $ bash Anaconda3-5.2.0-MacOSX-x86_64.sh
  ```

1. Accept the License by pressing `<Enter>`, then scrolling down to the bottom using `<space>` and writing `yes`

1. Choose the install location, I recommend `~/.local/anaconda3` instead of `~/anaconda3` to not mess up you home too much.

1. After the installation, you are asked if you want to add conda to the `PATH`. Answer `no`.

    ```
    Do you wish the installer to prepend the Anaconda3 install location
    to PATH in your /home/username/.bashrc ? [yes|no]
    [no] >>> no
    ```

1. Edit your `.bashrc` to include these two lines at the end:

  ```
  . "$HOME/.local/anaconda3/etc/profile.d/conda.sh"
  conda activate
  ```
