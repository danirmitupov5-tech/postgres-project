from db import engine, SessionLocal
from models import Base, Category, Book
from crud import create_category, create_book, get_category_by_name

def init_db():
    # Создаём таблицы
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    # Создаём категории с price
    categories = [
        ("Фантастика", "Научная фантастика и фэнтези книги", 1000.0),
        ("Детектив", "Криминальные романы и детективы", 800.0),
        ("Классика", "Мировая классическая литература", 600.0),
        ("Программирование", "Книги по программированию и IT", 1500.0),
    ]
    
    for name, desc, price in categories:
        create_category(db, name, desc, price)
    
    # Создаём книги (title, description, price, url, category_id)
    books_data = [
        ("1984", "Роман-антиутопия Джорджа Оруэлла", 450.0, "https://example.com/1984", "Фантастика"),
        ("Война миров", "Научно-фантастический роман Герберта Уэллса", 350.0, "https://example.com/war-of-worlds", "Фантастика"),
        ("Убийство в Восточном экспрессе", "Детектив Агаты Кристи", 400.0, "https://example.com/murder", "Детектив"),
        ("Преступление и наказание", "Роман Фёдора Достоевского", 500.0, "https://example.com/crime", "Классика"),
        ("Гордость и предубеждение", "Роман Джейн Остин", 420.0, "https://example.com/pride", "Классика"),
        ("Clean Code", "Книга Роберта Мартина о чистом коде", 1800.0, "https://example.com/clean-code", "Программирование"),
    ]
    
    for title, desc, price, url, category_name in books_data:
        category = get_category_by_name(db, category_name)
        if category:
            create_book(db, title, desc, price, url, category.id)
    
    db.close()
    print("База данных инициализирована успешно!")
    print("\nДобавленные категории и книги содержат поля: description, price, url")

if __name__ == "__main__":
    init_db()