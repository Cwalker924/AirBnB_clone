#!/usr/bin/python3
import cmd
import sys
import os
from models import *
"""
This is the HBNB console module
"""


class Console(cmd.Cmd):
    """ Console Interpreter"""
    prompt = "(hbnb) "
    class_names = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                   "Review"]

    def do_exit(self, args):
        """Exits the  Console with 'Ctrl + d'"""
        quit()

    def do_EOF(self, args):
        """Exits system with end of file character 'control' + 'c'"""
        print("")
        return (True)

    def do_shell(self, args):
        """Pass system shell if line starts with '!' character"""
        os.system(args)

    def do_help(self, args):
        """Gets help command if 'help' or '?' is passed"""
        cmd.Cmd.do_help(self, args)

    def do_quit(self, args):
        """Quit command to exit the program"""
        raise SystemExit

    def emptyline(self):
        """Prevents repeat of previous input."""
        pass

    def do_create(self, args):
        """ Creates an instance of a given model """
        model = {"BaseModel": models.BaseModel(), "User": models.User(),
                 "State": models.State(), "City": models.City(),
                 "Amenity": models.Amenity(), "Place": models.Place(),
                 "Review": models.Review()}
        if len(args) < 1:
            print("** class name missing **")
        else:
            if args in model.keys():
                value = model[args]
                new = value
                new.save()
                print(new.id)
            else:
                print ("** class doesn't exist **")
                return

    def do_show(self, args):
        """ Prints the string representation of an instance based on the class
        name and id """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] not in Console.class_names:
            print("** class doesn't exist **")
            return
        else:
            show_all = storage.all()
            for key_id in show_all.keys():
                if key_id == args[1]:
                    print(show_all[key_id])
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id """
        #import pdb; pdb.set_trace()
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in self.class_names:
            print("** class doesn't exist **")
        show_all = storage.all()
        if args[1] in show_all.keys():
            del show_all[args[1]]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """ all method
        shows all Classes created of a given class
        """
        show_list = []
        store = models.storage.all()

        args = args.split()
        if args[0] not in self.class_names:
            print("** class doesn't exist **")
            return
        else:
            for key in store.keys():
                if store[key].__class__.__name__ == args[0]:
                    show_list.append(str(store[key]))
            print(show_list)

    def do_update(self, args):
        """ Updates an instance based on the class name and id by adding or
        updating attribute """
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        stored_obj = models.storage.all()
        if args[1] in stored_obj.keys():
            setattr(stored_obj[args[1]], args[2], args[3])
            models.storage.save()
        else:
            print("** no instance found **")

if __name__ == "__main__":
    prompts = Console()
    prompts.cmdloop()
