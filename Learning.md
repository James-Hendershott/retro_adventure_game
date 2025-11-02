# Learning.md: Retro Adventure Game in Django

## What is This Project?
This project is a step-by-step conversion of a Python terminal adventure game into a modern Django web app, styled to look like a 1980s CRT monitor. It is designed for learning Django, web development, and best practices in project structure and documentation.

## Why This Approach?
- **Django**: Robust, scalable, and widely used for Python web apps.
- **Session-based**: No login needed; state is tracked per user session.
- **PostgreSQL**: Industry-standard database, ready for future expansion.
- **Retro UI**: Fun, engaging, and a great CSS/HTML learning opportunity.
- **Stepwise Refactoring**: Start with a Python dictionary for scenes, then migrate to models for scalability.

## Key Learning Steps
1. **Project Setup**: Organize code with Django’s app/project structure. Use virtual environments and requirements.txt for dependencies.
2. **Environment Variables**: Use a `.env` file for DB credentials, keeping secrets out of code.
3. **Database Integration**: Configure Django to use PostgreSQL, even if not used immediately.
4. **Static & Template Files**: Learn Django’s static and template system for CSS, images, and HTML.
5. **Session Management**: Use Django sessions to track game progress without user accounts.
6. **Game Logic Refactor**: Move from procedural code to a scene dictionary, then to Django models.
7. **Retro Styling**: Use CSS to mimic CRT monitors and 1980s desk setups.
8. **Documentation**: Maintain clear README and Learning.md files for future reference and onboarding.

## Next Steps
- Expand the scene dictionary to cover the full adventure.
- Refactor scenes/choices into Django models for DB-driven gameplay.
- Add outcome tracking, player name, and more advanced features.

---

**This file will be updated as you learn and build!**
