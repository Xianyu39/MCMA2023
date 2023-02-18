import requests

API_KEY = 'AIzaSyD6SEcS8iVMPrXUNJ4vmCOracrRrNyFivM'
WORD = 'eerie'

# 构建查询字符串
query = f'https://www.googleapis.com/books/v1/volumes?q={WORD}&key={API_KEY}'

# 发送请求
response = requests.get(query)
if response.status_code!=200:
    print(f"Error: with {response.status_code}")

# 解析响应
data = response.json()

# 获取包含单词的书籍总数
total_books = data['totalItems']

# 计算每本书中单词出现的平均次数
if total_books > 0:
    total_occurrences = sum([item['volumeInfo']['title'].count(WORD) for item in data['items']])
    average_occurrences = total_occurrences / total_books
    print(f"The word '{WORD}' appears on average {average_occurrences} times per book among {total_books} books.")
else:a
    print(f"No books found containing the word '{WORD}'.")
