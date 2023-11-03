## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.8+
- Pip for Python 3

### Installing

A step-by-step series of examples that tell you how to get a development environment running:

Navigate to the cloned directory:

```bash
cd ll_model
```

### Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Run the Flask application (running on your local machine):

```bash
flask run
```

### Using the API

To use the API, you can make a POST request to the `/predict` endpoint with JSON data containing the text to be analyzed. Example using curl:

```bash
curl -X POST https://level-lens-15580084405a.herokuapp.com/predict -H "Content-Type: application/json" -d '{"text":"Your sample text here."}'
```

### Deployment

The API is deployed on Heroku and is available at [https://level-lens-15580084405a.herokuapp.com/](https://level-lens-15580084405a.herokuapp.com/).
