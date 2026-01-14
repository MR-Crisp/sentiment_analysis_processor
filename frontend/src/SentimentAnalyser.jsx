import react from 'react';

function SentimentAnalyser() {
    return (
        <>
            <title>Sentiment Analysis</title>
            <form>
    <textarea
        name="text"
        id="text"
        defaultValue={"Input your sentence to be analysed"}
    />
                <button type="submit">Submit</button>
            </form>

        </>

    );
}

export default SentimentAnalyser;