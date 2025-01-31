class NameColumns:
    def __init__(self, name, index):
        self.name = name
        self.index = index + 2

    def __str__(self):
        str1 = "姓名：" + self.name + "，行号：" + str(self.index)
        if hasattr(self, 'score'):
            str1 += "，成绩：" + str(self.score)
        return str1
    def add_score(self, score):
        self.score = score