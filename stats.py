from typing import Dict, Optional


def get_book_text(filepath):
    try:
        with open(filepath) as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print(f"File with path {filepath} not found")
        return ""
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return ""


def count_book_words(str=""):
    if str == "":
        return 0
    return len(str.split())


def count_characters(str=""):
    output = {}
    if str == "":
        return output
    for value in str:
        final_value = value.lower()
        if final_value not in output:
            output[final_value] = 1
        else:
            output[final_value] += 1
    return output


def sort_characters_count(data: Optional[Dict[str, int]] = None) -> Dict[str, int]:
    if data is None:
        raise ValueError("Input data is None")
    sorted_list = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
    return sorted_list
