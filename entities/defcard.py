import numpy as np

class Card:
    #カードの定義
    def __init__(self):
        #paramの初期化
        self.role = ""
        self.power = ""

    #カードの役職と数字を返す
    @classmethod
    def set_job(cls, x):
        jobs = ["少年","兵士","占い師","乙女","死神","貴族","賢者","精霊","皇帝","英雄　"]
        setted_job = cls()
        setted_job.role = jobs[x-1]
        setted_job.power = x
        return setted_job
