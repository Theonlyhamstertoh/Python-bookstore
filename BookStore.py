import Book
import ArrayList
# import ArrayQueue
# import RandomQueue
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
# import AdjacencyList
import MaxQueue
import time

class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''

    def __init__(self):
        self.bookCatalog = ArrayList.ArrayList()        
        # self.bookIndices = ChainedHashTable.ChainedHashTable()
        # self.shoppingCart = ArrayQueue.ArrayQueue()
        self.shoppingCart =MaxQueue.MaxQueue()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()

    def loadCatalog(self, fileName: str):
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
     
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                # self.bookIndices.add(key, self.bookCatalog.size() - 1)
                self.sortedTitleIndices.add(title, self.bookCatalog.size() - 1)
            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def removeFromCatalog(self, i: int):
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i: int):
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            # print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def searchBookByInfix(self, infix: str, cnt: int):
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
            cnt: integer
        '''
        start_time = time.time()
        # todo

        catalog = ArrayList.ArrayList()

        # print all until 15 total counts, not 15 steps
        catalog = ArrayList.ArrayList()
        for book in self.bookCatalog:
            if infix in book.title:
                catalog.append(book)
            if catalog.size() == 15:
                break
        
        for book in catalog:
            print(book)



        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self):
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")
    
    def get_cart_best_seller(self):
        start_time = time.time()
        self.shoppingCart
        print('getCartBestSeller returned')
        print(self.shoppingCart.max().title)
        elapsed_time = time.time() - start_time
        print(f"Completed in {elapsed_time} seconds")

        return self.shoppingCart.max().title

    def addBookByKey(self, key):
        # print("RAN ADDBOOKBYKEY FUNCTION")
        start_time = time.time()
        bookIndex = self.bookIndices.find(key)
        if bookIndex is not None:
            book= self.bookCatalog.get(bookIndex)
            # print("shopping cart", self.shoppingCart.tail)
            self.shoppingCart.add(book) 
            elapsed_time = time.time() - start_time
            print(f"Added title: {self.shoppingCart.tail.x.title}")
        print('Book not found.')
        print(f"addBookByKey Completed in {elapsed_time} seconds")

    def addBookByPrefix(self, prefix):
        n = len(prefix)
        if n == 0: return;
        
        book = self.sortedTitleIndices.find_nearest_node(prefix)
        booktitle = book.k.lower()[0:n].replace(" ", "")
        prefixTitle = prefix.lower().replace(' ', '')
        print(booktitle, prefixTitle)
        if booktitle == prefixTitle :
            self.addBookByIndex(book.v)
            print(book.k)
            # print(f'Added first matched title: {book.k}')
            return book.k
        else:
            print('Book not found.')
            return None
    
    def bestsellers_with(self, infix, structure, n =0 ):
        best_sellers = None
        if structure == 1:
            best_sellers = BinarySearchTree.BinarySearchTree()
        elif structure == 2:
            best_sellers = BinaryHeap.BinaryHeap()
        else:
            print("Invalid data structure.")
            
        if best_sellers is not None:
            if infix == "":
                print("Invalid infix.")
            else:
                start_time = time.time()
                # FIXME: Insert the rest of the implementation here
                
                infixTitle = infix.lower().replace(" ", "")
                for book in self.bookCatalog:
                    bookTitle = book.title.lower().replace(' ', '')
                    if infixTitle in bookTitle:
                        if structure == 1:
                            best_sellers.add(book.rank, book)
                        elif structure == 2:
                            best_sellers.add_node(book.rank * -1, book)
                        
                        if n == 0:
                            continue;
                        if best_sellers.size() >= n:
                            break;
                
                if structure == 1:
                    for x in best_sellers.in_order()[::-1]:
                        print(x.v)
                elif structure == 2:
                    for i in range(best_sellers.n):
                        print(best_sellers.remove_node().v)
                elapsed_time = time.time() - start_time
                print(f"Displayed bestsellers_with({infix}, {structure}, {n}) in {elapsed_time} seconds")
        
                
    
# print( "WorldofPo" in "DuboseHeyward:ACharlestonGentlemanandtheWorldofPorgyandBess")
# title = "realestatehomeinspection:masteringtheprofession"
# infix = "worldofpo"
# print(infix in title == True)
# bookStore = BookStore()
# bookStore.loadCatalog("books.txt")
# bookStore.bestsellers_with('World of po', 1)

# (bookStore.addBookByPrefix("The Struggitt"))
# (bookStore.addBookByPrefix("America"))
# (bookStore.addBookByPrefix("The"))
# (bookStore.addBookByPrefix("My"))
# print(bookStore.shoppingCart.max().title)
# # bookstore.addBookByIndex(5838)    
# bookstore.addBookByIndex(15501)    
# bookstore.addBookByIndex(23295)    
# bookstore.addBookByIndex(13015)    
# bookstore.addBookByIndex(16701)
# bookstore.get_cart_best_seller()
        

