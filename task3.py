import csv
import json

# read csv file
with open('books.csv', 'r') as f:
    books = csv.DictReader(f)
    books = [i for i in books]

    # count the number of books #211
    cnt_books = 0
    for book in books:
        cnt_books += 1


# read json file
with open('users.json', 'r') as f:
    users = json.load(f)

# add new key 'books' to each user
for user in users:
    user['books'] = []


#count the number of users #28
cnt_users = len(users)


#sharing books to users
while books:
    for user in users:
        if books:
            user['books'].append(books.pop())
        else:
            break


# save result to result.json
with open('result.json', 'w') as f:
    json.dump(users, f, indent=4)







