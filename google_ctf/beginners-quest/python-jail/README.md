# PYTHON-JAIL

## 解題思路

這個program 基本上就是python的interpreter，只差在他會擋掉一些built-in function，像是import、open等，所以我們需要想辦法把這些功能叫出來。

我們可以發現，他沒有處理好 `__builtins__` 的內容，所以如果我們用字串組起來的index的方式去拿，就可以得到open的function

但open後要read時，發現read也是被擋的keyword，於是就不用function，直接用`*`去做unpack

最終payload如下:

```python
print(*__builtins__['o' + 'p' + 'e' + 'n']('flag.txt'))
```
