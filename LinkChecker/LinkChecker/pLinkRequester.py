import queue
import threading

class PLinkRequester(object):
    """Parallel link processor."""
    def __init__(self, numWorkers, workFn):
        self.inputQueue = queue.Queue()
        self.outputQueue = queue.Queue()
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
            # item is a Link obj
            statusCode, responseData = self.workFn(item)
            # also return the item so that we can map the
            # result to the link 
            # todo - consider adding these as properties to the
            # Link object itself
            self.outputQueue.put((statusCode, responseData, item))
            self.inputQueue.task_done()

    def add_work(self, item):
        self.inputQueue.put(item)
        
    def get_result(self):
        return self.outputQueue.get()
