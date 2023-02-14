class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        ...
        return self._name

    @property
    def author(self) -> str:
        ...
        return self._author

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.name!r}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name = {self.name!r}, author = {self.author!r})"

class AudioBook(Book):
    def __init__(self, duration: float):
        super().__init__(name, author)
        self._duration = None
        self.set_duration(duration)
    def set_duration(self, new_duration: float):
        if not isinstance(new_duration, float):
            raise ValueError("значение не является float")
        if new_duration <= 0:
            raise ValueError("Значение должно быть больше нуля")
        self._duration = new_duration
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name = {self.name!r}, author = {self.author!r}, duration = {self._duration!r})"

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = None
        self.set_pages(pages)
    def set_pages(self, new_pages: int):
        if not isinstance(new_pages, int):
            raise ValueError("значение не является int")
        if new_pages <= 0:
            raise ValueError("Значение должно быть больше нуля")
        self._pages = new_pages
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name = {self.name!r}, author = {self.author!r}, pages = {self._pages!r})"
book = PaperBook("Фауст", "Гёте",900)
print(str(book))
book.set_pages(700)
print(repr(book))