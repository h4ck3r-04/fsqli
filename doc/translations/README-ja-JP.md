# fsqli ![](https://i.imgur.com/fe85aVR.png)

[![.github/workflows/tests.yml](https://github.com/fsqliproject/fsqli/actions/workflows/tests.yml/badge.svg)](https://github.com/fsqliproject/fsqli/actions/workflows/tests.yml) [![Python 2.6|2.7|3.x](https://img.shields.io/badge/python-2.6|2.7|3.x-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv2-red.svg)](https://raw.githubusercontent.com/fsqliproject/fsqli/master/LICENSE) [![Twitter](https://img.shields.io/badge/twitter-@fsqli-blue.svg)](https://twitter.com/fsqli)

fsqli はオープンソースのペネトレーションテスティングツールです。SQL インジェクションの脆弱性の検出、活用、そしてデータベースサーバ奪取のプロセスを自動化します。
強力な検出エンジン、ペネトレーションテスターのための多くのニッチ機能、持続的なデータベースのフィンガープリンティングから、データベースのデータ取得やアウトオブバンド接続を介したオペレーティング・システム上でのコマンド実行、ファイルシステムへのアクセスなどの広範囲に及ぶスイッチを提供します。

## スクリーンショット

![Screenshot](https://raw.github.com/wiki/fsqliproject/fsqli/images/fsqli_screenshot.png)

wiki に載っているいくつかの機能のデモをスクリーンショットで見ることができます。 [スクリーンショット集](https://github.com/fsqliproject/fsqli/wiki/Screenshots)

## インストール

最新の tarball を [こちら](https://github.com/fsqliproject/fsqli/tarball/master) から、最新の zipball を [こちら](https://github.com/fsqliproject/fsqli/zipball/master) からダウンロードできます。

[Git](https://github.com/fsqliproject/fsqli) レポジトリをクローンして、fsqli をダウンロードすることも可能です。:

    git clone --depth 1 https://github.com/fsqliproject/fsqli.git fsqli-dev

fsqli は、 [Python](https://www.python.org/download/) バージョン **2.6**, **2.7** または **3.x** がインストールされていれば、全てのプラットフォームですぐに使用できます。

## 使用方法

基本的なオプションとスイッチの使用方法をリストで取得するには:

    python fsqli.py -h

全てのオプションとスイッチの使用方法をリストで取得するには:

    python fsqli.py -hh

実行例を [こちら](https://asciinema.org/a/46601) で見ることができます。
fsqli の概要、機能の一覧、全てのオプションやスイッチの使用方法を例とともに、 [ユーザーマニュアル](https://github.com/fsqliproject/fsqli/wiki/Usage) で確認することができます。

## リンク

- ホームページ: https://fsqli.org
- ダウンロード: [.tar.gz](https://github.com/fsqliproject/fsqli/tarball/master) or [.zip](https://github.com/fsqliproject/fsqli/zipball/master)
- コミットの RSS フィード: https://github.com/fsqliproject/fsqli/commits/master.atom
- 課題管理: https://github.com/fsqliproject/fsqli/issues
- ユーザーマニュアル: https://github.com/fsqliproject/fsqli/wiki
- よくある質問 (FAQ): https://github.com/fsqliproject/fsqli/wiki/FAQ
- X: [@fsqli](https://twitter.com/fsqli)
- デモ: [https://www.youtube.com/user/inquisb/videos](https://www.youtube.com/user/inquisb/videos)
- スクリーンショット: https://github.com/fsqliproject/fsqli/wiki/Screenshots
