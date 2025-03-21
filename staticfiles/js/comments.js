 // Update word count for comment
 function updateCommentWordCount() {
    const commentTextarea = document.getElementById('comment_textarea');
    const wordCountElement = document.getElementById('comment-word-count');
    const wordCount = commentTextarea.value.split(/\s+/).filter(Boolean).length;
    wordCountElement.textContent = `${wordCount} / 50 words`;
}


document.addEventListener("DOMContentLoaded", function() {
    // Scroll to the comments section after the page reloads
    if (window.location.hash === '#comments-section') {
        const commentsSection = document.getElementById('comments-section');
        if (commentsSection) {
            commentsSection.scrollIntoView({ behavior: 'smooth' });
        }
    }
});
