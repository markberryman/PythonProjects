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
            workRequest = self.inputQueue.get()
            self.workFn(workRequest)
            self.outputQueue.put(workRequest)
            self.inputQueue.task_done()
            self.numActiveWorkItems -= 1

    def add_work(self, link):
        if (link is None):
            raise TypeError("item can not be None.")

        self.numActiveWorkItems += 1
        self.inputQueue.put(link)

    def get_results(self):
        while (self.numActiveWorkItems != 0):
            pass

        results = []

        # all work has been processed
        while (self.outputQueue.empty() is False):
            results.append(self.outputQueue.get())

        return results

    def is_done(self):
        return (self.numActiveWorkItems == 0)
