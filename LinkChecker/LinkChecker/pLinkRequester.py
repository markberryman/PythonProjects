import queue
import threading


class PLinkRequester(object):
    """Parallel link processor."""
    def __init__(self, numWorkers, workFn, inputQueue, outputQueue):
        self.inputQueue = inputQueue
        self.outputQueue = outputQueue
        self.numWorkers = numWorkers
        self.workFn = workFn

    def start(self):
        for i in range(self.numWorkers):
            t = threading.Thread(target=self.worker)
            t.daemon = True
            t.start()

    def worker(self):
        while True:
            item = self.inputQueue.get()
            self.workFn(item)
            self.outputQueue.put(item)
            self.inputQueue.task_done()

    def add_work(self, item):
        self.inputQueue.put(item)

    def get_result(self):
        return self.outputQueue.get()
