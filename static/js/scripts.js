document.addEventListener('DOMContentLoaded', function() {
    const lessonContent = document.getElementById('lesson-content');

    fetch('/api/lessons')
        .then(response => response.json())
        .then(data => {
            data.lessons.forEach(lesson => {
                const lessonDiv = document.createElement('div');
                lessonDiv.classList.add('lesson');
                lessonDiv.innerHTML = `<h3>${lesson.title}</h3><p>${lesson.content}</p>`;
                lessonContent.appendChild(lessonDiv);
            });
        })
        .catch(error => console.error('Error fetching lessons:', error));
});
