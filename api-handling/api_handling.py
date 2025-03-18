import requests

def api_request_handling():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    api_response = requests.get(url)
    json_data = api_response.json()

    if json_data["success"] and "data" in json_data:
        book_details = json_data["data"]
        book_name = book_details["volumeInfo"]["title"]
        book_author = book_details["volumeInfo"]["authors"][0]
        book_description = book_details["volumeInfo"]["description"]
        return book_name,book_author,book_description
    else:
        raise Exception("Failed to access the API!")


def main():
    try:
        book_name, book_author, book_description = api_request_handling() 
        print("Book Name : ",book_name)
        print("Author : ",book_author)
        print("Description : ",book_description)
    except Exception:
        print(str(Exception))


if __name__ == "__main__":
    main()
