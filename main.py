from db import SessionLocal
from crud import get_categories, get_books

def main():
    db = SessionLocal()
    
    print("=" * 70)
    print("КАТЕГОРИИ (с полями description, price):")
    print("=" * 70)
    
    categories = get_categories(db)
    for cat in categories:
        print(f"ID: {cat.id} | Название: {cat.name}")
        print(f"    Описание: {cat.description}")
        print(f"    Цена: {cat.price} руб.")
    
    print("\n" + "=" * 70)
    print("КНИГИ (с полями description, price, url):")
    print("=" * 70)
    
    books = get_books(db)
    for book in books:
        print(f"ID: {book.id} | {book.title}")
        print(f"    Описание: {book.description}")
        print(f"    Цена: {book.price} руб.")
        print(f"    URL: {book.url}")
        print(f"    Категория: {book.category.name}")
        print("-" * 50)
    
    db.close()

if __name__ == "__main__":
    main()