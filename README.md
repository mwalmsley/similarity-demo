# similarity-demo
Similarity search demo intended for large-scale (1M+) Zooniverse image datasets, where a subset of images are Zooniverse subjects

## Running

To spin up the client/server on localhost:3000

    cd frontend
    npm run dev

## Design Overview

- `frontend` is a next.js app with both client and server components
    - the server components query our database for similar galaxies
    - the client components show the results as thumbnails
- `builder` is a local script for uploading galaxies (representation vectors, image urls, coordinates) to our database
- The database (Azure CosmosDB NoSQL) has fields with the image urls, and vector indices for the representation vectors and sky coordinates. 
- The images themselves are already hosted on a Google Cloud bucket

## Building this

### Creating the vector store

The vector store is CosmosDB from Azure (hat tip Travis). This is a NoSQL db with recently-added vector database support. It's nice to have both ("integrated vector database") because you can do vector queries and just normal NoSQL queries.

Create the instance using the Azure dashboard (or SDK, I guess). I set it up in serverless mode because I expect very erratic traffic patterns.

Once created, go to the instance settings and active vector database mode. Then create a container (group of tables, I think) with a standard index and at least one vector index. I created a vector index "/pca" and a vector index "/umap".

You can do this with config code but I just used the Azure dashboard. Some background [here](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/how-to-python-vector-index-query).

### Inserting data

I use the CosmosDB Python client to add data. [Quickstart](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/quickstart-python), [reference](https://azuresdkdocs.z19.web.core.windows.net/python/azure-cosmos/latest/index.html).


    # in new python env


CosmosDB Python client doesn't support bulk uploads but it does do async uploads. Example [here](https://stackoverflow.com/questions/73225265/how-to-insert-bulk-data-into-cosmos-db-in-python).


npx create-next-app@latest frontend
typescript, no eslint, no tailwind, yes router, no turbopack

    npm run dev

https://learn.microsoft.com/en-us/javascript/api/overview/azure/cosmos-readme?view=azure-node-latest

npm install @azure/cosmos

TODO use [css modules](https://nextjs.org/learn/dashboard-app/css-styling) or [bulma](https://bulma.io/) to style
