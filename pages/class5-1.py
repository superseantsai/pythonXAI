# def 區域變數與全域變數
length = 5  # 全域變數


def calculate_square_area():
    area = length**2  # length是全域變數, area是區域變數
    # length = length + 1 # 這行會出錯，
    # 因為在函數內部length是區域變數，不能直接修改全域變數
    print("面積是", area)


calculate_square_area()
# print("長度是", area) # 這行會出錯，因為area是區域變數，只能在函數內部使用

length = 5  # 全域變數


def calculate_square_area():
    area = length**2  # length是全域變數, area是區域變數
    print("面積是", area)


length = 10  # 全域變數
calculate_square_area()  # 面積是 100
# 因為要等到函數被呼叫時才會執行，所以area的值是在函數被呼叫時才會被計算


length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area():
    area = length**2  # length是全域變數, area是區域變數


calculate_square_area()
print("面積是", area)  # 面積是 100
# 這時候指令內部的area是區域變數，不會影響到全域變數的值

length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area() -> int:
    area = length**2  # length是全域變數, area是區域變數
    return area


area = calculate_square_area()
print("面積是", area)  # 面積是 25

length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area():
    global area  # 使用global，將area變成全域變數，可以在函數內部修改全域變數的值
    area = length**2  # length是全域變數, area是區域變數


calculate_square_area()
print("面積是", area)  # 面積是 25


def hello(name: str):  # 函數傳入參數都是區域變數
    """
    指令說明區\n
    這是一個打招呼的函數\n
    參數:\n
    name: str - 姓名

    回傳:None

    範例:hello("Alice") # Hello, Alice!
    """
    print(f"Hello, {name}!")
