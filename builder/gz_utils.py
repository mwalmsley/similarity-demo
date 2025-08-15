import pandas as pd


def load_df():
    vector_loc = '/Users/user/Dropbox (The University of Manchester)/euclid/export/q1_v5/representations_pca_40.parquet'
    vector_df = pd.read_parquet(vector_loc)

    morph_loc = '/Users/user/Dropbox (The University of Manchester)/euclid/export/q1_v5/morphology_catalogue.parquet'

    morph_cols = [
        'id_str',
        'object_id',
        'tile_index',
        'right_ascension',
        'declination',
        'segmentation_area',
        'mag_segmentation',
        'smooth-or-featured_featured-or-disk_fraction',
        'smooth-or-featured_problem_fraction'
    ]
    morph_df = pd.read_parquet(morph_loc, columns=morph_cols)

    df = pd.merge(vector_df, morph_df, on='id_str', how='inner')
    print(len(df))

    df['image_url'] = get_urls(df)

    return df

# seperately uploaded to GCP for streamlit demo
# files have a slightly different id_str convention
def get_urls(df):
    # df['tile_index'] = df['id_str'].apply(lambda x: x.split('_')[2])
    df['tile_index'] = df['tile_index'].astype(str)
    df['adjusted_id_str'] = df['id_str'].apply(lambda x: x.replace('-', 'NEG').replace('Q1_R1_', ''))
    image_urls = f'https://storage.googleapis.com/zootasks_test_us/euclid/q1_v5/cutouts_jpg_gz_arcsinh_vis_y/' + df['tile_index'] + '/' + df['adjusted_id_str'] + '_gz_arcsinh_vis_y.jpg'
    return image_urls
