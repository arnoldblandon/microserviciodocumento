from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings
from azure.storage.blob import PublicAccess

# Conexión  al almacenamiento de
block_blob_service = BlockBlobService(account_name='pruebamesfix', account_key='ihJKFJV1lswpHZlRn6UYvXJqp2EIPnuNbqsSEeSgrb+IZU8/CqmC6MCvi8XykEa+Old+q59dQzziKpLnCfpnvA==')
#si no hay blob lo crea
block_blob_service.create_container('mycontainer')
#tipo de accecibilidad al blob creado
block_blob_service.create_container('mycontainer', public_access=PublicAccess.Container)
