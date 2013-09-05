from azure.storage import QueueService
import azureStorageCreds
import time

inputQueueName = "inputqueue"
outputQueueName = "outputqueue"

queue_service = QueueService(azureStorageCreds.STORAGE_ACCOUNT, azureStorageCreds.STORAGE_ACCOUNT_KEY)
queue_service.create_queue(inputQueueName)

# format: <depth>:<start link>
testMessage = "1:http://www.foo.com"

queue_service.put_message(inputQueueName, testMessage)

while True:
    messages = queue_service.get_messages(inputQueueName)

    # we get one message by default
    if (len(messages.queue_messages) == 1):
        # todo - do work
        queue_service.delete_message(inputQueueName, messages[0].message_id, messages[0].pop_receipt)
        # todo - write result to queue
    else:
        print("No work. Sleeping for a bit...")
        time.sleep(2)

input('Press Enter to exit')