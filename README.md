# Kindle Highlights Scrappy 📚✨

A Python script that automates the extraction of highlights from Amazon's Kindle Notebook and exports them in structured JSON format. Perfect for those who want to backup their annotations, create a personal knowledge management system, or integrate their Kindle highlights into other applications.

## 🎯 What is this project?

When you read books on Kindle, you can create highlights of important passages. These highlights are saved in Amazon's [Kindle Notebook](https://read.amazon.com/notebook). However, Amazon doesn't offer an easy way to export this data in a structured format.

This project solves that problem! It:
1. Opens Kindle Notebook in the browser (using Selenium)
2. Allows you to log in to your Amazon account
3. Navigates through your books and automatically extracts all highlights
4. Saves highlights in organized and structured JSON files
5. Includes book metadata (title, author, cover, description)

## ✨ Features

- 🔍 Automatic extraction of highlights from Kindle Notebook
- 📄 Export in structured and readable JSON format
- 📍 Support for extracting page numbers or locations
- 📚 Process multiple books in a single session
- 🆔 Automatic generation of unique IDs (UUID) for each book and highlight
- 💾 Automatic saving in organized files in the `/exported` folder
- 🎨 Interactive terminal interface for entering book metadata

## 📋 Requirements

- **Python 3.x** (Python 3.7 or higher recommended)
- **Google Chrome** (browser installed on your system)
- **Amazon Account** with access to Kindle Notebook

### Required Python libraries:
- `selenium` - For browser automation
- `beautifulsoup4` - For parsing and extracting data from HTML
- `lxml` (optional) - Faster HTML parser for BeautifulSoup

## 🚀 Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/vinniciusgomes/kindle-highlights-scrappy.git
cd kindle-highlights-scrappy
```

### Step 2: Install dependencies

```bash
pip install selenium beautifulsoup4
```

**Explanation:** This command installs the required Python libraries:
- `selenium`: Allows you to control the Chrome browser automatically
- `beautifulsoup4`: Allows you to parse and extract information from HTML pages

### Step 3: Verify Chrome installation

The script uses **Selenium Manager** which automatically downloads the ChromeDriver compatible with your Chrome version. You just need to have Google Chrome installed on your system.

To verify if Chrome is installed, run:

```bash
# On macOS
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version

# On Linux
google-chrome --version

# On Windows (PowerShell)
(Get-Item 'C:\Program Files\Google\Chrome\Application\chrome.exe').VersionInfo
```

## 📖 How to use

### Step 1: Run the script

In the terminal, inside the project folder, run:

```bash
python scrappy.py
```

**What happens:** The script will automatically open a Chrome window and navigate to Amazon's Kindle Notebook page.

### Step 2: Log in to your Amazon account

You will see this message in the terminal:
```
Please log in to your Amazon account.
Press Enter after logging in...
```

**What to do:**
1. In the Chrome window that opened, log in with your Amazon credentials
2. Wait until you're completely logged in and can see your books
3. Return to the terminal and press **Enter**

### Step 3: Select a book

You will see this message:
```
Click on the book you want to export highlights from and press Enter to continue...
Press Enter after selecting a book...
```

**What to do:**
1. In the Chrome window, **click on the book** you want to export highlights from
2. Wait for the page to load the highlights
3. Return to the terminal and press **Enter**

### Step 4: Enter book metadata

The terminal will request the following information:

```
Enter the book title: 
```
**Example:** `Show Your Work`

```
Enter the book author:
```
**Example:** `Austin Kleon`

```
Enter the book cover URL:
```
**Example:** `https://m.media-amazon.com/images/I/71234567890.jpg`
**Tip:** You can find the cover URL by right-clicking on the book image in Kindle Notebook and copying the image address.

```
Enter the book description:
```
**Example:** `A practical guide on how to share your creative work and be discovered.`

### Step 5: File generated!

You will see a success message:
```
JSON for the book 'Show Your Work' generated successfully! 
File: exported/show_your_work.json
```

