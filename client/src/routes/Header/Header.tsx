import { gql } from "@apollo/client";
import client from "../../services/hasura";
import NavBar from "./NavBar";

const Header = () => {
  
  const getTransactions = async () => {
    const { data } = await client.query({
      query: gql`
        query GetProducts {
  Product {
    id
    data
  }
}
`,
    });

    console.log(data)
  }

  getTransactions()

  return (
    <>
      <h3>Header</h3>
      <NavBar />
    </>
  );
};

export default Header;
