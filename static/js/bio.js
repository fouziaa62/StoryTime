// Description: This file contains the javascript functions for the bio page.
function updateBioWordCount() {
    let textArea = document.getElementById("profile_bio");
    let wordCountDisplay = document.getElementById("bio-word-count");
    let maxWords = 250;

    // Split the input text into words
    let words = textArea.value.trim().split(/\s+/);

    if (words.length > maxWords) {
        textArea.value = words.slice(0, maxWords).join(" ");
    }

    // Update word count display
    wordCountDisplay.innerText = words.length + " / " + maxWords + " words";
}
