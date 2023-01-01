def read_first_line(filename: str) -> str:
    with open(f'bot_package//text_files//{filename}', 'r') as file:
        return file.readline()
