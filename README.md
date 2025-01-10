# Phishing Simulation Tool

A Flask-based web application that simulates phishing email campaigns and tracks user interactions. This tool is designed for educational purposes to help organizations understand the risks associated with phishing attacks.

## Features

- Send phishing emails to test user awareness.
- Track whether users clicked on the phishing links.
- Generate reports of user interactions.
- Modern, responsive interface built with Bootstrap.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **Flask-SQLAlchemy**: An extension that adds SQLAlchemy support to Flask applications.
- **Bootstrap**: A front-end framework for developing responsive websites.
- **SQLite**: A lightweight database for storing user interaction data.

## Installation

1. Clone the repository:
git clone https://github.com/yourusername/phishing-simulation-tool.git

2. Create a virtual environment:
python -m venv venv


3. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source venv/bin/activate
  ```

4. Install the required packages:
   pip install -r requirements.txt
   
5. Run the application:
   python app.py


6. Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

- Visit the home page to send phishing emails.
- Click on the links in the emails to simulate user interaction.
- View reports of user interactions in the report section.

## Contributing

We welcome contributions! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [Flask](https://flask.palletsprojects.com/) for providing a great framework.
- Thanks to [Bootstrap](https://getbootstrap.com/) for their responsive design components.
