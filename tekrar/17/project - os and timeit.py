import sys

commands = dict()

{'-n': ['compress.css'], '-f': ['index.css', '']}

current_command = None
for i in sys.argv:
    if i.startswith('-'):
        current_command = i
        commands[current_command] = []
    elif current_command:
        commands[current_command].append(i)
        

def minify(content):
    result = ''
    
    before_space = False
    is_comment = False
    for i, char in enumerate(content):
        if char == '/' and content[i+1] == '*':
            is_comment = True
        elif char == '/' and content[i-1] == '*' and is_comment:
            is_comment = False
        elif char in ' \t\n' and not is_comment:
            if not before_space:
                result += ' '
                before_space = True
        else:
            if not is_comment:
                result += char
                before_space = False
                
    return result



def combine_and_minify_files(file_names):
    result = ''
    for name in file_names:
        with open(name, mode='r', encoding='UTF-8') as file:
            file_content = file.read()
        minified_content = minify(file_content)
        result += minified_content
    return result



file_names = commands['-f']
new_file_name = commands['-n'][0]

result = combine_and_minify_files(file_names)

with open(new_file_name, 'w', encoding='utf-8') as file:
    file.write(result)
        
        
        
        