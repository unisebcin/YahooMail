# YahooMail

This program aims to show usage of Yahoo SMTP server. Two options provided for sending email:
- Send text message
- Send email with attachment

Username and Yahoo SMTP One-Time Password is required!!

Please insert One-Time Password as environment variable SMTP_PASSWORD

[![Python application](https://github.com/unisebcin/YahooMail/actions/workflows/python-app.yml/badge.svg)](https://github.com/unisebcin/YahooMail/actions/workflows/python-app.yml)

## Dependencies

Dependencies are managed by [potery](https://python-poetry.org/)

[Install poetry](https://python-poetry.org/docs/#installation) before moving forward.

Use Poetry to install required dependencies:
```console
poetry install --no-root
```

If you need to use new dependencies (eg. requests), use poetry:
```console
poetry add requests
```

To start the service call the following command:
```console
poetry run python app/main.py
```
