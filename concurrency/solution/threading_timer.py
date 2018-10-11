import queue
import logging
import threading

work_queue = queue.Queue()


def hello():
    while True:
        cmd = work_queue.get()
        print(cmd)
        work_queue.task_done()


t = threading.Timer(1.0, hello)
t.start()


# Zapełnij kolejkę
for todo in ['ping', 'ls -la', 'echo "hello world"', 'cat /etc/passwd']:
    work_queue.put(todo)

# wait to complete all tasks
print('before join')
t.join(timeout=5.0)
print('afer join')

print('done.')