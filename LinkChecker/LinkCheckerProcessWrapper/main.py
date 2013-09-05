from azure.storage import QueueService
import azureStorageCreds

# connect to queue
queue_service = QueueService(azureStorageCreds.STORAGE_ACCOUNT, azureStorageCreds.STORAGE_ACCOUNT_KEY)
queue_service.create_queue('testqueue')

# in a loop
    # get work
    # run work
    # write result to queue

input('Press Enter to exit')