function limitWords() {
    let textArea = document.getElementById("story_content");
    let wordCountDisplay = document.getElementById("word-count");
    let maxWords = 500;

    let words = textArea.value.trim().split(/\s+/);

    if (words.length > maxWords) {
        textArea.value = words.slice(0, maxWords).join(" ");
    }

    wordCountDisplay.innerText = words.length + " / " + maxWords + " words";
}