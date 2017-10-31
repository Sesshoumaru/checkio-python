我们假设我们的猴子正在打字，打字和打字，并且生成了各种各样的短文本段。 我们试着检查它们是否含有合理的单词。

我们会给出单词列表，您应该计算给定文本中包含了单词列表中含有的多少个单词。 单词可以是文本中的一个单词，也可能是文本中另一个单词的一部分。 文字大小写无关紧要。 给定的单词列表都是小写的，不重复。 如果一个单词在文本中出现多次，那么它应该只算一次。例如，文本 - “How aresjfhdskfhskd you?”，单词 - （"how", "are", "you", "hello"）。 结果将是3。

**输入:** 两个参数，1个是文本，1个是单词列表.

**输出:** 文本中包含指定单词列表的单词个数

**范例:**

```python

count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3
count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2
count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",{"sum", "hamlet", "infinity", "anything"}) == 1

```

