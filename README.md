# Retro Adventure Game

A text-based adventure game with a retro computer aesthetic, built with Django.

## Features

- Classic text-based adventure gameplay
- Retro CRT monitor visual style
- PostgreSQL database for game state persistence
- Session-based game progress tracking
- Multiple branching paths and choices

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL database
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/James-Hendershott/retro_adventure_game.git
cd retro_adventure_game
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Set up your `.env` file with database credentials:
```
DB_NAME=retro_adventure
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your-secret-key-here
DEBUG=True
```

6. Create the PostgreSQL database:
```bash
createdb retro_adventure
```

7. Run migrations:
```bash
python manage.py migrate
```

8. Create a superuser (optional, for admin access):
```bash
python manage.py createsuperuser
```

9. Run the development server:
```bash
python manage.py runserver
```

10. Open your browser and navigate to `http://localhost:8000`

## Project Structure

```
retro_adventure_game/
├── game/                      # Main game app
│   ├── migrations/           # Database migrations
│   ├── static/game/          # Static files (CSS, images)
│   ├── templates/game/       # HTML templates
│   ├── admin.py             # Django admin configuration
│   ├── apps.py              # App configuration
│   ├── models.py            # Database models
│   ├── tests.py             # Unit tests
│   ├── urls.py              # URL routing
│   └── views.py             # Game logic and views
├── retro_adventure_game/     # Project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Root URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (not in repo)
└── README.md               # This file
```

## Running Tests

```bash
python manage.py test
```

## Development

To contribute to this project:

1. Create a new branch for your feature
2. Make your changes
3. Write tests for new functionality
4. Run tests to ensure everything works
5. Submit a pull request

## License

This project is open source and available under the MIT License.
