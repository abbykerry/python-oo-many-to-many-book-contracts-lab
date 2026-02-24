# =========================
# Author Class
# =========================
class Author:
    """
    Represents an author.
    An author can have many books through contracts.
    """

    # Class attribute to store all Author instances
    all = []

    def __init__(self, name):
        """
        Initialize an Author with a name.
        """
        self.name = name
        Author.all.append(self)

    def contracts(self):
        """
        Returns a list of all Contract instances
        associated with this author.
        """
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """
        Returns a list of all Book instances
        associated with this author through contracts.
        """
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """
        Creates and returns a new Contract between
        this author and the given book.
        """
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """
        Returns the total royalties earned by this author
        from all of their contracts.
        """
        return sum(contract.royalties for contract in self.contracts())


# =========================
# Book Class
# =========================
class Book:
    """
    Represents a book.
    A book can have many authors through contracts.
    """

    # Class attribute to store all Book instances
    all = []

    def __init__(self, title):
        """
        Initialize a Book with a title.
        """
        self.title = title
        Book.all.append(self)

    def contracts(self):
        """
        Returns a list of all Contract instances
        associated with this book.
        """
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """
        Returns a list of all Author instances
        associated with this book through contracts.
        """
        return [contract.author for contract in self.contracts()]


# =========================
# Contract Class
# =========================
class Contract:
    """
    Represents a contract between an Author and a Book.
    This is the join model that creates a many-to-many relationship.
    """

    # Class attribute to store all Contract instances
    all = []

    def __init__(self, author, book, date, royalties):
        """
        Initialize a Contract with validation.
        """

        # Validate author
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")

        # Validate book
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")

        # Validate date
        if not isinstance(date, str):
            raise Exception("date must be a string")

        # Validate royalties
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """
        Returns a list of all contracts that match the given date.
        """
        return [contract for contract in cls.all if contract.date == date]