# Create a Book instance
from bookshelf.models import Book

# Create a Book instance in one step
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Verify creation
print(Book.objects.all())
