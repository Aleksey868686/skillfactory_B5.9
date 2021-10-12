import time

class TimeThis:
    """ Измеряет время работы фукции snooze. Можно запускать как декоратор через @Time_this, а можно через контекстный
    менеджер with. По умолчанию время измеряется через контекстный менеджер, а декоратор закомментирован.

    NUM_RUNS - константа, определяющая колчичество замеров времени работы функции.
    
    Способы запуска:
    1. Через декоратор @Time_this:
    @Time_this
    def snooze():
        time.sleep(1)
    snooze()

    2. Через контекстный менеджер with:
    def snooze():
        time.sleep(1)
    with Time_this(snooze):
        snooze()
    """

    def __init__(self, func):
        self.func = func
    def __enter__(self):
        return self
    def __call__(self, *args, **kwargs):
        avg_time = 0
        NUM_RUNS = 5
        for _ in range(NUM_RUNS):
            t1 = time.time()
            self.func()
            t2 = time.time()
        avg_time /= NUM_RUNS
        print(f"Время исполнения функции {self.func} составило: {t2-t1} сек.")   
    def __exit__(self,*args, **kwargs):
        avg_time = 0
        NUM_RUNS = 5
        for _ in range(NUM_RUNS):
            t1 = time.time()
            self.func()
            t2 = time.time()
        avg_time /= NUM_RUNS
        print(f"Время исполнения функции {self.func} составило: {t2-t1} сек.")

# @Time_this
def snooze():
    time.sleep(1)
#snooze()

with TimeThis(snooze):
    snooze()

