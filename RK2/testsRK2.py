import unittest 
from RK2 import run_book, sort_name, book_in_lib, Book, Library, BookLibrary
from operator import itemgetter
class test_RK2(unittest.TestCase):
    def setUp(self):
        self.Books = [
            Book(1, 'Анна Каренина', 4, 1),
            Book(2, 'Война и Мир', 10, 1),
            Book(3, 'Мертвые души', 3, 2),
            Book(4, 'Преступление и наказание', 3, 2),
            Book(5, 'Унесенные Ветром', 5, 3),
            Book(6, 'Горе от ума', 6, 4)]

        self.Lib = [
            Library(1, ' Л. Н. Толстой'),
            Library(2, 'Русская проза'),    
            Library(3, 'Зарубежная проза'),
            Library(4, 'Пьеса')]

        self.books_lib = [
            BookLibrary(1,1),
            BookLibrary(1,2),
            BookLibrary(2,3),
            BookLibrary(2,4),
            BookLibrary(3,5),
            BookLibrary(4,6)]

        self.one_to_many = [(b.name, b.num, l.rack)
            for b in self.Books
            for l in self.Lib
            if b.rack_ID == l.ID]

        self.many_to_many_temp = [(l.rack, bl.rack_ID, bl.book_ID)
            for l in self.Lib
            for bl in self.books_lib
            if l.ID == bl.rack_ID]
    
        self.many_to_many = [(b.name, b.num, lib_rack)
            for lib_rack, rack_ID, book_ID in self.many_to_many_temp
            for b in self.Books if b.ID == book_ID]

    def testSortname(self):
        res = sort_name(self.one_to_many)
        res2 = [('Анна Каренина', 4, ' Л. Н. Толстой'), 
        ('Война и Мир', 10, ' Л. Н. Толстой'), 
        ('Горе от ума', 6, 'Пьеса'),
         ('Мертвые души', 3, 'Русская проза'), 
         ('Преступление и наказание', 3, 'Русская проза'), 
         ('Унесенные Ветром', 5, 'Зарубежная проза')]
        self.assertEqual(res,res2)

    def test_book_in_lib(self):
        res = book_in_lib(self.one_to_many, self.Lib)
        res2 = [(' Л. Н. Толстой', 2), ('Русская проза', 2), ('Зарубежная проза', 1), ('Пьеса', 1)]
        self.assertEqual(res,res2)

    def test_run_book(self):
        res = run_book(self.many_to_many, self.Lib)
        res2 = [(' Л. Н. Толстой', 'Война и Мир')]
        self.assertEqual(res,res2)

        

if __name__ == '__main__':
    unittest.main()


