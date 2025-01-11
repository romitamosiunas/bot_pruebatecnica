import React from 'react';
import Weather from './components/weather';
import './css/App.css';

const app = () => {
    return (
        <div>
            <h1>DeltoBot Dashboard</h1>
            <Weather />
        </div>
    );
};

export default app;


