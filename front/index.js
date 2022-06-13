let res = []
serverUrl = 'http://127.0.0.1:8000/books/'
const allBooks = async () => {
    res = await fetch(serverUrl)
        .then(response => response.json())
    buildGUI()
}

const buildGUI = () => {
    document.getElementById('root').innerHTML = res.map(b => `<p>${b.Book_Name}&nbsp;&nbsp;<button onclick="deleteBook(${b.BookID})">Delete</button></p>`).join('')
}

const addBook = async () => {
    await fetch(serverUrl, {
        method: 'POST',
        body: JSON.stringify({
            Book_Name: bookName.value,
            Book_Author: bookAuthor.value
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
        },
    })
        .then((response) => response.json())
    allBooks()
}

const deleteBook = (id) => {
    fetch(`${serverUrl}${id}`, {
        method: 'DELETE',
    });
    allBooks()
};
