
class CeleryChainMock:
    """
    Mocked implementation of celery chain signature to allow usage on disabled backend.

    See: https://docs.celeryproject.org/en/stable/userguide/canvas.html#important-notes
    """

    def __init__(self, *tasks):
        self.task_queue = list(tasks)
        self.parent = self.task_queue[-1] if len(self.task_queue) else None
        self.errback = None

    def __call__(self):
        for task in self.task_queue:
            try:
                task.apply(throw=True)
            except Exception as e:
                self.errback.apply()
                raise e
        return self

    def on_error(self, errback):
        self.errback = errback
        return self
