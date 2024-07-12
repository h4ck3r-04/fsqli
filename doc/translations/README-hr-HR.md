# fsqli ![](https://i.imgur.com/fe85aVR.png)

[![.github/workflows/tests.yml](https://github.com/fsqliproject/fsqli/actions/workflows/tests.yml/badge.svg)](https://github.com/fsqliproject/fsqli/actions/workflows/tests.yml) [![Python 2.6|2.7|3.x](https://img.shields.io/badge/python-2.6|2.7|3.x-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv2-red.svg)](https://raw.githubusercontent.com/fsqliproject/fsqli/master/LICENSE) [![Twitter](https://img.shields.io/badge/twitter-@fsqli-blue.svg)](https://twitter.com/fsqli)

fsqli je alat namijenjen za penetracijsko testiranje koji automatizira proces detekcije i eksploatacije sigurnosnih propusta SQL injekcije te preuzimanje poslužitelja baze podataka. Dolazi s moćnim mehanizmom za detekciju, mnoštvom korisnih opcija za napredno penetracijsko testiranje te široki spektar opcija od onih za prepoznavanja baze podataka, preko dohvaćanja podataka iz baze, do pristupa zahvaćenom datotečnom sustavu i izvršavanja komandi na operacijskom sustavu korištenjem tzv. "out-of-band" veza.

## Slike zaslona

![Slika zaslona](https://raw.github.com/wiki/fsqliproject/fsqli/images/fsqli_screenshot.png)

Možete posjetiti [kolekciju slika zaslona](https://github.com/fsqliproject/fsqli/wiki/Screenshots) gdje se demonstriraju neke od značajki na wiki stranicama.

## Instalacija

Možete preuzeti zadnji tarball klikom [ovdje](https://github.com/fsqliproject/fsqli/tarball/master) ili zadnji zipball klikom [ovdje](https://github.com/fsqliproject/fsqli/zipball/master).

Po mogućnosti, možete preuzeti fsqli kloniranjem [Git](https://github.com/fsqliproject/fsqli) repozitorija:

    git clone --depth 1 https://github.com/fsqliproject/fsqli.git fsqli-dev

fsqli radi bez posebnih zahtjeva korištenjem [Python](https://www.python.org/download/) verzije **2.6**, **2.7** i/ili **3.x** na bilo kojoj platformi.

## Korištenje

Kako biste dobili listu osnovnih opcija i prekidača koristite:

    python fsqli.py -h

Kako biste dobili listu svih opcija i prekidača koristite:

    python fsqli.py -hh

Možete pronaći primjer izvršavanja [ovdje](https://asciinema.org/a/46601).
Kako biste dobili pregled mogućnosti fsqli-a, liste podržanih značajki te opis svih opcija i prekidača, zajedno s primjerima, preporučen je uvid u [korisnički priručnik](https://github.com/fsqliproject/fsqli/wiki/Usage).

## Poveznice

- Početna stranica: https://fsqli.org
- Preuzimanje: [.tar.gz](https://github.com/fsqliproject/fsqli/tarball/master) ili [.zip](https://github.com/fsqliproject/fsqli/zipball/master)
- RSS feed promjena u kodu: https://github.com/fsqliproject/fsqli/commits/master.atom
- Prijava problema: https://github.com/fsqliproject/fsqli/issues
- Korisnički priručnik: https://github.com/fsqliproject/fsqli/wiki
- Najčešće postavljena pitanja (FAQ): https://github.com/fsqliproject/fsqli/wiki/FAQ
- X: [@fsqli](https://twitter.com/fsqli)
- Demo: [https://www.youtube.com/user/inquisb/videos](https://www.youtube.com/user/inquisb/videos)
- Slike zaslona: https://github.com/fsqliproject/fsqli/wiki/Screenshots
