# NOTE: This starter code is intentionally incomplete so all tests fail.
# Students will need to define the parser, subcommands, and handlers.

# TODO: Import the argparse module

# TODO: Define the add_task function
# This function should accept 'args' and print: ✅ Task added: <description>

# TODO: Define the list_tasks function
# This function should accept 'args' and print: 📋 Listing all tasks...

# TODO: Define the main() function
# Inside main():
# - Create an ArgumentParser with a helpful description
# - Add subparsers for "add" and "list" commands
# - For "add", require a "description" argument and set its handler
# - For "list", just set the handler to list_tasks
# - Parse the arguments and call the appropriate handler (if exists)

import argparse

def add_task(args):
  print(f"✅ Task added: {args.description}")

def list_tasks(args):
  print(f"Listing all tasks...")

def main():
  parser = argparse.ArgumentParser(description = "Task Manager CLI")
  subparsers = parser.add_subparsers()

  #Add command
  add_parser = subparsers.add_parser("add", help="Add a new task")
  add_parser.add_argument("description", help="Description of the task")
  add_parser.set_defaults(func=add_task)

  #List command
  add_parser = subparsers.add_parser("list", help="List all tasks")
  add_parser.set_defaults(func=list_tasks)

  args = parser.parse_args()

  #Handle missing command
  if hasattr(args, "func"):
    args.func(args)
  else:
    parser.print_help()