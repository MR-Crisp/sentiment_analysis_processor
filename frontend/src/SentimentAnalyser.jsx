import React, { useState } from 'react';
import axios from 'axios';

function SentimentAnalyser() {
    const [text, setText] = useState('');
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const analyseSentiment = async (e) => {
        e.preventDefault();

        if (!text.trim()) {
            setError('Please enter some text');
            return;
        }

        setLoading(true);
        setError(null);

        try {
            const response = await axios.post('http://localhost:5000/model', {
                text: text
            });

            setResult(response.data);
        } catch (err) {
            setError('Failed to analyse sentiment. Make sure the backend is running.');
            console.error('Error:', err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <>
            <title>Sentiment Analysis</title>
            <form onSubmit={analyseSentiment}>
                <textarea
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                    name="text"
                    id="text"
                    placeholder="Input your sentence to be analysed"
                />
                <button type="submit" disabled={loading}>
                    {loading ? 'Analysing...' : 'Submit'}
                </button>
            </form>

            {error && (
                <div style={{ color: 'red', margin: '20px' }}>
                    {error}
                </div>
            )}

            {result && (
                <div style={{ margin: '20px', padding: '20px', border: '2px solid #ff8200', borderRadius: '10px' }}>
                    <h2>Result:</h2>
                    <p><strong>Sentiment:</strong> {result.sentiment}</p>
                    <p><strong>Confidence:</strong> {(result.sentiment_val * 100).toFixed(1)}%</p>
                    <p><strong>Text analysed:</strong> "{result.text}"</p>
                </div>
            )}
        </>
    );
}

export default SentimentAnalyser;