input_filename = 'input.txt'
output_filename = 'newscores.txt'

def update_scores(input_filename, ouput_filename):
    with open(input_filename, 'r') as infile, open(ouput_filename, 'w') as outfile:
        for line in infile:
            username, score = line.strip().split()
            new_score = int(score) + 5
            outfile.write(f'{username} {new_score}\n')

print('New scores saved to newscores.txt')
