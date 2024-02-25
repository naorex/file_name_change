import os

work_path = input("作業するフォルダのパスを入力: ")
target_word = input("一括置換したい文字列を入力: ")
replace_word = input("代入する文字列を入力: ")


file_list = os.listdir(work_path)

for file_name in file_list:
    file_name_r = file_name.replace(target_word, replace_word)
    file_path_full = work_path + "\\" + file_name
    file_path_full_r = work_path + "\\" + file_name_r
    os.rename(file_path_full, file_path_full_r)
