import numpy as np
import gz_utils, db_utils


def main():
    # run a test search
    # https://azuresdkdocs.z19.web.core.windows.net/python/azure-cosmos/latest/index.html#public-preview-vector-search
    # https://github.com/Azure/azure-sdk-for-python/blob/azure-cosmos_4.9.0/sdk/cosmos/azure-cosmos/samples/index_management.py#L735

    df = gz_utils.load_df()
    pca_cols = [col for col in df.columns if col.startswith('feat_pca_')]

    container = db_utils.get_container()

    example_row = df.query('segmentation_area > 1500').sample()
    search_vector = example_row[pca_cols].astype(np.float32).values.tolist() # not squeezed
    print('search: ', example_row['image_url'].values[0])

    print(search_vector)
    exit()

    # c acts as the container name
    query = "SELECT TOP 3 c.image_url, c.object_id, VectorDistance(c.pca, [{}]) AS similarity_score " \
            "FROM c " \
            "WHERE c.segmentation_area > 1500 " \
            "ORDER BY VectorDistance(c.pca, [{}])" \
            "".format(search_vector, search_vector, search_vector)

    results = container.query_items(query=query, enable_cross_partition_query=True)
    print('neighbours: ')
    for item in results:
        print(item)

if __name__ == '__main__':

    main()