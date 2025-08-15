import { CosmosClient, Container, ContainerResponse } from "@azure/cosmos";  // useful for typing as well


async function getContainer(): Promise<Container> {
  const endpoint = process.env.ACCOUNT_URI;
  const key = process.env.ACCOUNT_KEY;
  const client = new CosmosClient({ endpoint, key });
  const database = (await client.databases.createIfNotExists({ id: "q1" })).database
  const container = (await database.containers.createIfNotExists({ id: "zoobot" })).container;  // containerresponse.container
  return container;

}

// function getSimilar(container) {
    
//     const resources = [
//         {
//             'id_str': 12,
//             'SimilarityScore': 0.9
//         }
//     ]
//     return resources;
// }

async function getSimilar(container: Container): Promise<Array<SearchResult>> {

    const search_vector = [4.738552093505859, 7.470155239105225, -6.015420436859131, -0.7379969358444214, 1.8239898681640625, 0.7689674496650696, 2.935908079147339, -1.619835376739502, -2.958463668823242, 1.4655219316482544, -3.4920461177825928, 0.7281328439712524, -5.327934741973877, -0.9259732365608215, -0.2614843249320984, -0.3087991774082184, -0.7487781643867493, -2.0624632835388184, 1.6211451292037964, -1.688948631286621, 0.007734626065939665, 0.056243669241666794, 1.174306869506836, -0.18829312920570374, -0.24228033423423767, 1.0672425031661987, 0.30462613701820374, -0.1868823766708374, -0.4348199665546417, 0.4641546308994293, -0.20532585680484772, 0.6645591259002686, 0.6272052526473999, -0.5078186392784119, -0.5312449932098389, -0.1756150722503662, -0.418759822845459, -0.14622414112091064, 0.28305113315582275, 0.15616346895694733]

    const { resources } = await container.items
    .query({
        query: "SELECT TOP 3 c.id, c.right_ascension, c.declination, c.image_url FROM c ORDER BY VectorDistance(c.pca, @embedding)",
        parameters: [{ name: "@embedding", value: search_vector }]
    })
    .fetchAll();

    return resources;

}

async function getNearby(container: Container, ra:number, dec:number): Promise<Array<SearchResult>> {
    const { resources } = await container.items
    .query({
        query: "SELECT TOP 1 c.id, c.right_ascension, c.declination, c.image_url FROM c ORDER BY VectorDistance(c.sky, @embedding)",
        parameters: [{ name: "@embedding", value: [ra, dec] }]
    })
    .fetchAll();

    return resources;
}

export default getSimilar;
export { getContainer, getNearby };

//     for (const item of resources) {
//     console.log(`${item.id_str}, ${item.SimilarityScore} `);
//     }
// }

// export default getContainer;
