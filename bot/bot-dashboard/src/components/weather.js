import React, { useState } from 'react';
import axios from 'axios';

const Weather = () => {
    const [city, setCity] = useState('');
    const [weather, setWeather] = useState(null);

    const fetchWeather = async () => {
        console.log('fetchweather called');
        console.log('City:', city);
        console.log('API Key:', process.env.REACT_APP_OPENWEATHER_API_KEY); // Verificar que la clave API se esté cargando

        try {
            const response = await axios.get(`http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${process.env.REACT_APP_OPENWEATHER_API_KEY}&units=metric&lang=es`);
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


