from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings
from azure.storage.blob import PublicAccess

block_blob_service = BlockBlobService(account_name='pruebamesfix', account_key='ihJKFJV1lswpHZlRn6UYvXJqp2EIPnuNbqsSEeSgrb+IZU8/CqmC6MCvi8XykEa+Old+q59dQzziKpLnCfpnvA==')
block_blob_service.create_container('mycontainer')
block_blob_service.create_container('mycontainer', public_access=PublicAccess.Container)
