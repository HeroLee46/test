import re                                                 #import re library

def search_log(file_path):                                #create search function
    with open(file_path, 'r', encoding="utf-8") as file:   
        for line in file:                                  #find the keyword using for loop
            if re.search(find_word, line, re.IGNORECASE):  #if re.search(r'(error|fail)', line, re.IGNORECASE):
                print(line.strip())                        #print the whole line  

# 指定 log 檔案的路徑
# log_file_path = 'C:\\Users\\Hero\\Downloads\\dism.txt'

find_file = input('請輸入你要找的檔案實體位置:')             #input the log path  
find_word = input('請輸入你要找的字:')                      #input the keyword

# 呼叫函式進行搜尋
search_log(find_file)                                     #search the keyword  
