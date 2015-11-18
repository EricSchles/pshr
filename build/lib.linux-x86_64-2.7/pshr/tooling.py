def generate_gitignore(file_types=[".pyc","~","#",".pdf",".csv",".txt",".pickle",".json"]):
    with open(".gitignore","w") as f:
        for Type in file_types:
            f.write("*"+Type)

    
