# HTTP通信の中身

https://qiita.com/Sekky0905/items/dff3d0da059d6f5bfabf

- クライアント => サーバー

Webブラウザで`http://localhost:8080/`などのURLを指定すると,以下の様なメッセージがブラウザからサーバーに送信される.

```
GET /index.html HTTP/1.1 
Host: localhost:8080
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36
Accept: */*
Referer: http://localhost:8080/
Accept-Encoding: gzip, deflate, sdch, br
Accept-Language: ja,en-US;q=0.8,en;q=0.6
```
