import argparse
from . import enqueue, worker_start, status

def main():
    parser = argparse.ArgumentParser(description="QueueCTL Command Line Tool")
    subparsers = parser.add_subparsers(dest="command")

    # enqueue command
    enqueue_parser = subparsers.add_parser("enqueue", help="Add job to queue")
    enqueue_parser.add_argument("--command", required=True, help="Command to enqueue")
    enqueue_parser.add_argument("--id", required=True, help="Job ID")

    # worker_start command
    worker_parser = subparsers.add_parser("worker_start", help="Start worker")
    worker_parser.add_argument("--count", type=int, default=1, help="Number of workers")

    # status command
    subparsers.add_parser("status", help="Show queue status")

    args = parser.parse_args()

    if args.command == "enqueue":
        enqueue.main(args)
    elif args.command == "worker_start":
        worker_start.main(args)
    elif args.command == "status":
        status.main()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
