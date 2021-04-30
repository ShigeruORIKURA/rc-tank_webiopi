# rc-tank_webiopi
webブラウザから操作できるRC戦車のwebiopi設定値を記載します。

# 環境構築方法
TODO:

# ディレクトリ構成
各ファイルは、以下に記載するRaspberry Piのディレクトリに配置して下さい。

### "/home/pi"ディレクトリ

"/home/pi"ディレクトリには、以下のファイルを配置して下さい。

```
/home/pi

|-- camera.sh
`-- moter.py
```

### "/usr/share/webiopi/htdocs"ディレクトリ

"/usr/share/webiopi/htdocs"ディレクトリには、以下のファイルを配置して下さい。

```
/usr/share/webiopi/htdocs

|-- index.html   // ★元からあるファイルに上書きしてしまって大丈夫です。
`-- images
    |-- default_image.jpg
    |-- loading_animation.gif
    |-- loading_image.jpg
    |-- shutdown_image_001.jpg
    `-- shutdown_image_002.jpg
```

### "/etc/webiopi/"ディレクトリ

"/etc/webiopi/"ディレクトリには、以下のファイルを配置して下さい。

```
/etc/webiopi/

`-- config
```

# 参考URL

https://shigeru-orikura.com/category/%e3%82%ab%e3%83%a1%e3%83%a9%e4%bb%98%e3%81%8d%e3%83%a9%e3%82%b8%e3%82%b3%e3%83%b3%e5%8c%96%e8%a8%88%e7%94%bb/