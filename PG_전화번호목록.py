def solution(phone_book):
    book_sorted = sorted(phone_book)

    for i in range(0, len(book_sorted) - 1):
        if book_sorted[i + 1].startswith(book_sorted[i]):
            return False

    return True


if __name__ == "__main__":
    phone_book = ["123", "456", "789"]
    result = solution(phone_book)
    print(result)
