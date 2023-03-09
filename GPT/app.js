const axios = require("axios");

const promptInput = document.getElementById("prompt-input");
const outputDiv = document.getElementById("output");
const form = document.getElementById("prompt-form");

// Replace YOUR_API_KEY with your actual API key
const apiKey = "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";

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const prompt = promptInput.value.trim();
  if (!prompt) return;

  const apiUrl =
    "https://api.openai.com/v1/engines/text-davinci-003/completions";
  const apiParams = {
    prompt: prompt,
    max_tokens: 2048,
    temperature: 0.7,
  };
  const apiHeaders = {
    "Content-Type": "application/json",
    Authorization: `Bearer ${apiKey}`,
  };

  try {
    const apiResponse = await axios.post(apiUrl, apiParams, {
      headers: apiHeaders,
    });
    const generatedText = apiResponse.data.choices[0].text;
    outputDiv.innerText = generatedText;
  } catch (err) {
    console.error(err);
    outputDiv.innerText = "Error generating text";
  }
});
