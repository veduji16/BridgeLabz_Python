import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()

    def end(self):
        self.end_time = time.time()

    def elapsed_time(self):
        if self.start_time is None or self.end_time is None:
            return None
        return self.end_time - self.start_time

stopwatch = Stopwatch()

input("Press Enter to start the stopwatch...")
stopwatch.start()

input("Press Enter to stop the stopwatch...")
stopwatch.end()

elapsed = stopwatch.elapsed_time()
if elapsed is not None:
    print(f"Elapsed time: {elapsed:.2f} seconds")
else:
    print("Error: Please start and end the stopwatch correctly.")