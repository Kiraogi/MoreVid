import React, { useState, useEffect } from "react";
import Layout from "./Layout";
import axios from "axios";

const UserManagement = () => {
    const [users, setUsers] = useState([]);
    const [newUser, setNewUser] = useState({ username: '', email: '', password: '' });
  
    useEffect(() => {
      fetchUsers();
    }, []);
  
    const fetchUsers = async () => {
      try {
        const response = await axios.get('/api/users');
        setUsers(response.data);
      } catch (error) {
        console.error('Ошибка при получении пользователей:', error);
      }
    };
  
    const handleInputChange = (e) => {
      setNewUser({ ...newUser, [e.target.name]: e.target.value });
    };
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      try {
        await axios.post('/api/register', newUser);
        setNewUser({ username: '', email: '', password: '' });
        fetchUsers();
      } catch (error) {
        console.error('Ошибка при создании пользователя:', error);
      }
    };
  
    return (
      <Layout>
        <div className="container">
          <h2 className="mb-4">Управление пользователями</h2>
          <form onSubmit={handleSubmit} className="mb-4">
            <div className="mb-3">
              <input
                type="text"
                className="form-control"
                name="username"
                value={newUser.username}
                onChange={handleInputChange}
                placeholder="Имя пользователя"
                required
              />
            </div>
            <div className="mb-3">
              <input
                type="email"
                className="form-control"
                name="email"
                value={newUser.email}
                onChange={handleInputChange}
                placeholder="Email"
                required
              />
            </div>
            <div className="mb-3">
              <input
                type="password"
                className="form-control"
                name="password"
                value={newUser.password}
                onChange={handleInputChange}
                placeholder="Пароль"
                required
              />
            </div>
            <button type="submit" className="btn btn-primary">Создать пользователя</button>
          </form>
          <h3>Список пользователей</h3>
          <ul className="list-group">
            {users.map((user) => (
              <li key={user.id} className="list-group-item">{user.username} - {user.email}</li>
            ))}
          </ul>
        </div>
      </Layout>
    );
  };
  
  export default UserManagement;
  