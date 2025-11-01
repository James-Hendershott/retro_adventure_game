
# Retro Adventure Game

A web-based, retro-styled adventure game built with Django. The game interface mimics a 1980s CRT monitor on a cluttered desk, and gameplay is session-based with PostgreSQL for future scalability.

## Features
- CRT monitor UI with green-on-black text
- Interactive adventure scenes and choices
- Session-based progress tracking (no login required)
- Scene logic in Python dictionary (easy to migrate to DB)
- PostgreSQL-ready (via .env)
- Modern Django project structure

## How to Use
1. **Clone this repo and open in VS Code**
2. **Create a Python virtual environment and activate it**
3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
4. **Set up PostgreSQL and create a `.env` file** (see below)
5. **Run migrations:**
   ```
   python manage.py migrate
   ```
6. **Start the server:**
   ```
   python manage.py runserver
   ```
7. **Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to play!**

## .env Example
```
DB_NAME=retro_adventure
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

## Project Structure
```
retro_adventure_game/
├── game/
│   ├── templates/game/index.html
│   ├── static/game/css/style.css
│   ├── views.py
│   ├── scenes.py
├── retro_project/
│   ├── settings.py
│   ├── urls.py
├── requirements.txt
├── .env
├── README.md
```

## Future Ideas & Improvements
- Move scene logic from Python dictionary to Django models (database-driven)
- Add player name and outcome tracking
- Save and display past adventures
- Add sound effects and retro CRT scanline animation
- Add more scenes, puzzles, and branching logic
- User-selectable themes (amber, green, white CRT)
- Mobile-friendly UI improvements
- Docker support for easy deployment
- Admin interface for editing scenes

## Credits
- Inspired by Monty Python, The Princess Bride, and classic 1980s adventure games.
