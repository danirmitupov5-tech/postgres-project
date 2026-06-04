from db import SessionLocal
from crud import get_categories, get_books

def main():
    db = SessionLocal()
    
    print("=" * 50)
    print("КАТЕГОРИИ:")
    print("=" * 50)
    
    categories = get_categories(db)
    for cat in categories:
        print(f"ID: {cat.id} | Название: {cat.name} | Описание: {cat.description}")
    
    print("\n" + "=" * 50)
    print("КНИГИ:")
    print("=" * 50)
    
    books = get_books(db)
    for book in books:
        print(f"ID: {book.id} | {book.title} | {book.author} ({book.year}) | Категория: {book.category.name}")
    
    db.close()

if __name__ == "__main__":
    main()