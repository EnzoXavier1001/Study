## Fetch method
The fetch() method in JS is used to request to the server and load the information in the webpages. The request can be of any APIs that return the data of the format JSON or XML. This method returns a promise.

```node
function App() {
  useEffect(() => {
    fetch('https://site.com/")
    .then (response => response.json())
    .then (json => console.log(json));
  }, []);
}
```

<hr />

## Async/Await
It is the preferred way of fetching the data from an API as it enables us to remove our .then() callbacks and return asynchronously resolved data. In the async block, we can use Await function to wait for the promise.

```node
function App() {
  useEffect(() => {
    (async () => {
      try {
        const result = await axios.get('https://site.com/');
        console.log(result.data);
      } catch (error) {
        console.error(error);
      }
    })()
  })
```

<hr />

## Axios library
With Axios, we can easily send asynchronous HTTP requests to REST APIs &  perform create, read, update and delete operations. Axios can be imported in plain JavaScript or with any library accordingly.

```node
function App() {
  useEffect(() => {
    axios.get("https ://site.com")
    .then((response) = console.log(response.data));
  }, []);
}
```

<hr />

## Usage in the component
Import the useFetch hook and pass the URL of the API endpoint from where you want to fetch data. Now just like any React hook we can directly use our custom hook to fetch the data.

```node
import useFetch from "/useFetch";

const App = () => {
  const { isLoading, serverError, apidata } = usefetch('https://site.com');

  return (
    <div>
      <h2>API Data</h2>
      { isLoading && <span>Loading...</span> }
      { !isLoading && serverError ? (
        <span>Error in fetching data ...</span>
      ) : (
        <span>{JSON.stringify(apiData)}</span>
      )}
    </div>
  )
}
```

<hr />

## React Query Library
With this we can achieve a lot more than just fetching data. It provides support for caching and refetching, which impacts the overall user experience by preventing irregularities and ensuring our app feels faster.

```node
import axios from "axios'
import { useQuery } from 'react-query'

function App() {
  const { isLoading, error, data } = 
  useQuery('posts', () => axios('https ://site.com'));
  console.log (data);
}
```