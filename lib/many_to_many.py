# many_to_many.py

from typing import List


class Author:
    """
    Author has a many-to-many relationship to Book through Contract.
    """
    all: List["Author"] = []

    def __init__(self, name: str):
        self.name = name
        Author.all.append(self)

    # --- simple attribute validation via property (optional but tidy) ---
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Author.name must be a string")
        self._name = value

    # --- relationship helpers ---
    def contracts(self) -> List["Contract"]:
        """Return list of Contract instances for this author."""
        return [c for c in Contract.all if c.author is self]

    def books(self) -> List["Book"]:
        """Return unique list of Books for this author via Contract."""
        return list({c.book for c in self.contracts()})

    def sign_contract(self, book: "Book", date: str, royalties: int) -> "Contract":
        """
        Create and return a new Contract for this author and `book`
        with the given date and royalties.
        """
        return Contract(self, book, date, royalties)

    def total_royalties(self) -> int:
        """Sum of royalties from all of this author's contracts."""
        return sum(c.royalties for c in self.contracts())


class Book:
    """
    Book has a many-to-many relationship to Author through Contract.
    """
    all: List["Book"] = []

    def __init__(self, title: str):
        self.title = title
        Book.all.append(self)

    # --- simple attribute validation via property (optional but tidy) ---
    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Book.title must be a string")
        self._title = value

    # --- relationship helpers ---
    def contracts(self) -> List["Contract"]:
        """Return list of Contract instances for this book."""
        return [c for c in Contract.all if c.book is self]

    def authors(self) -> List["Author"]:
        """Return unique list of Authors for this book via Contract."""
        return list({c.author for c in self.contracts()})


class Contract:
    """
    Contract joins an Author to a Book on a given date for a given royalty amount.
    """
    all: List["Contract"] = []

    def __init__(self, author: Author, book: Book, date: str, royalties: int):
        # use property setters for validation
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    # --- validated properties (raise Exception if invalid) ---
    @property
    def author(self) -> Author:
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Contract.author must be an Author")
        self._author = value

    @property
    def book(self) -> Book:
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Contract.book must be a Book")
        self._book = value

    @property
    def date(self) -> str:
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Contract.date must be a str")
        self._date = value

    @property
    def royalties(self) -> int:
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Contract.royalties must be an int")
        self._royalties = value

    # --- class methods ---
    @classmethod
    def contracts_by_date(cls, date: str) -> List["Contract"]:
        """
        Return all contracts that have the same date as the given `date`.
        Preserves insertion order (tests rely on it).
        """
        return [c for c in cls.all if c.date == date]
