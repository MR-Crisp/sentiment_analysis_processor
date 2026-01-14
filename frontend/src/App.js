import react from "react";
import "./App.css";
import SentimentAnalyser from "./SentimentAnalyser";

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1>Sentiment Analysis Tool</h1>
                <p>Analyse the sentiment of any text using my rudimentary model</p>
            </header>
            <SentimentAnalyser />
            <footer>
                <p className="footer-line">Developed by Aamir Amin</p>
            </footer>
        </div>
    )
}

export default App;