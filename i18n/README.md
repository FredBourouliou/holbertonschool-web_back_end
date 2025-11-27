# i18n - Internationalization with Flask

This project implements internationalization (i18n) in a Flask application using Flask-Babel. It covers locale detection, translation management, and timezone handling.

## Learning Objectives

- Learn how to parametrize Flask templates to display different languages
- Learn how to infer the correct locale based on URL parameters, user settings, or request headers
- Learn how to localize timestamps

## Requirements

- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
- All files should end with a new line
- Code should use the pycodestyle style (version 2.5)
- The first line of all files should be exactly `#!/usr/bin/env python3`
- All `*.py` files should be executable
- All modules, classes, and functions should have documentation
- All functions and coroutines must be type-annotated

## Installation

```bash
# Install required packages
pip3 install flask flask_babel pytz
```

## Project Structure

```
i18n/
├── README.md
├── babel.cfg
├── messages.pot
├── templates/
│   ├── 0-index.html
│   ├── 1-index.html
│   ├── 2-index.html
│   ├── 3-index.html
│   ├── 4-index.html
│   ├── 5-index.html
│   ├── 6-index.html
│   └── 7-index.html
├── translations/
│   ├── en/
│   │   └── LC_MESSAGES/
│   │       ├── messages.po
│   │       └── messages.mo
│   └── fr/
│       └── LC_MESSAGES/
│           ├── messages.po
│           └── messages.mo
├── 0-app.py
├── 1-app.py
├── 2-app.py
├── 3-app.py
├── 4-app.py
├── 5-app.py
├── 6-app.py
└── 7-app.py
```

## Tasks

### 0. Basic Flask app
**File:** `0-app.py`, `templates/0-index.html`

Basic Flask app with a single `/` route that renders a simple HTML template with "Welcome to Holberton" as page title and "Hello world" as header.

### 1. Basic Babel setup
**File:** `1-app.py`, `templates/1-index.html`

Setup Flask-Babel with a `Config` class containing:
- `LANGUAGES = ["en", "fr"]`
- `BABEL_DEFAULT_LOCALE = "en"`
- `BABEL_DEFAULT_TIMEZONE = "UTC"`

### 2. Get locale from request
**File:** `2-app.py`, `templates/2-index.html`

Implements `get_locale` function using `request.accept_languages` to determine the best match with supported languages.

### 3. Parametrize templates
**File:** `3-app.py`, `babel.cfg`, `templates/3-index.html`, `translations/`

Uses `_()` function to parametrize templates with message IDs:
- `home_title`: "Welcome to Holberton" / "Bienvenue chez Holberton"
- `home_header`: "Hello world!" / "Bonjour monde!"

### 4. Force locale with URL parameter
**File:** `4-app.py`, `templates/4-index.html`

Allows forcing locale via URL parameter: `?locale=fr` or `?locale=en`

### 5. Mock logging in
**File:** `5-app.py`, `templates/5-index.html`

Implements mock user login with `login_as` URL parameter and displays:
- `logged_in_as`: "You are logged in as %(username)s." / "Vous êtes connecté en tant que %(username)s."
- `not_logged_in`: "You are not logged in." / "Vous n'êtes pas connecté."

### 6. Use user locale
**File:** `6-app.py`, `templates/6-index.html`

Locale priority order:
1. Locale from URL parameters
2. Locale from user settings
3. Locale from request header
4. Default locale

### 7. Infer appropriate time zone
**File:** `7-app.py`, `templates/7-index.html`

Timezone selection with priority order:
1. Timezone from URL parameters
2. Timezone from user settings
3. Default to UTC

Validates timezones using `pytz.timezone()`.

## Usage

### Running the application

```bash
# Run any version of the app
python3 7-app.py
```

Then visit `http://127.0.0.1:5000/` in your browser.

### URL Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `locale` | Force a specific language | `?locale=fr` |
| `login_as` | Login as a specific user (1-4) | `?login_as=2` |
| `timezone` | Force a specific timezone | `?timezone=Europe/Paris` |

### Examples

```bash
# Default page (English)
http://127.0.0.1:5000/

# French version
http://127.0.0.1:5000/?locale=fr

# Login as Balou (French user)
http://127.0.0.1:5000/?login_as=1

# Login as Beyonce (English user)
http://127.0.0.1:5000/?login_as=2

# Force timezone
http://127.0.0.1:5000/?timezone=US/Eastern

# Combined parameters
http://127.0.0.1:5000/?login_as=1&locale=en&timezone=Asia/Tokyo
```

## Translation Management

### Extract messages
```bash
pybabel extract -F babel.cfg -o messages.pot .
```

### Initialize a new language
```bash
pybabel init -i messages.pot -d translations -l <language_code>
```

### Update existing translations
```bash
pybabel update -i messages.pot -d translations
```

### Compile translations
```bash
pybabel compile -d translations
```

## Mock Users

| ID | Name | Locale | Timezone |
|----|------|--------|----------|
| 1 | Balou | fr | Europe/Paris |
| 2 | Beyonce | en | US/Central |
| 3 | Spock | kg | Vulcan |
| 4 | Teletubby | None | Europe/London |

## Author

Holberton School Project
