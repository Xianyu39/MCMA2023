import pandas as pd
file_path = 'Problem_C_Data_Wordle.xlsx'
df = pd.read_excel(file_path)

words_colum='Word'
words = df[words_colum]
# print(words)
def count_letters(word):
    # 将单词转换为小写，以避免区分大小写
    word = word.lower()

    # 创建一个字典来存储每个字母出现的次数
    letter_counts = {}

    # 遍历单词的每个字符，并将字符添加到字典中
    for char in word:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    max_count = 0
    max_letter = ''
    for letter, count in letter_counts.items():
        if count > max_count:
            max_count = count
            max_letter = letter

    return max_count

results_column = 'Replication number'
results = []
for word in words:
    counts = count_letters(word)
    results.append(counts)
df[results_column] = results
with pd.ExcelWriter(file_path) as writer:
    df.to_excel(writer, index=False)