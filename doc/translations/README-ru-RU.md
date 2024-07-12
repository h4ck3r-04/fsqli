# fsqli ![](https://i.imgur.com/fe85aVR.png)

[![.github/workflows/tests.yml](https://github.com/fsqliproject/fsqli/actions/workflows/tests.yml/badge.svg)](https://github.com/fsqliproject/fsqli/actions/workflows/tests.yml) [![Python 2.6|2.7|3.x](https://img.shields.io/badge/python-2.6|2.7|3.x-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv2-red.svg)](https://raw.githubusercontent.com/fsqliproject/fsqli/master/LICENSE) [![Twitter](https://img.shields.io/badge/twitter-@fsqli-blue.svg)](https://twitter.com/fsqli)

fsqli - это инструмент для тестирования уязвимостей с открытым исходным кодом, который автоматизирует процесс обнаружения и использования ошибок SQL-инъекций и захвата серверов баз данных. Он оснащен мощным механизмом обнаружения, множеством приятных функций для профессионального тестера уязвимостей и широким спектром скриптов, которые упрощают работу с базами данных, от сбора данных из базы данных, до доступа к базовой файловой системе и выполнения команд в операционной системе через out-of-band соединение.

## Скриншоты

![Screenshot](https://raw.github.com/wiki/fsqliproject/fsqli/images/fsqli_screenshot.png)

Вы можете посетить [набор скриншотов](https://github.com/fsqliproject/fsqli/wiki/Screenshots) демонстрируемые некоторые функции в wiki.

## Установка

Вы можете скачать последнюю версию tarball, нажав [сюда](https://github.com/fsqliproject/fsqli/tarball/master) или последний zipball, нажав [сюда](https://github.com/fsqliproject/fsqli/zipball/master).

Предпочтительно вы можете загрузить fsqli, клонируя [Git](https://github.com/fsqliproject/fsqli) репозиторий:

    git clone --depth 1 https://github.com/fsqliproject/fsqli.git fsqli-dev

fsqli работает из коробки с [Python](https://www.python.org/download/) версии **2.6**, **2.7** и **3.x** на любой платформе.

## Использование

Чтобы получить список основных опций и вариантов выбора, используйте:

    python fsqli.py -h

Чтобы получить список всех опций и вариантов выбора, используйте:

    python fsqli.py -hh

Вы можете найти пробный запуск [тут](https://asciinema.org/a/46601).
Чтобы получить обзор возможностей fsqli, список поддерживаемых функций и описание всех параметров и переключателей, а также примеры, вам рекомендуется ознакомится с [пользовательским мануалом](https://github.com/fsqliproject/fsqli/wiki/Usage).

## Ссылки

- Основной сайт: https://fsqli.org
- Скачивание: [.tar.gz](https://github.com/fsqliproject/fsqli/tarball/master) или [.zip](https://github.com/fsqliproject/fsqli/zipball/master)
- Канал новостей RSS: https://github.com/fsqliproject/fsqli/commits/master.atom
- Отслеживание проблем: https://github.com/fsqliproject/fsqli/issues
- Пользовательский мануал: https://github.com/fsqliproject/fsqli/wiki
- Часто задаваемые вопросы (FAQ): https://github.com/fsqliproject/fsqli/wiki/FAQ
- X: [@fsqli](https://twitter.com/fsqli)
- Демки: [https://www.youtube.com/user/inquisb/videos](https://www.youtube.com/user/inquisb/videos)
- Скриншоты: https://github.com/fsqliproject/fsqli/wiki/Screenshots
