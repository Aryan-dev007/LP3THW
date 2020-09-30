import sys
script , input_encoding , error = sys.argv


def main(language_file , encoding , errors):
    line = language_file.readline()

    if line:
        print_line(line , encoding , errors)
        return main(language_file , encoding , errors)


def print_line(line , encoding , errors):
    next_lang = line.strip()
    print(next_lang)
    #raw_bytes = next_lang.encode(encoding , errors=errors)
    cooked_string = next_lang.decode(encoding,errors=errors)
    raw_bytes = cooked_string.encode(encoding , errors=errors)


    print(cooked_string,"<===>",raw_bytes)

#languages = b"\xd0\x90\xd2\xa7\xd1\x81\xd1\x88\xd3\x99\xd0\xb0" 
languages = open("languages.txt",'rb')
main(languages , input_encoding , error)