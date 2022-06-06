# [Cliweather](https://absozero.github.io/cliweather):cloud:
> The weather app that is free and open source, can use multiple providers, and runs in the command line and a web interface..

![GitHub Repo stars](https://img.shields.io/github/stars/absozero/cliweather?logo=github&style=flat-square)
![Lines of code](https://img.shields.io/tokei/lines/github/absozero/cliweather?style=flat-square)
![GitHub all releases](https://img.shields.io/github/downloads/absozero/cliweather/total?style=flat-square)

Having to check a website for your weather could be sucky, depending on your mood. To check multiple, to cross reference and get accurate weather, even worse. To solve this problem, :sparkle:cliweather was made. :sparkle:
For the geeks out there, you can view the weather just from the cli, and for selfhosters, you can host a web ui of the app, and see it in a browser, all locally, except the calls to external weather api's. For people who just want to see the weather, both of these options are easy to get set up with. No tracking and open source.


## Installation
First [install the python interpreter](https://docs.python.org/3/using/index.html)(*required*)
1. Clone the repository
```bash
gh repo clone absozero/cliweather
or
git clone https://github.com/absozero/cliweather.git
```
2. Get into the folder by using `cd cliweather`
3. Then, create a virtual environment(Basically, it isolates packages from the rest of the system) by using
```
python3 -m venv venv
or
python -m venv venv
```
4. Then initialize the environment with the scripts given in the venv/Scripts or the venv/bin folder. You may have to use `. venv/bin/activate` on mac and linux
5.  You can use pipenv, which is recommended for the project, or you could also use the requirements.txt given. It can be used with this:
```bash
pipenv:
pipenv install
pip:
pip install -r requirements.txt
```
Then, you run the actual program, inside your virtual environment.
`python(3) main.py`

## Changelog/Roadmap

 - [ ] Make a web ui
 - [ ] Figuring out packaging formats
 - [ ] Setup multiple api's
 - [ ] Make a tui
 - [ ] Get a working prototype going :smile:

## Contact

Absozero - https://github.com/absozero

Distributed under the MIT license. 

[https://github.com/absozero/cliweather](https://github.com/dbader/)

Docs - https://absozero.github.io/cliweather

## Contributing
Please do contribute to the project, either by making a pull request or by making a github issue.

To make a pull request:
1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->

[Docs](https://absozero.github.io/cliweather)
