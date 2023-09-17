# Algorie

Algorie is a web application that generates hints for coding problems based on a description and user's current code. It uses Python Flask for the backend and the OpenAI API for generating hints.
</br></br>


## Table of Contents

- [Prerequisites]
- [Python Package Installation]
- [API Key]
- [How to Start]
- [Contributing]
</br></br>


## Prerequisites

Before you run the Algorie Scratch application, please make sure that you have all of the following prerequisites installed:

- Python. (3.6 or higher)
- Python packages. (OpenAI and Flask)
- OpenAI API key.


## Python and Packages Installation

1.  Download Python from https://www.python.org/downloads/ <br/>
(If you already have Python, then you can skip this step.)

2. Install libraries
```
pip3 install openai
```
```
pip3 install flask
```
> Copy and paste it into your terminal.


## API Key

1. log into https://openai.com/blog/introducing-chatgpt-and-whisper-apis

2. Go to user settings

3. Get a secret API key

4. Open `algorie.py` <br/>
`api_key = "Enter your secret API key"` <br/>
Change it to your unique key!


## How to Start

1. `cd` to directory where have `alogire.py` and `templates`

2. `python3 algorie.py`

3. Open any web browser and type `http://127.0.0.1:5000` in URL

4. Enjoy!


## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature
```
git checkout -b feature
```
3. Implement your feature or fix.
4. Commit your changes
```
git commit -m "Your message"
```
5. Push to the branch
```
git push origin feature
```
6. Submit a pull request.
