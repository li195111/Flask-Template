import threading
from main import app

if __name__ == "__main__":
    import os
    import sys
    import threading
    import multiprocessing
    # Execute redis-server
    redis = threading.Thread(target=os.system,args=('redis-server',)) 
    redis.start()
    
    celery_schedule = multiprocessing.Process(target=os.system, args=('celery -A tasks.task beat',))
    celery_schedule.start()

    app.run(host='0.0.0.0', port=3000, debug=True, load_dotenv=True)
    
    redis.join()
    celery_schedule.join()
