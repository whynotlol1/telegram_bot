def read_file(filename: str) -> str:
    with open(f'bot//text_files//{filename}', 'r') as file:
        return file.read()
