from queue import Queue
import uuid

def generate_request(request_string: str, request_queue: Queue):
    request = {uuid.uuid4().hex: request_string}
    request_queue.put(request)

def process_request(request_queue: Queue):
    if request_queue.empty():
        print(f"Request queue is empty")
        return

    request = request_queue.get()
    print(f"Request processed: {request}")

def main():
    request_queue = Queue()

    print("Type your request")
    try:
        while True:
            request_string = input('>> ')

            if request_string in ['exit', 'close']:
                print('Good bye!')
                break

            if request_string != '':
                generate_request(request_string, request_queue)

            process_request(request_queue)

    except KeyboardInterrupt:
        print('Good bye!')

if __name__ == '__main__':
    main()