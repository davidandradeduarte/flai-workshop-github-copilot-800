import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  const [teams, setTeams] = useState([]);
  const [editingUser, setEditingUser] = useState(null);
  const [form, setForm] = useState({ username: '', name: '', email: '', team: '' });
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState('');

  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const apiUrl = codespace
    ? `https://${codespace}-8000.app.github.dev/api/users/`
    : 'http://localhost:8000/api/users/';
  const teamsUrl = codespace
    ? `https://${codespace}-8000.app.github.dev/api/teams/`
    : 'http://localhost:8000/api/teams/';
  const baseUrl = codespace
    ? `https://${codespace}-8000.app.github.dev`
    : 'http://localhost:8000';

  const fetchUsers = () => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => setUsers(data.results ? data.results : data));
  };

  useEffect(() => {
    fetchUsers();
    fetch(teamsUrl)
      .then(res => res.json())
      .then(data => setTeams(data.results ? data.results : data));
  }, [apiUrl, teamsUrl]);

  const openEdit = (user) => {
    setEditingUser(user);
    setForm({ username: user.username, name: user.name, email: user.email, team: user.team || '' });
    setError('');
  };

  const closeEdit = () => {
    setEditingUser(null);
    setError('');
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSave = () => {
    setSaving(true);
    setError('');
    fetch(`${baseUrl}/api/users/${editingUser.id}/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form),
    })
      .then(res => {
        if (!res.ok) return res.json().then(d => { throw new Error(JSON.stringify(d)); });
        return res.json();
      })
      .then(() => {
        setSaving(false);
        closeEdit();
        fetchUsers();
      })
      .catch(err => {
        setSaving(false);
        setError(err.message || 'Failed to save changes.');
      });
  };

  return (
    <div>
      <h2 className="mb-4">Users</h2>
      <div className="table-responsive">
        <table className="table table-striped table-bordered">
          <thead className="table-dark">
            <tr>
              <th>Username</th>
              <th>Name</th>
              <th>Email</th>
              <th>Team</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user, idx) => (
              <tr key={user.id || idx}>
                <td>{user.username}</td>
                <td>{user.name}</td>
                <td>{user.email}</td>
                <td>{user.team || <span className="text-muted">—</span>}</td>
                <td>
                  <button
                    className="btn btn-sm btn-outline-primary"
                    onClick={() => openEdit(user)}
                  >
                    Edit
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {editingUser && (
        <div className="modal d-block" style={{ backgroundColor: 'rgba(0,0,0,0.4)' }} tabIndex="-1">
          <div className="modal-dialog modal-dialog-centered">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">Edit User: {editingUser.username}</h5>
                <button type="button" className="btn-close" onClick={closeEdit}></button>
              </div>
              <div className="modal-body">
                {error && <div className="alert alert-danger py-2">{error}</div>}
                <div className="mb-3">
                  <label className="form-label fw-semibold">Username</label>
                  <input
                    type="text"
                    className="form-control"
                    name="username"
                    value={form.username}
                    onChange={handleChange}
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label fw-semibold">Name</label>
                  <input
                    type="text"
                    className="form-control"
                    name="name"
                    value={form.name}
                    onChange={handleChange}
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label fw-semibold">Email</label>
                  <input
                    type="email"
                    className="form-control"
                    name="email"
                    value={form.email}
                    onChange={handleChange}
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label fw-semibold">Team</label>
                  <select
                    className="form-select"
                    name="team"
                    value={form.team}
                    onChange={handleChange}
                  >
                    <option value="">— No Team —</option>
                    {teams.map((t, i) => (
                      <option key={t.id || i} value={t.name}>{t.name}</option>
                    ))}
                  </select>
                </div>
              </div>
              <div className="modal-footer">
                <button className="btn btn-secondary" onClick={closeEdit} disabled={saving}>Cancel</button>
                <button className="btn btn-primary" onClick={handleSave} disabled={saving}>
                  {saving ? 'Saving…' : 'Save Changes'}
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Users;
