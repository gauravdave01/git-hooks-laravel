# Git Hook + Laravel 5 #
This repository is based on git hooks. The idea behind this repository is there are basic task (like `composer install`, `npm install`, `php artisan migrate:refresh` etc), which sould be addressed automatically. So, that developer doesn't need to engage in those simple tasks, and which get address automatically.

This handles operations, which are performed when you setup a project and when you start working on it, and collaborating with other developer.

***

## Git Hooks ##

* Git hooks are scripts that Git executes before or after events such as: commit, push, and receive
* Git hooks are a built-in feature - no need to download anything. Git hooks are run locally

***

There are 3 files which you need to go through, to understand this repository:

1. **.env.example**
> You'll find 2 new key:
> - `DB_MIGRATION=false`
> - `DB_MIGRATION_REFRESH=true`
>
> When you want to perform Laravel Migration (i.e. `php artisan migrate`) on contributors machine, then set: <br>
> `DB_MIGRATION=`**true**,
>
> and when you want to perform Laravel Migration Refresh (i.e. `php artisan migrate:refresh`), then set: <br>
> `DB_MIGRATION_REFRESH=`**true**
>
> Then, commit the .env.example file and push it to server. As you won't be able to commit the .env file. Migration related changes will be handled by .env.example file.

2. **`init.py`**
> This script is written in Python 3. What it does:
> - Clone **.env.example** file to **.env**
> - Install Laravel packages i.e. `composer install`
> - Generate App Key (`php artisan key:generate`)
> - Clone *git-hooks* consisting files, to **.git**'s hooks folder.
> - Install node packages [referring package.json] (`npm install`)

3. **git-hook/post-merge**
> - It include *post-merge* file, which gets called, whenever contributor successfully, takes a pull (without conflicts). <br>
> - When the pull is executed, it checks all changed file, if there **.env.example** file. <br>
> - If there's, then it will check if the migration flag has a `true` value assigned to it. <br>
> - Based on the flag, it will perform DB (database) changes.

***

## Project Flow ##

* Install Python 3 (minimum requirement)
* Run `python3 init.py` to execute initialising script.

**Note:** *.git* folder is marked in *.gitignore* file, so you have to make sure your contributors also perform this step, else you and other contributors won't be able to take advantage of git hooks.

* Update your .env file with DB Credentials.
* Create vhost, hosts entry.
* Restart your server.
* After starting with the development,

***

### **Note** ###

This hook is created taking into consideration that when developers create a product/website, there are changes in `DB (database) Architecture`, and which leads to change in migration, and then they have to share this changes to fellow developers who may and may not be sitting next to each other. Also, use this with precaution when you're migrating from staging to production environment, as you don't want to refresh your DB, when you're already live and have genuine entries.

***

## Contribution guidelines ##

* Code review
* Feel free to add elegant enhancements
