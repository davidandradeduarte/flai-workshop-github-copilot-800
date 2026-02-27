import React from 'react';
import { Link } from 'react-router-dom';

const cards = [
  {
    title: 'Users',
    description: 'View and manage all registered users and their profiles.',
    path: '/users',
    icon: '👤',
  },
  {
    title: 'Activities',
    description: 'Log and track fitness activities for each user.',
    path: '/activities',
    icon: '🏃',
  },
  {
    title: 'Leaderboard',
    description: 'See the competitive rankings and scores across all users.',
    path: '/leaderboard',
    icon: '🏆',
  },
  {
    title: 'Teams',
    description: 'Browse and manage teams and their members.',
    path: '/teams',
    icon: '👥',
  },
  {
    title: 'Workouts',
    description: 'Explore personalized workout suggestions and exercise plans.',
    path: '/workouts',
    icon: '💪',
  },
];

const Home = () => {
  return (
    <div>
      <div className="text-center mb-5">
        <h1 className="display-5 fw-bold">Welcome to Octofit Tracker</h1>
        <p className="lead text-muted">Your superhero fitness companion. Track activities, compete with teammates, and crush your goals.</p>
      </div>
      <div className="row g-4 justify-content-center">
        {cards.map((card) => (
          <div className="col-sm-6 col-md-4" key={card.title}>
            <Link to={card.path} className="text-decoration-none">
              <div className="card h-100 shadow-sm border-0 home-card">
                <div className="card-body text-center p-4">
                  <div style={{ fontSize: '2.5rem' }}>{card.icon}</div>
                  <h5 className="card-title mt-2 fw-bold">{card.title}</h5>
                  <p className="card-text text-muted">{card.description}</p>
                </div>
              </div>
            </Link>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Home;
