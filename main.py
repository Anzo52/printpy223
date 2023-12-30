import glob
import os
import tokenize

def process_file(filepath):
    with tokenize.open(filepath) as f:
        tokens = list(tokenize.tokenize(f.readline))
        new_tokens = []
        skip_next = False
        for token in tokens:
            if skip_next:
                skip_next = False
                continue
            if token.type == tokenize.NAME and token.string == 'print':
                next_token = next(tokens)
                if next_token.string != '(':
                    new_tokens.extend([
                        token,
                        tokenize.TokenInfo(tokenize.OP, '(', token.start, token.end, ''),
                        next_token,
                        tokenize.TokenInfo(tokenize.OP, ')', next_token.start, next_token.end, '')
                    ])
                    skip_next = True
                else:
                    new_tokens.extend((token, next_token))
            else:
                new_tokens.append(token)
        new_content = tokenize.untokenize(new_tokens)
        f.seek(0)
        f.truncate()
        f.write(new_content)

def update_print_statements(directory):
    for filepath in glob.iglob(os.path.join(directory, '**', '*.py'), recursive=True):
        print(filepath)
        process_file(filepath)

def main():
    directory = input("Enter the path to your package (must be absolute path): ")
    update_print_statements(directory)

if __name__ == "__main__":
    main()
