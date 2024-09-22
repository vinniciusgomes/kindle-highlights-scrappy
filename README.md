# Kindle Highlights Extractor

This script extracts highlights from the Kindle Notebook web application and outputs them as a JSON file. It uses Selenium to navigate the web application and BeautifulSoup to parse the HTML and extract relevant data.

## Features

- Extracts highlights from the Kindle Notebook web application
- Outputs highlights in JSON format
- Supports extracting location or page number and content of highlights
- User-friendly input for book details (title, author, cover URL, and description)

## Requirements

- Python 3.x
- `selenium`
- `beautifulsoup4`
- `lxml` or `html.parser` (BeautifulSoup parser)
- `re` (regular expression module, included in Python standard library)

## Installation

You can install the required Python packages using pip:

```bash
pip install selenium beautifulsoup4
```

Additionally, make sure to download the appropriate ChromeDriver for your version of Chrome and place it in a directory accessible by your PATH.

## Usage

1. **Login to Kindle Notebook:** Open your browser and log in to the Kindle Notebook web application at [read.amazon.com/notebook](https://read.amazon.com/notebook).

2. **Run the script:** Execute the script using Python. It will prompt you to select a book and provide details.
```bash
  python scrappy.py
```

3. **Select a book:** Click on the book you wish to export highlights from and then press Enter in the terminal.

4. **Provide details:** When prompted, enter the following details:
- Book title
- Book author
- URL of the book cover (optional)
- Book description

5. **Check the output:** The script will generate a JSON file in the `/exported` folder containing the extracted highlights and book details.

## Example
```plaintext
Click on the book you wish to export the highlights from and press Enter to continue...
Press Enter after selecting a book...
Please enter the title of the book: Example Book
Please enter the author of the book: Example Author
Please enter the URL of the book cover: http://example.com/cover.jpg
Please enter a description of the book: This is an example book.
```

Output in `/exported/example_book.json`:
```json
{
  "id": "some-uuid",
  "book": {
    "name": "Example Book",
    "author": "Example Author",
    "cover": "http://example.com/cover.jpg",
    "description": "This is an example book."
  },
  "highlights": [
    {
      "location": "136",
      "content": "Passionate about solving common problems."
    }
  ]
}
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.
