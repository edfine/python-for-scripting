from collections import Counter, defaultdict
import re
import pathlib
from sys import path

def main():
    # Path setup to RJ file
    path_to_parent_folder = pathlib.Path(__file__).parent.absolute()
    path_to_rj = path_to_parent_folder / 'book-texts' / 'romeo-and-juliet-no-header-footer.txt'

    lines_by_speaker, word_counts_by_speaker = count_lines_and_words(path_to_rj)

    for speaker, lines in lines_by_speaker.most_common():
        print(f'{speaker} had {lines} lines.')
        print('  In those lines, they said these words most often...')
        for word, count in word_counts_by_speaker[speaker].most_common()[0:10]:
            print('    ', word, count)


def count_lines_and_words(path_to_book):
    # Basic setup
    current_speaker = ''
    lines_by_speaker = Counter()
    word_counts_by_speaker = defaultdict(Counter)

    
    with open(path_to_book, 'r') as rj_reader:
        line = 'will be ignored...'

        while line != '':
            line = rj_reader.readline()

            if line_is_nonspeaking(line):
                continue

            new_speaker, line = detect_and_remove_speaker(line)
            if new_speaker:
                current_speaker = new_speaker

            line = remove_internal_stage_directions(line)

            # If we are here, we know it's a speaking line, so lets update the count and words
            lines_by_speaker[current_speaker] += 1
            words_in_this_line = line.strip().split()
            for word in words_in_this_line:
                # remove punctuation from the word
                word = re.sub(r'\W+', '', word).lower()

                word_counts_by_speaker[current_speaker][word] += 1

    return lines_by_speaker, word_counts_by_speaker 
            

def line_is_nonspeaking(line):
    '''
    Return True if the line is a nonspeaking line
    False otherwise.
    '''
    non_speaking_pattern = r'^\S'
    full_line_stage_direction_pattern = r'^ {5,}'
    stripped_line = line.strip()

    is_nonspeaking = (
        re.search(non_speaking_pattern, line) or
        re.search(full_line_stage_direction_pattern, line) or
        stripped_line.startswith("Enter") or 
        stripped_line.startswith("Exit")
    )

    return is_nonspeaking

def detect_and_remove_speaker(line):
    '''
    If the line matches the pattern for a new speaker return (True, name, new_line)
    where name is the name of the new speaker. Otherwise return (False, None, line)
    '''
    new_speaker_pattern = r'^  ([A-Z1-9][a-z]* ?[A-Za-z]*?)\. '
    match = re.search(new_speaker_pattern, line)
    if match:
        current_speaker = match.group(1)
        
        # We also don't want to count the names as spoken words.
        line_without_speaker = re.sub(new_speaker_pattern, '', line)
        return (current_speaker, line_without_speaker)
    
    return (None, line)


def remove_internal_stage_directions(line):
    '''
    If the line contains internal stage directions, remove them from the line.
    Either way, return the line.
    '''
    stage_direction_pattern = r'\[.*?\]'
    if re.search(stage_direction_pattern, line):
        minus_stage_directions = re.sub(stage_direction_pattern, '', line)
        return minus_stage_directions

    return line

if __name__ == '__main__':
    main()