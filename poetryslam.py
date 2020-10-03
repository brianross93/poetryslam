import random



def get_file_lines(filename):
    """
    gets lines from txt and returns string
    """
    poetry_file_name = "/Users/brianross/dev/courses/cs1.0/Poetry Slam/poem.txt"
    poem_Open = open(poetry_file_name, 'r').readlines()
    poem = []
    for line in poem_Open:
        poem.append(line.strip())
    
    
    return poem
    
print(get_file_lines('poem.txt'))
def lines_printed_backwards(lines_list):
    lines_list = open("/Users/brianross/dev/courses/cs1.0/Poetry Slam/poem.txt", 'r').readlines()
    number_line = len(lines_list)
    #backwards_poem = []
    lines_list = lines_list[::-1]
    for line in range(len(lines_list)): 
        reverse_number = str(number_line - line) + " " + lines_list[line]
        #backwards_poem.append(line.rstrip())
        print(reverse_number)
    return lines_list
    

def lines_printed_random(lines_list): 
    lines_list = open("/Users/brianross/dev/courses/cs1.0/Poetry Slam/poem.txt", 'r').readlines()
    for line in lines_list:
        line = random.randrange(len(lines_list))
        random_line = str(line) + " " + lines_list[line]
        print(random_line)

def lines_printed_custom(lines_list): 
    lines_list = open("/Users/brianross/dev/courses/cs1.0/Poetry Slam/poem.txt", 'r').readlines()
    for line in range(len(lines_list)): 
        if (line % 2 == 0):
            print(line, lines_list[line])
    

lines_printed_backwards("poem.txt")
lines_printed_random("poem.txt")
lines_printed_custom("poem.txt")
