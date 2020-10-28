<a href="http://github.com/enoreyes/EssayBot"><img src="https://raw.githubusercontent.com/enoreyes/EssayBot/master/EssayBot.png" alt="EssayBot"></a>

# EssayBot

> EssayBot is an attempt to outline a system that combines state of the art techniques in the domain of text synthesis (GPT-2) with advanced grammar and style parsers, with the goal of proposing a model for a new highly efficient writing assistant software.

- Warning: This repo is still under development so may not build successfully.

## Installation

### Clone

- Clone this repo to your local machine using `https://github.com/enoreyes/EssayBot`

### Setup

> First make sure you have installed requirements

```shell
$ pip3 install language-check
$ pip3 install -r requirements.txt
```

> now run an example

```shell
$ chmod +x RunMe.sh
$ ./Runme
```

---

## Features
- Utilizes the small (117M Parameter) implementation of OpenAI's GPT-2 to generate text
- Cleans the output and removes duplicate (Still implementing this)
- Parses the output using LanguageTool to find style / grammar errors

## Contributing

> Will update this eventually

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/enoreyes/EssayBot.git`

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/enoreyes/EssayBot/compare/" target="_blank">`https://github.com/enoreyes/EssayBot/compare/`</a>.

---

## FAQ

- **This isn't working on my machine!**
    - No problem! Feel free to shoot me an email and I can provide some more specific instructions.

---

## Support

Reach out to me at one of the following places!

- Website at <a href="http://enoreyes.com" target="_blank">`enoreyes.com`</a>

---

## Credits
Huge creds to TaeHwan Jung(@graykode) for his implementation of GPT-2 as well as LanguageTools and OpenAI.

---

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
