import threading


class PLinkRequester(object):
    """Parallel link processor."""
    def __init__(self, numWorkers, workFn, inputQueue, outputQueue):
        self.inputQueue = inputQueue
        self.outputQueue = outputQueue
        self.numWorkers = numWorkers
        self.workFn = workFn
        self.numActiveWorkItems = 0

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
        self.numActiveWorkItems += 1
        self.inputQueue.put(item)

    def get_result(self):
        result = self.outputQueue.get()
        self.numActiveWorkItems -= 1
        return result

    def is_done(self):
        return (self.numActiveWorkItems == 0)
