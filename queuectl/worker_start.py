import time

def main(args):
    for i in range(args.count):
        print(f"👷 Worker {i+1} started and waiting for jobs...")
        time.sleep(1)