The JSON file will be automatically saved in the `/exported` folder with a name based on the book title.

### Step 6: Export more books (optional)

The script will ask:
```
Do you want to export another book? (Y/n):
```

- Type **Y** or just press **Enter** to export another book
- Type **n** to close the script

**What to do if you choose "Y":**
1. In the Chrome window, click on another book
2. Press **Enter** in the terminal
3. Repeat steps 4 and 5

## 📝 Complete usage example

### Terminal input:
```plaintext
Please log in to your Amazon account.
Press Enter after logging in...
[user logs in and presses Enter]

Click on the book you want to export highlights from and press Enter to continue...
Press Enter after selecting a book...
[user clicks on the book and presses Enter]

Enter the book title: Show Your Work
Enter the book author: Austin Kleon
Enter the book cover URL: https://m.media-amazon.com/images/I/71Q8Zr0XVHL.jpg
Enter the book description: 10 ways to share your creativity and get discovered

JSON for the book 'Show Your Work' generated successfully! 
File: exported/show_your_work.json

Do you want to export another book? (Y/n): n
```

### Generated file (`/exported/show_your_work.json`):
```json
{
  "id": "a3d7f8e2-4b1c-4a5e-9f2d-1c8b3e7a9d4f",
  "book": {
    "name": "Show Your Work",
    "author": "Austin Kleon",
    "cover": "https://m.media-amazon.com/images/I/71Q8Zr0XVHL.jpg",
    "description": "10 ways to share your creativity and get discovered"
  },
  "highlights": [
    {
      "id": "b4e8a9c2-5d3e-4f7a-8c1b-2d9e6f3a7b5c",
      "page": "18",
      "content": "When people like you, they see the best in you. When they don't, they tend to see the worst. It's common sense, really."
    },
    {
      "id": "c5f9b0d3-6e4f-5a8b-9d2c-3e0f7a4c8d6e",
      "location": "245",
      "content": "You don't have to be a genius. You just have to be yourself."
    }
  ]
}
```

## 🗂️ JSON Structure

Each exported file contains:

- **`id`**: Unique identifier (UUID) of the book
- **`book`**: Object with book metadata
  - **`name`**: Book title
  - **`author`**: Author name
  - **`cover`**: Cover image URL
  - **`description`**: Book description or synopsis
- **`highlights`**: Array of highlights
  - **`id`**: Unique identifier (UUID) of the highlight
  - **`page`** or **`location`**: Page number or location in the book
  - **`content`**: Highlight text

## 🛠️ Troubleshooting

### Chrome doesn't open
- Verify that Google Chrome is installed
- Run the script again - Selenium Manager will download ChromeDriver automatically

### Can't log in to Amazon
- Make sure your credentials are correct
- If there's two-factor authentication, complete it in the Chrome window
- Wait until you're completely logged in before pressing Enter

### Highlights are not extracted
- Make sure you clicked on the book and waited for the page to fully load
- Verify that the book actually has saved highlights
- Try clicking on the book again

### Error saving the file
- Check if you have write permissions in the project folder
- The `/exported` folder will be created automatically if it doesn't exist

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/MyFeature`)
3. Commit your changes (`git commit -m 'Add MyFeature'`)
4. Push to the branch (`git push origin feature/MyFeature`)
5. Open a Pull Request

## 📄 License

This project is under the MIT License - see the LICENSE file for more details.

## 🔒 Privacy & Security

**Your Amazon session is completely safe and private:**
- Your Amazon login credentials and session data are **NOT saved** anywhere
- Your session data is **NOT sent** to any external server
- When the script stops, all session data is **automatically cleared** as the Chrome instance is closed
- The script runs entirely on your local machine
- Only the book highlights you choose to export are saved as JSON files in your local `/exported` folder

## ⚠️ Legal Disclaimer

This project is for personal and educational use only. Please respect Amazon's Terms of Service when using this script. Use it only to backup your own highlights.
