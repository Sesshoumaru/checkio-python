在一个给定的8*8的棋盘上中（横向用字母a至h表示，纵向用数字1到8表示），旗子在棋盘中只能按左下或者右下的方式行走，如果某一个棋子的位置可以由其他棋子一步到达，则认为该棋子安全。

我们在棋盘上有几个白色的棋子，只有白色的棋子。你应该设计你的代码来找到几个棋子是安全的。

**输入：** 旗子组合成的位置坐标集合

**输出：** 安全的旗子的数量

**例子：**

```python

safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

```

**如果使用：** For a game AI one of the important tasks is the ability to estimate game state. This concept will show how you can do this on the simple chess figures positions.