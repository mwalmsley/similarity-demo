
from tqdm import tqdm

import gz_utils, db_utils
import tmp_secrets # sets up env variables


def main():

    df = gz_utils.load_df()
    df = df.sample(40000, random_state=42)
    
    items = create_items(df)

    container = db_utils.get_container()

    # about 90 seconds per 1k rows
    for item in tqdm(items, total=len(df)):
        container.upsert_item(item)


def make_item(standard_cols, pca_cols, row):
    pca_vector = row[pca_cols].tolist()
    sky_vector = row[['right_ascension', 'declination']].tolist()

    item = {
        'id': row['id_str'],  # id is required for nosql, and is also used as the partition key
        # 'idkey': row['id_str'],  # idkey is the partition key for sharding (simply reused)
        'pca': pca_vector,  # set as a vector store "path" i.e. treat data under this field as a vector
        'sky': sky_vector  # similarly (how elegant). Useful for "find nearest object"
    }

    for col in standard_cols:
        item[col] = row[col]
    return item


def create_items(df):

    pca_cols = [col for col in df.columns if col.startswith('feat_pca_')]
    assert len(pca_cols) == 40

    standard_cols = [
        'image_url',  # obviously required
        'object_id',
        'tile_index',
        'right_ascension',
        'declination',
        'segmentation_area',
        'mag_segmentation',
        'smooth-or-featured_featured-or-disk_fraction',
        'smooth-or-featured_problem_fraction'
    ]

    for _, row in df.iterrows():
        yield make_item(row=row, standard_cols=standard_cols, pca_cols=pca_cols)


if __name__ == '__main__':
    main()
