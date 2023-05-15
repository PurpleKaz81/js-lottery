window.addEventListener("DOMContentLoaded", () => {
  fetch('/api/numbers')
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    if (data && Array.isArray(data)) {
      let numbers = data.join(' || ');
      document.getElementById('header').textContent = numbers;
    } else {
      console.error('Received data is not an array:', data);
    }
  })
  .catch(error => {
    console.error('There was an error fetching the numbers:', error);
  });

})
