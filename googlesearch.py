from googlesearch import search as s
keyword=input('Enter a keyword: ')
results=s(keyword,8)
for i in results:
    print(i)