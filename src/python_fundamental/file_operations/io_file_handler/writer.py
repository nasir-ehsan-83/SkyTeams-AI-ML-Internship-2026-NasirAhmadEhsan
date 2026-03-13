# Write text into a file
def write_text(file, text: str) -> None:
    file.seek(0)
    file.write(text)
    file.truncate()
