def bill(total_price, book_price_list):
    return total_price - sum(book_price_list)

if __name__ == "__main__":
    total_price = int(input())
    book_price_list = []
    
    for _ in range(9):
        book_price = int(input())
        book_price_list.append(book_price)
    
    print(bill(total_price, book_price_list))