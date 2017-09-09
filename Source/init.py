""" Importing Python Modules """
from __future__ import print_function
from glob import glob
from os import system, chdir
from os.path import abspath, curdir, isdir, isfile, join, pardir
from shutil import copy, copyfile


class BoilerPlate(object):
    """ Boiler Plate Code """
    def __init__(self):
        # [START] Default Variable
        self.parent_dir = abspath(curdir)
        self.git_hook_dir = '.git/hooks/'
        # [END] Default Variable

        # [START] Check/Create ENV File
        if not self.check_env():
            print('creating .env file')
            if self.clone_env():
                print('.env file created.')
        # [END] Check/Create ENV File

        # [START] Check/Create Laravel Libraries
        self.handle_vendor()
        # [END] Check/Create Laravel Libraries

        # [START] Create Git Hook
        self.clone_hook()
        # [END] Create Git Hook

        # [START] Check/Create Node Modules
        if not self.check_node_modules():
            self.install_node_modules()
        # [END] Check/Create Node Modules

        print('[SUCCESS] Process Completed')

    def check_env(self):
        """ Check if project has .env file """
        if isfile('.env'):
            return True
        else:
            return False

    def clone_env(self):
        """ Cloning .env.example to .env file. """
        copyfile('.env.example', '.env')
        return True

    def handle_vendor(self):
        """ Checking Laravel libraries """
        if self.check_vendor():
            return True
        else:
            self.install_laravel_packages()

    def check_vendor(self):
        """ Check if Laravel libraries are installed """
        if isdir('vendor'):
            print('[Laravel] Package Exists.')
            return True
        else:
            print('[Laravel] Package Does Not Exists!')
            return False

    def generate_app_key(self):
        """ Generate APP KEY in .env file """
        print('[Laravel] Generating App Key.')
        system('php artisan key:generate')
        return None

    def clone_hook(self):
        """ Cloning files from git-hook to .git/hooks directory """
        for hook in glob(join(abspath(curdir), 'git-hook/*')):
            chdir(join(abspath(join(self.parent_dir, pardir)), self.git_hook_dir))
            copy(hook, abspath(curdir))
        else:
            print('[Git] Hooks Cloned')
            chdir(self.parent_dir)

    def install_laravel_packages(self):
        """ Install dependency as per the composer.json file """
        try:
            print('[Laravel] Installing Packages.')
            system('composer install')
        except RuntimeError:
            print('[Laravel] Oops! Something went wrong, while installing packages.')
            return False
        else:
            print('[Laravel] Packages Installed.')
            self.generate_app_key()
            return True

    def check_node_modules(self):
        """ Check if Node Packages are installed """
        if isdir('node_modules'):
            print('[Node] Packages Exists.')
            return True
        else:
            print('[Node] Packages Does Not Exists!')
            return False

    def install_node_modules(self):
        """ Performing npm install """
        try:
            print('[Node] Installing Packages.')
            system('npm install')
        except RuntimeError:
            print('[Node] Oops! Something went wrong, while installing packages.')
            return False
        else:
            print('[Node] Packages Installed.')
            return True

# Execute!
BoilerPlate()
