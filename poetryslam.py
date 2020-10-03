poetry_file_name = "poem.txt"
poem_Open = open(poetry_file_name, 'r')



def get_file_lines(filename):
    """
    gets lines from txt and returns string
    """
    poem_string_list = poem_Open.readlines()
 
    return poem_string_list

print(get_file_lines(poetry_file_name))

poem_Open.close()