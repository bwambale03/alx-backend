# i18n Translation Project

This repository contains an internationalization (i18n) setup for a Flask project using Babel.

## Directory Structure

- **translations/**
  - **fr/LC_MESSAGES/**: French translations containing `messages.po` and `messages.mo` files.
  - **en/LC_MESSAGES/**: English translations containing `messages.po` and `messages.mo` files.

## Files

- **babel.cfg**: Configuration file for Babel, specifying translation instructions.
- **app.py**: Flask application file for handling the i18n setup.
- **templates/**: HTML templates for rendering web pages.

## How to Use

1. Navigate to the `translations/` directory.
2. Modify `.po` files for your desired language.
3. Compile the `.po` files into `.mo` using Babel.
4. Run the Flask app with `python app.py`.

## Requirements

- Flask
- Babel

