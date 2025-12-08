import time

class Logger:
    @staticmethod
    def log_event(event: str):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        message = f"--[{current_time}]: {event}"
        print(message)
        try:
            with open('logs.txt', 'a')as f:
                f.write(message + '\n')
        except Exception as e:
            print(f"--[{current_time}]: Failed to save logs - {e}")
