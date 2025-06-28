import math

class Paginator:
    def __init__(self, data, page_size):
        self.data = data                
        self.page_size = page_size       # page size
        self.total_pages = math.ceil(len(data) / page_size)  # calculate summ pages
        self.current_page = 0            # current page (began from 0)

    def __iter__(self):
        return self  

    def __next__(self):
        if self.current_page >= self.total_pages:
            raise StopIteration  # if pages end i mean last pages , its means iteration end

        start = self.current_page * self.page_size  # start indeks current page
        end = start + self.page_size               # last indeks
        page_data = self.data[start:end]           

        self.current_page += 1  # move next page

        return {
            "page": self.current_page,     # Current page 
            "page_max": self.total_pages,  # how mane pages?qty
            "data": page_data              # Current page data
        }
#testing
data1 = [1,2,3,4,5,6,7,8,9]
data2 = [1,2,3,4,5,6,7,8,9,10,11]
pager1 = Paginator(data1, 3)
pager2 = Paginator(data2, 4)
print(f'Book :{data1}')
for page in pager1:
    print(page)
print("")
print(f'Book :{data2}')
for page in pager2:
    print(page)
