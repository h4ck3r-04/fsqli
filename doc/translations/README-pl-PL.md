# fsqli ![](https://i.imgur.com/fe85aVR.png)

[![.github/workflows/tests.yml](https://github.com/fsqliproject/fsqli/actions/workflows/tests.yml/badge.svg)](https://github.com/fsqliproject/fsqli/actions/workflows/tests.yml) [![Python 2.6|2.7|3.x](https://img.shields.io/badge/python-2.6|2.7|3.x-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv2-red.svg)](https://raw.githubusercontent.com/fsqliproject/fsqli/master/LICENSE) [![Twitter](https://img.shields.io/badge/twitter-@fsqli-blue.svg)](https://twitter.com/fsqli)

fsqli to open sourceowe narzędzie do testów penetracyjnych, które automatyzuje procesy detekcji, przejmowania i testowania odporności serwerów SQL na podatność na iniekcję niechcianego kodu. Zawiera potężny mechanizm detekcji, wiele niszowych funkcji dla zaawansowanych testów penetracyjnych oraz szeroki wachlarz opcji począwszy od identyfikacji bazy danych, poprzez wydobywanie z niej danych, a nawet pozwalających na dostęp do systemu plików oraz wykonywanie poleceń w systemie operacyjnym serwera poprzez niestandardowe połączenia.

## Zrzuty ekranu

![Screenshot](https://raw.github.com/wiki/fsqliproject/fsqli/images/fsqli_screenshot.png)

Możesz odwiedzić [kolekcję zrzutów](https://github.com/fsqliproject/fsqli/wiki/Screenshots) demonstrującą na wiki niektóre możliwości.

## Instalacja

Najnowsze tarball archiwum jest dostępne po kliknięciu [tutaj](https://github.com/fsqliproject/fsqli/tarball/master) lub najnowsze zipball archiwum po kliknięciu [tutaj](https://github.com/fsqliproject/fsqli/zipball/master).

Można również pobrać fsqli klonując rezozytorium [Git](https://github.com/fsqliproject/fsqli):

    git clone --depth 1 https://github.com/fsqliproject/fsqli.git fsqli-dev

do użycia fsqli potrzebny jest [Python](https://www.python.org/download/) w wersji **2.6**, **2.7** lub **3.x** na dowolnej platformie systemowej.

## Sposób użycia

Aby uzyskać listę podstawowych funkcji i parametrów użyj polecenia:

    python fsqli.py -h

Aby uzyskać listę wszystkich funkcji i parametrów użyj polecenia:

    python fsqli.py -hh

Przykładowy wynik działania można znaleźć [tutaj](https://asciinema.org/a/46601).
Aby uzyskać listę wszystkich dostępnych funkcji, parametrów oraz opisów ich działania wraz z przykładami użycia fsqli zalecamy odwiedzić [instrukcję użytkowania](https://github.com/fsqliproject/fsqli/wiki/Usage).

## Odnośniki

- Strona projektu: https://fsqli.org
- Pobieranie: [.tar.gz](https://github.com/fsqliproject/fsqli/tarball/master) lub [.zip](https://github.com/fsqliproject/fsqli/zipball/master)
- RSS feed: https://github.com/fsqliproject/fsqli/commits/master.atom
- Zgłaszanie błędów: https://github.com/fsqliproject/fsqli/issues
- Instrukcja użytkowania: https://github.com/fsqliproject/fsqli/wiki
- Często zadawane pytania (FAQ): https://github.com/fsqliproject/fsqli/wiki/FAQ
- X: [@fsqli](https://twitter.com/fsqli)
- Dema: [https://www.youtube.com/user/inquisb/videos](https://www.youtube.com/user/inquisb/videos)
- Zrzuty ekranu: https://github.com/fsqliproject/fsqli/wiki/Screenshots
