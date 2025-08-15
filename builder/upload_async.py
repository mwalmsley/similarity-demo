# # tried this and it didn't seem faster

# # https://stackoverflow.com/questions/73225265/how-to-insert-bulk-data-into-cosmos-db-in-python


# from azure.cosmos.aio import CosmosClient as async_CosmosClient
# from azure.cosmos import ThroughputProperties, PartitionKey

# # async def upload_async(df, pca_cols, standard_cols):
# #     # async with CosmosClient(os.environ['ACCOUNT_URI'], credential=os.environ['ACCOUNT_KEY']) as client:

# #     # https://github.com/Azure/azure-sdk-for-python/blob/azure-cosmos_4.9.0/sdk/cosmos/azure-cosmos/samples/concurrency_sample.py
# #     async with async_CosmosClient.from_connection_string(os.environ['READ_WRITE_PRIMARY_CONNECTION_STRING']) as client:
# #         throughput_properties = ThroughputProperties(auto_scale_max_throughput=100)
# #         database = await client.create_database_if_not_exists('q1', offer_throughput=throughput_properties)
# #         container = await database.create_container_if_not_exists('zoobot', partition_key=PartitionKey(path='/idkey'))
# #         for _, row in tqdm(df.iterrows(), total=len(df)):
# #             await container.upsert_item(make_item(row=row, standard_cols=standard_cols, pca_cols=pca_cols))


# async def main():

#     await upload_async(df, pca_cols, standard_cols)



# if __name__ == '__main__':
#     import asyncio
#     asyncio.run(main())
