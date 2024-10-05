import { useState, FormEvent } from 'react';
import axios from 'axios';

const Login = () => {

  const [userName, setUserName] = useState('');
  const [password, setPassword] = useState('');

  function handleSubmit(evt: FormEvent) {
    evt.preventDefault();

    const payload = {
      userName,
      password
    };

    axios.post('/api/users/login', payload)
      .then(response => {
        console.log('User login successful.', response.data);

        setUserName('');
        setPassword('');

      })
      .catch(error => {
        console.log('Error logging in user', error);
        alert("Error logging in user.  Please try again.  If the problem persists, please contact support.")
      })
  }

  return (
    <>
      <form onSubmit={handleSubmit}>

      <label htmlFor="user_name">Display Name</label>
        <input type="text" name="user_name" placeholder="secure👍🏻user_01" required value={userName} onChange={(e) => setUserName(e.target.value)} />

        <label htmlFor="password">Password</label>
        <input type="password" name="password" placeholder="l*O9l(lnF56So^O" required autoComplete="new-password" value={password} onChange={(e) => setPassword(e.target.value)} />

        <button type="submit">Register</button>
      </form>
    </>
  );
};

export default Login;
