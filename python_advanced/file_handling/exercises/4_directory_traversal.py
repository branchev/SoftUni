import os


def file_filter(dir_list):
    return [el for el in dir_list if os.path.isfile(el)]


def report_dir_content(files_list):
    files_extensions_holder = {}
    for f in files_list:
        extension = f.split(".")[1]
        if extension not in files_extensions_holder:
            files_extensions_holder[extension] = []
        files_extensions_holder[extension].append(f)
    return files_extensions_holder


def result_to_string(reported):
    result = ""
    for ext, files in sorted(reported.items(), key=lambda x: x[0]):
        result += f".{ext}" + "\n"
        for file in files:
            result += f"- - - {file}" + "\n"
    return result


def file_creator_to_desktop(string_content):
    desktop_path = r"C:\Users\Dell\Desktop\\"
    with open(f"{desktop_path}report.txt", "w") as file:
        file.writelines(string_content)


files_list = file_filter(os.listdir())
reported = report_dir_content(files_list)
result_str = result_to_string(reported)
file_creator_to_desktop(result_str)