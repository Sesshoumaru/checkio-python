斯蒂芬和索菲亚对于一切都使用简单的密码，忘记了安全性。请你帮助尼古拉开发一个密码安全检查模块。如果密码的长度大于或等于10个符号，至少有一个数字，一个大写字母和一个小写字母，该密码将被视为足够强大。密码只包含ASCII拉丁字母或数字。

**输入:** 密码 (str, unicode)。

**输出:** 密码的安全与否，作为布尔值(bool)，或者任何可以转换和处理为布尔值的数据类型。你会在结果看到转换后的结果(True 或 False)。

**范例:**

```python

checkio('A1213pokl') == False
checkio('bAse730onE') == True
checkio('asasasasasasasaas') == False
checkio('QWERTYqwerty') == False
checkio('123456123456') == False
checkio('QwErTy911poqqqq') == True

```

**如何使用:** 如果你担心你的应用或服务的安全性，您可以检查用户密码的复杂性。你可以使用这些技巧要求你的用户的密码符合多个条件（标点符号或unicode）。

**前提:**
```
re.match("[a-zA-Z0-9]+", password)
0 < len(password) ≤ 64
```