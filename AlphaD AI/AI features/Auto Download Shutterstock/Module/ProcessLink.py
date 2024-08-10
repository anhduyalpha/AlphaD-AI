def process_name_image(Original_link):
    
    string_input = Original_link.replace("https://www.shutterstock.com/vi/image-photo/","").replace("-", " ").title()
    num ='1234567890'
    string_without_num = ""
    id_image = ""
    ID = "ID"

    for i in string_input:
        if i not in num:
            string_without_num += i
    for i in string_input:
        if i in num:
            id_image += i
    string_output = f"{string_without_num}{ID} {id_image}.jpg "
    return string_output, string_without_num, id_image
            
def main():
    process_name_image()
if __name__ == "__main__":
    main()