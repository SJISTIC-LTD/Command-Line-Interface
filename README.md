# Command-Line-Interface
A command-line interface (CLI) usually starts with the name of the executable. You just enter it’s name in the console and you access the main entry point of the script, an example is pip.
There are parameters you need to pass to the script depending how they are developed and they can either be:
Arguments: This is a required parameter that’s passed to the script. If you don’t provide it, the CLI will run into an error. For instance, django is the argument in this command: pip install django.
Options: As the name implies, its is an optional parameter which usually comes in a name and a value pair such as pip install django --cache-dir ./my-cache-dir. The --cache-dir is an option param and the value ./my-cache-dir should be uses as the cache directory.
Flags: This is special option parameter that tells the script to enable or disable a certain behaviour. The most common one is probably --help.
With complex CLIs like the Heroku Toolbelt, you’ll be able access some commands that are all grouped under the main entry point . They are usually regarded as commands or sub-commands.
