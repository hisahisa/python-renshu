
class MyClass:
    def set_value(self, text):  # クラス内の value 変数に値を代入するメソッド
        self.value = text

    def print_value(self):      # 変数 value の値を表示するメソッド
        print(self.value)

if __name__ == "__main__":
    a = MyClass()               # MyClass のインスタンスを生成
    a.set_value("abc")          # 変数 value に文字列 "abc" を代入
    a.print_value()             # abc
