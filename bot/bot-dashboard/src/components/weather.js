import React, { useState } from 'react';
import axios from 'axios';

const Weather = () => {
    const [city, setCity] = useState('');
    const [weather, setWeather] = useState(null);

    const fetchWeather = async () => {
        console.log('fetchWeather called');
        console.log('City:', city);

        try {
            const response = await axios.get(`http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=697ca98f2f789619c6573d094204b659&units=metric&lang=es`);
            console.log('API Response:', response.data);
            setWeather(response.data);
        } catch (error) {
            console.error('Error fetching weather:', error);
        }
    };

    return (
        <div>
            <input
                type="text"
                value={city}
                onChange={(e) => setCity(e.target.value)}
                placeholder="Ingresa una ciudad"
            />
            <button onClick={fetchWeather}>Obtener Clima</button>
            {weather && (
                <div>
                    <p>Temperatura: {weather.main.temp}°C</p>
                    <p>Descripción: {weather.weather[0].description}</p>
                </div>
            )}
        </div>
    );
};

export default Weather;

