import queue
import logging
import threading

work_queue = queue.Queue()


class Worker(threading.Thread):
    daemon = True

    def run(self):
        while True:
            # Remove and return an item from the queue.
            job = work_queue.get()

            # Execute work
            logging.warning('Will do the work: %s' % job)

            # Indicate that a formerly enqueued task is complete.
            work_queue.task_done()


def spawn_worker(how_many):
    for i in range(how_many):
        Worker().start()


if __name__ == '__main__':
    spawn_worker(3)

    # Zapełnij kolejkę
    for todo in ['ping', 'ls -la', 'echo "hello world"', 'cat /etc/passwd']:
        work_queue.put(todo)

    # wait to complete all tasks
    work_queue.join()
