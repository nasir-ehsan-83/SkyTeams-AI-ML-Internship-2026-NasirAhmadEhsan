import os 

# rename specific file 
def rename_file(old_name: str, new_name: str):
    return os.rename(old_name, new_name)