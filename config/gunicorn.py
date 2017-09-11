import multiprocessing

bind = "127.0.0.1:13070"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'egg:meinheld#gunicorn_worker'
