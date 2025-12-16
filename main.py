# 在这里编写代码
class Book:
    """书籍类，包含书名、作者、ISBN等属性，以及可借状态"""
    def __init__(self, title, author, isbn):
        self.title = title  # 书名
        self.author = author  # 作者
        self.isbn = isbn  # ISBN编号
        self.is_available = True  # 是否可借，默认可借

    def check_availability(self):
        """检查书籍是否可借"""
        return self.is_available

    def borrow_book(self):
        """借出书籍，修改可借状态"""
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self):
        """归还书籍，恢复可借状态"""
        self.is_available = True
        return True


class User:
    """用户类，包含姓名、借书卡号，以及借阅书籍列表"""
    def __init__(self, name, card_id):
        self.name = name  # 姓名
        self.card_id = card_id  # 借书卡号
        self.borrowed_books = []  # 已借书籍列表

    def borrow(self, book):
        """用户借书功能"""
        if book.check_availability():
            book.borrow_book()
            self.borrowed_books.append(book)
            print(f"{self.name}成功借阅《{book.title}》")
        else:
            print(f"《{book.title}》已被借出，无法借阅")

    def return_book(self, book):
        """用户还书功能"""
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name}成功归还《{book.title}》")
        else:
            print(f"{self.name}未借阅《{book.title}》，无法归还")


# 测试代码
if __name__ == "__main__":
    # 创建书籍实例
    book1 = Book("Python编程：从入门到实践", "埃里克·马瑟斯", "9787115428028")
    book2 = Book("数据结构与算法分析", "马克·艾伦·维斯", "9787115546926")

    # 创建用户实例
    user1 = User("张三", "C001")
    user2 = User("李四", "C002")

    # 测试借书功能
    user1.borrow(book1)
    user2.borrow(book1)  # 尝试借阅已被借出的书

    # 测试还书功能
    user1.return_book(book1)
    user2.borrow(book1)  # 归还后再次借阅

    # 测试检查可借状态
    print(f"《{book2.title}》是否可借：{book2.check_availability()}")
