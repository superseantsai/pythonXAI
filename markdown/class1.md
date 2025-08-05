這是你今天學到的 Python 指令內容，我幫你用**國小六年級可以理解的方式**整理如下：

---

## 🧠 一、註解（給人看的，不是給電腦看的）

```python
# 這是單行註解
"""
這是多行註解
"""
```

👉 註解就是寫給「人」看的筆記，電腦不會執行。

---

## 📢 二、印出文字或數字

```python
print("Hello, World!")
```

👉 `print()` 會把你放進去的東西「顯示」在畫面上（終端機）。

---

## 🧩 三、基本資料型態（電腦記得資料的方式）

| 例子            | 型態名稱 | 解釋              |
| --------------- | -------- | ----------------- |
| `1`, `-5`       | `int`    | 整數              |
| `1.0`, `3.14`   | `float`  | 小數              |
| `"apple"`       | `str`    | 文字（字串）      |
| `True`, `False` | `bool`   | 是/不是（布林值） |

```python
print(1)
print(1.234)
print("apple")
print(True)
```

---

## 📦 四、變數（幫資料取名字）

```python
a = 10
print(a)  # 顯示 10

a = "apple"
print(a)  # 顯示 apple
```

👉 把資料放進「盒子」裡，這個盒子取名叫 `a`，以後就可以用 `a` 來叫出內容。

---

## ➕ 五、運算（數學加減乘除）

```python
print(1 + 1)  # 加法
print(2 - 1)  # 減法
print(3 * 2)  # 乘法
print(4 / 2)  # 除法（會有小數）
print(5 // 2)  # 取整數商，結果是 2
print(5 % 2)  # 取餘數，結果是 1
print(2**3)  # 次方，2的3次方=8
```

**計算順序（很像數學）**

1. `()` 先算括號
2. `**` 次方
3. `* / // %`
4. `+ -`

---

## 🧵 六、字串操作（對文字做事情）

```python
print("apple" + " pen")  # 合併變成 apple pen
print("apple " * 3)  # 重複變成 apple apple apple
print(len("apple"))  # 計算長度，結果是 5
```

---

## 🕵️ 七、查看型態（看資料是什麼種類）

```python
print(type(1))        # <class 'int'>
print(type("apple"))  # <class 'str'>
print(type(True))     # <class 'bool'>
```

---

## 🔄 八、型態轉換（改變資料的種類）

```python
print(int(1.0))       # 把小數變整數
print(float(1))       # 把整數變小數
print(str(1))         # 把數字變成文字
print(bool(1.234))    # 變成布林值
print(float("1.234")) # 文字變小數
```

🚫 下面這行會錯誤，因為 `"hello"` 不是數字：

```python
# print(int("hello"))
```

---

## ⌨️ 九、輸入 input（請使用者輸入東西）

```python
a = input("請輸入一些文字: ")
print(a)
print(type(a))  # input()輸入的都是字串
```

### ✏️ 計算輸入的數字 +10：

```python
a = input("請輸入數字：")
print(int(a) + 10)
```

### ✏️ 計算圓面積：

```python
a = int(input("請輸入半徑："))
print(a * a * 3.14)
```

### ✏️ 計算國語平均成績：

```python
a = input("請輸入期中成績")
b = input("請輸入期末成績")
print("國語成績平均為", (int(a) + int(b)) / 2)
```

---

## ✅ 小總結：今天你學會了什麼？

- 怎麼在畫面上顯示東西（print）
- 怎麼讓使用者輸入內容（input）
- 數字、文字、真假（基本資料型態）
- 算數（加減乘除、取餘數、次方）
- 怎麼命名資料（變數）
- 怎麼轉換資料的型態（int、str、float、bool）
- 怎麼對文字做加法、乘法
- 怎麼計算平均、圓面積...

---

如果你需要我幫你做成筆記（圖文版、表格版、PDF）也可以跟我說！
