# Create a Book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Verify creation
print(Book.objects.all())