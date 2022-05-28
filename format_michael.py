import os
import re

"""
Takes the output of the scraper, finds all the Michael Scott quotes, and formats
them for ingestion into a machine learning progrma.
"""

def append_to_file(filename: str, string: str):
    append_file = open(f"michael_interactions/{filename}", "a")
    append_file.write(string + "\n")
    append_file.close()


def process():
    directory = os.fsencode("./output/")

    for filepath in os.listdir(directory):
        filepath_str = os.fsdecode(filepath)
        filename = os.path.basename(filepath_str)
        with open(f"./output/{filepath_str}", "r") as file:
            last_line = ''
            for line in file:
                line = line.rstrip()
                line = re.sub('\[.*?\]', '', line)
                try:
                    if line.startswith("Michael:"):
                        if last_line == '---':
                            line_i = line.index(':')
                            # append_to_file(filename, line)
                            append_to_file(filename, "|| " + line[line_i+1:].strip())
                        else:
                            # append_to_file(
                            #     filename,
                            #     last_line + " || " + line
                            # )
                            line_i = line.index(':')
                            last_line_i = last_line.index(':')
                            append_to_file(
                                filename,
                                last_line[last_line_i+1:].strip() + " || " + line[line_i+1:].strip()
                            )
                except ValueError:
                    continue

                last_line = line


if __name__ == '__main__':
    process()
