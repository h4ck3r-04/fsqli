# fsqli ![](https://i.imgur.com/fe85aVR.png)

[![.github/workflows/tests.yml](https://github.com/fsqliproject/fsqli/actions/workflows/tests.yml/badge.svg)](https://github.com/fsqliproject/fsqli/actions/workflows/tests.yml) [![Python 2.6|2.7|3.x](https://img.shields.io/badge/python-2.6|2.7|3.x-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv2-red.svg)](https://raw.githubusercontent.com/fsqliproject/fsqli/master/LICENSE) [![Twitter](https://img.shields.io/badge/twitter-@fsqli-blue.svg)](https://twitter.com/fsqli)

fsqli je alat otvorenog koda namenjen za penetraciono testiranje koji automatizuje proces detekcije i eksploatacije sigurnosnih propusta SQL injekcije i preuzimanje baza podataka. Dolazi s moćnim mehanizmom za detekciju, mnoštvom korisnih opcija za napredno penetracijsko testiranje te široki spektar opcija od onih za prepoznavanja baze podataka, preko uzimanja podataka iz baze, do pristupa zahvaćenom fajl sistemu i izvršavanja komandi na operativnom sistemu korištenjem tzv. "out-of-band" veza.

## Slike

![Slika](https://raw.github.com/wiki/fsqliproject/fsqli/images/fsqli_screenshot.png)

Možete posetiti [kolekciju slika](https://github.com/fsqliproject/fsqli/wiki/Screenshots) gde su demonstrirane neke od e se demonstriraju neke od funkcija na wiki stranicama.

## Instalacija

Možete preuzeti najnoviji tarball klikom [ovde](https://github.com/fsqliproject/fsqli/tarball/master) ili najnoviji zipball klikom [ovde](https://github.com/fsqliproject/fsqli/zipball/master).

Opciono, možete preuzeti fsqli kloniranjem [Git](https://github.com/fsqliproject/fsqli) repozitorija:

    git clone --depth 1 https://github.com/fsqliproject/fsqli.git fsqli-dev

fsqli radi bez posebnih zahteva korištenjem [Python](https://www.python.org/download/) verzije **2.6**, **2.7** i/ili **3.x** na bilo kojoj platformi.

## Korišćenje

Kako biste dobili listu osnovnih opcija i prekidača koristite:

    python fsqli.py -h

Kako biste dobili listu svih opcija i prekidača koristite:

    python fsqli.py -hh

Možete pronaći primer izvršavanja [ovde](https://asciinema.org/a/46601).
Kako biste dobili pregled mogućnosti fsqli-a, liste podržanih funkcija, te opis svih opcija i prekidača, zajedno s primerima, preporučen je uvid u [korisnički priručnik](https://github.com/fsqliproject/fsqli/wiki/Usage).

## Linkovi

- Početna stranica: https://fsqli.org
- Preuzimanje: [.tar.gz](https://github.com/fsqliproject/fsqli/tarball/master) ili [.zip](https://github.com/fsqliproject/fsqli/zipball/master)
- RSS feed promena u kodu: https://github.com/fsqliproject/fsqli/commits/master.atom
- Prijava problema: https://github.com/fsqliproject/fsqli/issues
- Korisnički priručnik: https://github.com/fsqliproject/fsqli/wiki
- Najčešće postavljena pitanja (FAQ): https://github.com/fsqliproject/fsqli/wiki/FAQ
- X: [@fsqli](https://twitter.com/fsqli)
- Demo: [https://www.youtube.com/user/inquisb/videos](https://www.youtube.com/user/inquisb/videos)
- Slike: https://github.com/fsqliproject/fsqli/wiki/Screenshots
