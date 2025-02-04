import React, { useState } from "react";
import axios from "axios";

function App() {
    const [text, setText] = useState("");
    const [model, setModel] = useState("custom");
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);

    const analyzeSentiment = async () => {
        setLoading(true);
        try {
            const response = await axios.post("http://127.0.0.1:8000/analyze", {
                text,
                model
            });
            setResult(response.data);
        } catch (error) {
            console.error("Error:", error);
            setResult({ sentiment: "Error", confidence: 0 });
        }
        setLoading(false);
    };

    return (
        <div style={{ padding: "20px", textAlign: "center" }}>
            <h2>Sentiment Analysis</h2>
            <textarea
                rows="4"
                cols="50"
                placeholder="Enter text here..."
                value={text}
                onChange={(e) => setText(e.target.value)}
            />
            <br />
            <select onChange={(e) => setModel(e.target.value)} value={model}>
                <option value="custom">Custom Model</option>
                <option value="llama">LLaMA 3</option>
            </select>
            <br />
            <button onClick={analyzeSentiment} disabled={loading}>
                {loading ? "Analyzing..." : "Analyze Sentiment"}
            </button>
            {result && (
                <div>
                    <h3>Result:</h3>
                    <p><strong>Sentiment:</strong> {result.sentiment}</p>
                    <p><strong>Confidence:</strong> {result.confidence.toFixed(2)}</p>
                </div>
            )}
        </div>
    );
}

export default App;
