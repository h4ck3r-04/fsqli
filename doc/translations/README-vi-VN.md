# fsqli ![](https://i.imgur.com/fe85aVR.png)

[![.github/workflows/tests.yml](https://github.com/fsqliproject/fsqli/actions/workflows/tests.yml/badge.svg)](https://github.com/fsqliproject/fsqli/actions/workflows/tests.yml) [![Python 2.6|2.7|3.x](https://img.shields.io/badge/python-2.6|2.7|3.x-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv2-red.svg)](https://raw.githubusercontent.com/fsqliproject/fsqli/master/LICENSE) [![Twitter](https://img.shields.io/badge/twitter-@fsqli-blue.svg)](https://twitter.com/fsqli)

fsqli là một công cụ kiểm tra thâm nhập mã nguồn mở, nhằm tự động hóa quá trình phát hiện, khai thác lỗ hổng tiêm SQL và tiếp quản các máy chủ cơ sở dữ liệu. Nó đi kèm với
một hệ thống phát hiện mạnh mẽ, nhiều tính năng thích hợp cho người kiểm tra thâm nhập (pentester) và một loạt các tùy chọn bao gồm phát hiện cơ sở dữ liệu, truy xuất dữ liệu từ cơ sở dữ liệu, truy cập tệp của hệ thống và thực hiện các lệnh trên hệ điều hành từ xa.

## Ảnh chụp màn hình

![Screenshot](https://raw.github.com/wiki/fsqliproject/fsqli/images/fsqli_screenshot.png)

Bạn có thể truy cập vào [bộ sưu tập ảnh chụp màn hình](https://github.com/fsqliproject/fsqli/wiki/Screenshots), chúng trình bày một số tính năng có thể tìm thấy trong wiki.

## Cài đặt

Bạn có thể tải xuống tập tin nén tar mới nhất bằng cách nhấp vào [đây](https://github.com/fsqliproject/fsqli/tarball/master) hoặc tập tin nén zip mới nhất bằng cách nhấp vào [đây](https://github.com/fsqliproject/fsqli/zipball/master).

Tốt hơn là bạn nên tải xuống fsqli bằng cách clone với [Git](https://github.com/fsqliproject/fsqli):

    git clone --depth 1 https://github.com/fsqliproject/fsqli.git fsqli-dev

fsqli hoạt động hiệu quả với [Python](https://www.python.org/download/) phiên bản **2.6**, **2.7** và **3.x** trên bất kì hệ điều hành nào.

## Sử dụng

Để có được danh sách các tùy chọn cơ bản, hãy sử dụng:

    python fsqli.py -h

Để có được danh sách tất cả các tùy chọn, hãy sử dụng:

    python fsqli.py -hh

Bạn có thể xem video chạy thử [tại đây](https://asciinema.org/a/46601).
Để có cái nhìn tổng quan về các khả năng của fsqli, danh sách các tính năng được hỗ trợ và mô tả về tất cả các tùy chọn, cùng với các ví dụ, bạn nên tham khảo [hướng dẫn sử dụng](https://github.com/fsqliproject/fsqli/wiki/Usage) (Tiếng Anh).

## Liên kết

- Trang chủ: https://fsqli.org
- Tải xuống: [.tar.gz](https://github.com/fsqliproject/fsqli/tarball/master) hoặc [.zip](https://github.com/fsqliproject/fsqli/zipball/master)
- Nguồn cấp dữ liệu RSS về commits: https://github.com/fsqliproject/fsqli/commits/master.atom
- Theo dõi vấn đề: https://github.com/fsqliproject/fsqli/issues
- Hướng dẫn sử dụng: https://github.com/fsqliproject/fsqli/wiki
- Các câu hỏi thường gặp (FAQ): https://github.com/fsqliproject/fsqli/wiki/FAQ
- X: [@fsqli](https://twitter.com/fsqli)
- Demo: [https://www.youtube.com/user/inquisb/videos](https://www.youtube.com/user/inquisb/videos)
- Ảnh chụp màn hình: https://github.com/fsqliproject/fsqli/wiki/Screenshots
