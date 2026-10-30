class Python_notbook:
    def __init__(self):
        self.page_number1=''
        self.page_number5=''
        self.page_number8=''
    def chapter_info(self):
        print("page_number1:-",self.page_number1)
        print("page_number5:-", self.page_number5)
        print("page_number8:-", self.page_number8)

p=Python_notbook()
p.page_number1="loops"
p.page_number5="ifelsh"
p.page_number8="oop"
p.chapter_info()