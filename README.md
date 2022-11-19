# Passive RTT Measurement Application for ORF2022

## 使い方
- docker-compose.yml を編集しましょう
    - シェルで `ip -br l` と実行し，ミラートラフィックを受信しているインターフェイスの名前を調べる
    - `entrypoint` と書かれている部分を編集する
        - `entrypoint: /passive_rtt [interface name] [ipv4 addr range(DHCP)] [CNS' ipv6 addr range(RA)]`
        - `[interface_name]`: さっき調べたインターフェイスの名前を書く
        - `[ipv4 addr range(DHCP)]`: CNS/Starlin/5G のそれぞれから配られる IPv4 アドレスのレンジを書く
        - `[ipv6 addr range(RA)]`: IPv4 同様，それぞれの RA から配られる IPv6 アドレスのレンジを書く
            - --Starlink は IPv6 対応してないかも？ → 対応していない場合は適当なアドレスを書いておいてください．とにかくなにか書かれていないと起動しません--
            - Starlink にも 5G にも無いらしいので適当に書いておいてください

- 起動しましょう
    - `docker-compose.yml` と同じディレクトリで `docker compose up` を実行
```
Attaching to test_starlink_1, test_cns_1
starlink_1  | [2022-11-13T11:34:40Z INFO  passive_rtt] [192.168.0.28] -> [192.168.0.64], time=136.529ms
cns_1       | [2022-11-13T11:34:48Z INFO  passive_rtt] [192.168.0.28] -> [203.178.139.57], time=11.169568ms
```
こんな感じになっていれば OK

- 停止しましょう
    - `Ctrl+C` を押下するとシェルに戻ります(一度でだめなら連打！)
    - `docker compose down` を実行
    - しばらくすると消えます
    - 停止後はまた `docker compose up` を実行すれば起動します

- より見やすい起動方法
    - `docker-compose.yml` と同じディレクトリで `docker compose up -d` を実行
        - `-d` をつけるとバックグラウンドで実行されるため，コマンドが終了したように見えます
    - ターミナルアプリを 2 つ起動し，ウィンドウを左右に並べる
        - tmux とかでももちろん OK
    - 両方のウィンドウで `docker-compose.yml` と同じディレクトリに移動
    - 左右でそれぞれ `docker-compose logs -f cns`，`docker-compose logs -f starlink` を実行
    - 出力が左右で分かれるので見やすくなります
- webgui 作りました
    - と言ってもグラフを出すだけです
    - ブラウザで localhost:8888 にアクセスし，view.html を開いてください
    - 何回か計測して数分放置すると CDF のグラフが出ます
    - 1, 2 分に一度グラフは更新されます
        - ブラウザ開きっぱなしで大丈夫です．自動更新されます．
## なんか動きません
- インターフェイス名，IP アドレスのレンジは間違えていませんか？
    - 間違っているとプログラムは異常終了し，Docker がそれを再起動，また異常終了... を繰り返します
    - `停止しましょう` を見て止めて書き直してまた上げてください

- よくわからないけど動きません
    - とりあえず何も考えずにコンテナを再起動しましょう
    - 頑張ってみてみてもわからなかったら先輩に助けを求めましょう！
