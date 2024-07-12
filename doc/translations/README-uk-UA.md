# fsqli ![](https://i.imgur.com/fe85aVR.png)

[![.github/workflows/tests.yml](https://github.com/fsqliproject/fsqli/actions/workflows/tests.yml/badge.svg)](https://github.com/fsqliproject/fsqli/actions/workflows/tests.yml) [![Python 2.6|2.7|3.x](https://img.shields.io/badge/python-2.6|2.7|3.x-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv2-red.svg)](https://raw.githubusercontent.com/fsqliproject/fsqli/master/LICENSE) [![Twitter](https://img.shields.io/badge/twitter-@fsqli-blue.svg)](https://twitter.com/fsqli)

fsqli - це інструмент для тестування вразливостей з відкритим сирцевим кодом, який автоматизує процес виявлення і використання дефектів SQL-ін'єкцій, а також захоплення серверів баз даних. Він оснащений потужним механізмом виявлення, безліччю приємних функцій для професійного тестувальника вразливостей і широким спектром скриптів, які спрощують роботу з базами даних - від відбитка бази даних до доступу до базової файлової системи та виконання команд в операційній системі через out-of-band з'єднання.

## Скриншоти

![Screenshot](https://raw.github.com/wiki/fsqliproject/fsqli/images/fsqli_screenshot.png)

Ви можете ознайомитися з [колекцією скриншотів](https://github.com/fsqliproject/fsqli/wiki/Screenshots), які демонструють деякі функції в wiki.

## Встановлення

Ви можете завантажити останню версію tarball натиснувши [сюди](https://github.com/fsqliproject/fsqli/tarball/master) або останню версію zipball натиснувши [сюди](https://github.com/fsqliproject/fsqli/zipball/master).

Найкраще завантажити fsqli шляхом клонування [Git](https://github.com/fsqliproject/fsqli) репозиторію:

    git clone --depth 1 https://github.com/fsqliproject/fsqli.git fsqli-dev

fsqli «працює з коробки» з [Python](https://www.python.org/download/) версії **2.6**, **2.7** та **3.x** на будь-якій платформі.

## Використання

Щоб отримати список основних опцій і перемикачів, використовуйте:

    python fsqli.py -h

Щоб отримати список всіх опцій і перемикачів, використовуйте:

    python fsqli.py -hh

Ви можете знайти приклад виконання [тут](https://asciinema.org/a/46601).
Для того, щоб ознайомитися з можливостями fsqli, списком підтримуваних функцій та описом всіх параметрів і перемикачів, а також прикладами, вам рекомендується скористатися [інструкцією користувача](https://github.com/fsqliproject/fsqli/wiki/Usage).

## Посилання

- Основний сайт: https://fsqli.org
- Завантаження: [.tar.gz](https://github.com/fsqliproject/fsqli/tarball/master) або [.zip](https://github.com/fsqliproject/fsqli/zipball/master)
- Канал новин RSS: https://github.com/fsqliproject/fsqli/commits/master.atom
- Відстеження проблем: https://github.com/fsqliproject/fsqli/issues
- Інструкція користувача: https://github.com/fsqliproject/fsqli/wiki
- Поширенні питання (FAQ): https://github.com/fsqliproject/fsqli/wiki/FAQ
- X: [@fsqli](https://twitter.com/fsqli)
- Демо: [https://www.youtube.com/user/inquisb/videos](https://www.youtube.com/user/inquisb/videos)
- Скриншоти: https://github.com/fsqliproject/fsqli/wiki/Screenshots
