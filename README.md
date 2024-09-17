# Kindle highlights extractor

This script extracts highlights from a Kindle-generated HTML file and outputs them as a JSON file. It uses BeautifulSoup to parse the HTML and extract relevant data.

## Features

- Extracts highlights from Kindle HTML files
- Outputs highlights in JSON format
- Supports extracting location and content of highlights

## Requirements

- Python 3.x
- `beautifulsoup4`
- `lxml` or `html.parser` (BeautifulSoup parser)
- `re` (regular expression module, included in Python standard library)

## Installation

You can install the required Python packages using pip:

```bash
pip install beautifulsoup4
```

## Usage
1. **Prepare your Kindle HTML file:** Ensure you have a Kindle-generated HTML file with highlights. 

2. **Run the script:** Execute the script using Python. It will prompt you for the path to the HTML file and book details.
```bash
python script.py
```

3. **Provide details:** When prompted, provide the following details:
- Path to the Kindle HTML file
- Book name
- Book author
- URL of the book cover (optional)
- Book description

4. **Check the output:** The script will generate a JSON file named `result.json` containing the extracted highlights and book details.

## Example
```plaintext
Please enter the path to the HTML file: /path/to/highlights.html
Please enter the name of the book: Example Book
Please enter the author of the book: Example Author
Please enter the URL of the book cover: http://example.com/cover.jpg
Please enter a description of the book: This is an example book.
```

Output in `result.json`:
```json
{
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
