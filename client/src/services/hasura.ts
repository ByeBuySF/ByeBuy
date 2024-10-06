import {
  ApolloClient,
  createHttpLink,
  InMemoryCache
} from '@apollo/client';

const client = new ApolloClient({
  ssrMode: true,
  link: createHttpLink({
    uri: 'https://tomegg-dev.hasura.app/v1/graphql',
    credentials: 'same-origin',
    headers: {
      'x-hasura-admin-secret': `ZND2I4URtoMPqwUmNe0GrrTC40M14ajwCLP9VWaCNpa2y0SHBWTX3s72blEiw67g`,
    },
  }),
  cache: new InMemoryCache(),
});
export default client;