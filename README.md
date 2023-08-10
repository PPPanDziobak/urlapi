### English:

## Simple API Project

This project provides a simple Django API that offers URL shortening and reverting functionality.

### Setup

1. Ensure you have Python 3.10 installed.


2. Install project dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

### How to Use

This project offers two main endpoints:

1. **Shorten URL:**
   - Endpoint: `http://127.0.0.1:8003/change/`
   - Method: POST
   - Input: Provide the `input_url` in the JSON request to obtain a shortened version of the link.

2. **Revert URL:**
   - Endpoint: `http://127.0.0.1:8003/revert/`
   - Method: POST
   - Input: Provide the `output_url` in the JSON request to revert the link to its original form.

### Making API Requests

You can use tools like Postman to make API requests:

1. **Shorten URL:**
   - Method: POST
   - URL: `http://127.0.0.1:8003/change/`
   - Body (JSON): `{"input_url": "your_long_url_here"}`

2. **Revert URL:**
   - Method: POST
   - URL: `http://127.0.0.1:8003/revert/`
   - Body (JSON): `{"output_url": "your_shortened_url_here"}`

### Polish:

## Projekt prostego API

Ten projekt dostarcza proste API w Django, oferujące funkcje skracania i przywracania linków.

### Konfiguracja

1. Upewnij się, że masz zainstalowany Python 3.10.

2. Zainstaluj zależności projektu za pomocą pip:
   ```
   pip install -r requirements.txt
   ```

### Jak korzystać

Ten projekt udostępnia dwa główne endpointy:

1. **Skracanie URL:**
   - Endpoint: `http://127.0.0.1:8003/change/`
   - Metoda: POST
   - Wejście: Podaj `input_url` w żądaniu JSON, aby otrzymać skróconą wersję linka.

2. **Przywracanie URL:**
   - Endpoint: `http://127.0.0.1:8003/revert/`
   - Metoda: POST
   - Wejście: Podaj `output_url` w żądaniu JSON, aby przywrócić link do jego pierwotnej wersji.

### Wywoływanie żądań API

Możesz użyć narzędzi takich jak Postman, aby wywoływać żądania API:

1. **Skracanie URL:**
   - Metoda: POST
   - URL: `http://127.0.0.1:8003/change/`
   - Body (JSON): `{"input_url": "twój_długi_url_tutaj"}`

2. **Przywracanie URL:**
   - Metoda: POST
   - URL: `http://127.0.0.1:8003/revert/`
   - Body (JSON): `{"output_url": "twój_skrócony_url_tutaj"}`