# clue

A Slack developer bot assistant.

## Configuration

It's strongly recommanded to use this app with the virtual environment.  
Follow those commands to initialize venv:  

**On windows**  

```bat
python -m venv venv
venv\Scripts\activate
```

**On Linux**  

```bash
python3 -m virtualenv venv
venv/bin/activate
```

Once your venv is activate, you must upgrade PyPi:  

**On windows**  

```bat
venv\Scripts\python -m pip install --upgrade pip
```

**On Linux**  

```bash
venv/bin/python3 -m pip3 install --upgrade pip3
```

Now, install all required dependencies:  

**On windows**  

```bat
venv\Scripts\pip install -r requirements.txt
```

**On Linux**  

```bash
venv/bin/pip3 install -r requirements.txt
```

Then, you have to unlock your `config` file:  

```sh
mv config.yml.lock config.yml
```

Next, replace your `bot api key` to the `api.slack.token` key in the *config.yml* file.  

The application is now setted up !

## Running

Run the bot with the following command:  

**On Windows:**  

```bat
venv\Scripts\python main.py
```

**On Linux:**  

```sh
venv/bin/python3 main.py
```