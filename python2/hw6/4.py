def modify(num_lines, lines):
    modified_lines = []
    for line in lines:
        modified_line = line.replace(' && ', 'and').replace(' || ', 'or')
        modified_lines.append(modified_line)
    return modified_lines

if __name__ == "__main__":
    num_lines = int(input().strip())
    lines = [input().strip() for _ in range(num_lines)]
    text = modify(num_lines, lines)
    for modified_line in text:
        print(modified_line)
