# from azure.cosmos import exceptions, CosmosClient, PartitionKey
# import requests


# # Initialize the Cosmos client
# endpoint = "https://gtto-cosmosdb.documents.azure.com:443/"
# key = 'z0mwYS79v1KOGL97eCVKmWCAwlkh8FkScxSaLBmiUa4opH5s5Kf9Ci7wZGVJQ54IOysl95Q3ESNuPBsapgjYXw=='

# # <create_cosmos_client>
# client = CosmosClient(endpoint, key)
# # </create_cosmos_client>

# # Create a database
# # <create_database_if_not_exists>
# database_name = 'FuncDatabase'
# database = client.create_database_if_not_exists(id=database_name)
# # </create_database_if_not_exists>

# # Create a container
# # Using a good partition key improves the performance of database operations.
# # <create_container_if_not_exists>
# container_name = 'FuncContainer'
# container = database.create_container_if_not_exists(
#     id=container_name, 
#     partition_key=PartitionKey(path="/password"),
#     offer_throughput=400
# )
# # </create_container_if_not_exists>


# # Add items to the container
# item = requests.get('https://gttofuncapp.azurewebsites.net/api/Service1?code=iqOo/yn11VtPwqiGSWwKCIN4Db4naTyyJs8vg1ala5nj3XNZSX0FAA==').text

#  # <create_item>
# container.create_item(body=item)
# # </create_item>

# # Read items (key value lookups by partition key and id, aka point reads)
# # <read_item>
# item_response = container.read_item(item=item['id'], partition_key=item['password'])
# request_charge = container.client_connection.last_response_headers['x-ms-request-charge']
# print('Read item with id {0}. Operation consumed {1} request units'.format(item_response['id'], (request_charge)))
# # </read_item>

# # Query these items using the SQL query syntax. 
# # Specifying the partition key value in the query allows Cosmos DB to retrieve data only from the relevant partitions, which improves performance
# # <query_items>
# query = "SELECT * FROM c ORDER BY c.id"

# items = list(container.query_items(
#     query=query,
#     enable_cross_partition_query=True
# ))

# request_charge = container.client_connection.last_response_headers['x-ms-request-charge']

# print('Query returned {0} items. Operation consumed {1} request units'.format(len(items), request_charge))
# # </query_items>