def read_file(filename: str) -> list:
    with open(f'bot_package//text_files//{filename}', 'r') as file:
        return file.read_lines()
