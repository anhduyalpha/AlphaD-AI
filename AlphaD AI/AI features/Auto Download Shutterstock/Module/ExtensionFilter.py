def extract_file_extensions(file_list):
    
    return [file.split('.')[-1] for file in file_list]

def main():
    extract_file_extensions()
if __name__ == '__main__':
    main()