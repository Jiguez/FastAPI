from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


#Devuelve todos los libros
@app.get("/books")
async def read_all_books():
    return BOOKS

#Ejercicio

@app.get("/books/specific_author/")
async def specific_author(author: str):
    books_to_author = []
    for book in BOOKS:
        if book.get('author').lower() == author.lower():
            books_to_author.append(book)

    return books_to_author

#GET

#Con parametros dinamico ( Los parametros estaticos siempre van primero)

@app.get("/books/mybook")
async def read_all_books():
    return {'book_tittle':'My favorite book'}

@app.get("/books/{book_tittle}")
async def read_books(book_tittle: str):
    for book in BOOKS:
        if book.get('title').lower() == book_tittle.lower():
            return book

#Con parametros por query

@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').lower() == category.lower():
            books_to_return.append(book)

    return books_to_return

#Con parametros por path y con query en la funcion

@app.get("/books/{book_author}/")
async def read_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').lower() == book_author.lower() and \
                book.get('category').lower() == category.lower():
            books_to_return.append(book)

    return books_to_return

#POST

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

#PUT

@app.put("/books/update_book")
async def update_book(update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').lower() == update_book.get('title').lower():
            BOOKS[i] = update_book

#DELETE

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').lower() == book_title.lower():
            BOOKS.pop(i)
            break


