# fsqli ![](https://i.imgur.com/fe85aVR.png)

[![.github/workflows/tests.yml](https://github.com/fsqliproject/fsqli/actions/workflows/tests.yml/badge.svg)](https://github.com/fsqliproject/fsqli/actions/workflows/tests.yml) [![Python 2.6|2.7|3.x](https://img.shields.io/badge/python-2.6|2.7|3.x-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv2-red.svg)](https://raw.githubusercontent.com/fsqliproject/fsqli/master/LICENSE) [![Twitter](https://img.shields.io/badge/twitter-@fsqli-blue.svg)](https://twitter.com/fsqli)

fsqli e инструмент за тестване и проникване, с отворен код, който автоматизира процеса на откриване и използване на недостатъците на SQL база данните чрез SQL инжекция, която ги взима от сървъра. Снабден е с мощен детектор, множество специални функции за най-добрия тестер и широк спектър от функции, които могат да се използват за множество цели - извличане на данни от базата данни, достъп до основната файлова система и изпълняване на команди на операционната система.

## Демо снимки

![Снимка на екрана](https://raw.github.com/wiki/fsqliproject/fsqli/images/fsqli_screenshot.png)

Можете да посетите [колекцията от снимки на екрана](https://github.com/fsqliproject/fsqli/wiki/Screenshots), показващи някои функции, качени на wiki.

## Инсталиране

Може да изтеглине най-новите tar архиви като кликнете [тук](https://github.com/fsqliproject/fsqli/tarball/master) или най-новите zip архиви като кликнете [тук](https://github.com/fsqliproject/fsqli/zipball/master).

За предпочитане е да изтеглите fsqli като клонирате [Git](https://github.com/fsqliproject/fsqli) хранилището:

    git clone --depth 1 https://github.com/fsqliproject/fsqli.git fsqli-dev

fsqli работи самостоятелно с [Python](https://www.python.org/download/) версия **2.6**, **2.7** и **3.x** на всички платформи.

## Използване

За да получите списък с основните опции използвайте:

    python fsqli.py -h

За да получите списък с всички опции използвайте:

    python fsqli.py -hh

Може да намерите пример за използване на fsqli [тук](https://asciinema.org/a/46601).
За да разберете възможностите на fsqli, списък на поддържаните функции и описание на всички опции, заедно с примери, се препоръчва да се разгледа [упътването](https://github.com/fsqliproject/fsqli/wiki/Usage).

## Връзки

- Начална страница: https://fsqli.org
- Изтегляне: [.tar.gz](https://github.com/fsqliproject/fsqli/tarball/master) or [.zip](https://github.com/fsqliproject/fsqli/zipball/master)
- RSS емисия: https://github.com/fsqliproject/fsqli/commits/master.atom
- Проследяване на проблеми и въпроси: https://github.com/fsqliproject/fsqli/issues
- Упътване: https://github.com/fsqliproject/fsqli/wiki
- Често задавани въпроси (FAQ): https://github.com/fsqliproject/fsqli/wiki/FAQ
- X: [@fsqli](https://twitter.com/fsqli)
- Демо: [https://www.youtube.com/user/inquisb/videos](https://www.youtube.com/user/inquisb/videos)
- Снимки на екрана: https://github.com/fsqliproject/fsqli/wiki/Screenshots
