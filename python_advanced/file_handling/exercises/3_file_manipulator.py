import os


def file_existing_check(file_name):
    try:
        with open(f"{file_name}", "r") as file:
            return True
    except FileNotFoundError:
        return False


def create(file_name):
    file_name = file_name[0]
    with open(f"{file_name}", "w") as file:
        file.write("")


def add(list_of_args):
    file_name, content = list_of_args
    with open(f"{file_name}", "a") as file:
        file.write(f"{content}\n")


def replace(list_of_args):
    file_name, old_string, new_string = list_of_args
    if file_existing_check(file_name):
        with open(f"{file_name}", "r+") as file:
            content = " ".join(file.readlines())
            replaced_content = content.replace(old_string, new_string)
            file.seek(0)
            file.writelines(replaced_content.split(" "))
    else:
        print("An error occurred")


def delete(file_name):
    if file_existing_check(file_name):
        os.remove(file_name)
    else:
        print("An error occurred")


COMMAND_MAPPER = {
    "Create": create,
    "Add": add,
    "Replace": replace,
    "Delete": delete
}

while True:
    line = input()
    if line == "End":
        break
    command, *arguments_list = line.split("-")
    COMMAND_MAPPER[command](arguments_list)

