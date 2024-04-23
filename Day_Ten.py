#Functions with Outputs

def format_name(f_name, l_name):
    """This function take a first and last name and format it to return the title case"""
    if f_name == "" or l_name == "":
        return 
    formated = f_name.title()
    formated_l = l_name.title()

    return f"{formated} {formated_l}"

formated_String = format_name("angela", "ANGELA")
print(formated_String)

#Docstrings
