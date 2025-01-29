import React from 'react';

const Layout = ({ children }) => {
  return (
    <div className="container">
      <header className="mb-4">
        <h1 className="display-4">MoreVid</h1>
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
          <ul className="navbar-nav">
            <li className="nav-item">
              <a className="nav-link" href="#">Home</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">About</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">Contact</a>
            </li>
          </ul>
        </nav>
      </header>
      <main>{children}</main>
      <footer className="mt-4">
        <p className="text-center">© 2025 MoreVid. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default Layout;