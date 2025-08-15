// https://nextjs.org/docs/app/getting-started/server-and-client-components#passing-data-from-server-to-client-components

'use client'

import Image from "next/image"; 

export default function SearchView({ query, matches }: { query:SearchResult, matches: Array<SearchResult> }) {

    // console.log("query", query);
    console.log("matches", matches);

    return (
        <div>
        <h2>Search Query</h2>
        <Image src={query.image_url} alt={`Image for ${query.id}`} width={200} height={200} />
        <h2>Search Results</h2>
        <SearchResults matches={matches} />
        </div>
    );
    }

function SearchResults({ matches }: { matches: Array<SearchResult> }) {
    return (
        <ul>
        {matches.map(item => (
            <Image key={item.id} src={item.image_url} alt={`Image for ${item.id}`} width={200} height={200} />
        ))}
        </ul>
    );
}

// export default function SearchResults({ items }: { items: Array<SearchResult> }) {
//   return (
//     <ul>
//       {items.map(item => (
//         <li key={item.id}>
//           {item.id}: {item.image_url}
//         </li>
//       ))}
//     </ul>
//   );
// }