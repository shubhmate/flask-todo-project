# Flask To-Do Project

A simple Flask-based web application for creating and managing to-do items with MongoDB as the backend database.

## Features

- ✅ Create new to-do items with name and description
- ✅ Generate unique UUIDs for each item
- ✅ Store items in MongoDB database
- ✅ Simple and intuitive web interface
- ✅ RESTful API endpoints for data retrieval

## Tech Stack

- **Backend**: Python with Flask
- **Database**: MongoDB
- **Frontend**: HTML
- **API**: JSON/REST

## Project Structure

```
flask-todo-project/
├── app.py                 # Main Flask application
├── templates/
│   └── todo.html         # To-do creation form template
├── data.json             # Sample data/configuration
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies (recommended)
```

## Installation

### Prerequisites

- Python 3.7 or higher
- MongoDB (local or cloud instance like MongoDB Atlas)
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/shubhmate/flask-todo-project.git
   cd flask-todo-project
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask pymongo
   ```

4. **Configure MongoDB connection**
   - Update the MongoDB connection string in `app.py`:
   ```python
   client = MongoClient("your-mongodb-uri")
   ```
   - For local MongoDB: `MongoClient("mongodb://localhost:27017")`
   - For MongoDB Atlas: `MongoClient("mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority")`

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   - Navigate to `http://localhost:5000/`

## Usage

### Creating a To-Do Item

1. Open the application in your browser
2. Fill in the following fields:
   - **Item Name**: The title of your to-do item
   - **Item Description**: Detailed description of the task
   - **Item ID** (Optional): Custom identifier for the item
3. Click the **"Generate ID"** button to auto-generate a UUID
4. Click **"Submit"** to save the item to the database

### API Endpoints

- **GET** `/` - Displays the to-do form
- **GET** `/api` - Returns data from `data.json` as JSON
- **POST** `/submit_todoitem` - Submits a new to-do item

## Example Request

```bash
curl -X POST http://localhost:5000/submit_todoitem \
  -d "item_name=Buy Groceries&item_description=Milk, Bread, Eggs"
```

## Database Schema

Items are stored in MongoDB with the following structure:

```json
{
  "_id": ObjectId,
  "item_name": "string",
  "item_description": "string"
}
```

## Configuration

### Environment Variables (Recommended)

Create a `.env` file in the project root:

```
MONGODB_URI=mongodb://localhost:27017
FLASK_ENV=development
FLASK_DEBUG=True
```

Then update `app.py` to use environment variables:

```python
import os
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv('MONGODB_URI'))
```

## Future Improvements

- [ ] Add form validation on the client side
- [ ] Implement UUID generation in JavaScript
- [ ] Add item hash generation functionality
- [ ] Implement item update/delete functionality
- [ ] Add CSS styling for better UI/UX
- [ ] Add user authentication
- [ ] Display list of all to-do items
- [ ] Add test cases

## Troubleshooting

### MongoDB Connection Error

- Ensure MongoDB is running locally or check your connection string
- Verify network access if using MongoDB Atlas
- Check firewall/proxy settings

### Form Submission Issues

- Ensure all required fields are filled
- Check browser console for JavaScript errors
- Verify Flask debug mode is enabled for detailed error messages

### Port Already in Use

If port 5000 is already in use:

```python
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Use a different port
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for bugs and feature requests.

## License

This project is open source and available under the MIT License.

## Author

**shubhmate**

---

## Getting Help

For issues or questions:
1. Check the troubleshooting section above
2. Review the code comments in `app.py`
3. Open an issue on GitHub

---

**Note**: This is a Git and GitHub Assignment project from Tutedude.
