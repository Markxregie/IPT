import sqlite3

connect = sqlite3.connect('bookmarks.db')
cursor = connect.cursor()


def add(title, url):
    cursor.execute('INSERT INTO bookmarks (Title, URL) VALUES (?, ?)', (title, url))
    conn.commit()

def edit(bk_id, new_title, new_url):
    cursor.execute('UPDATE bookmarks SET Title = ?, URL = ? WHERE Bk_ID = ?', (new_title, new_url, bk_id))
    conn.commit()

def list():
    cursor.execute('SELECT * FROM bookmarks')
    return cursor.fetchall()

def remove(bk_id):
    cursor.execute('DELETE FROM bookmarks WHERE Bk_ID = ?', (bk_id,))
    conn.commit()

def main():
    while True:
        print("\nBookmarks")
        bookmarks = list()
        for bk in bookmarks:
            print(f"({bk[0]}) {bk[1]}{' '*(25-len(bk[1]))}{bk[2]}")

        print("\n(A)dd (E)dit (L)ist (R)emove (Q)uit")
        choice = input("Choose an option: ").strip().upper()

        if choice == 'A':
            title = input("Title: ").strip()
            url = input("URL: ").strip()
            add(title, url)
        elif choice == 'E':
            bk_id = int(input("Number of bookmark to edit: ").strip())
            url = input("URL: ").strip()
            title = input("Title: ").strip()
            edit(bk_id, title, url)
        elif choice == 'L':
            continue
        elif choice == 'R':
            bk_id = int(input("Number of bookmark to remove: ").strip())
            remove(bk_id)
        elif choice == 'Q':
            break
        else:
            print("Invalid option!.")

main()


connect.close()
