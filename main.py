import os

def update_print_statements(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    lines = f.readlines()

                with open(filepath, 'w') as f:
                    for line in lines:
                        if 'print ' in line and '#' not in line:
                            line = line.replace('print ', 'print(').rstrip() + ')\n'
                        f.write(line)

# Replace this with the path to your package
def main():
    directory = input('Enter the absolute path to your package: ')
    update_print_statements(directory)
    
if __name__ == '__main__':
    main()