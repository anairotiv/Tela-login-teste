const form = document.querySelector('form');

console.log(form)
form.addEventListener('submit', (event) => {
  event.preventDefault();
  const name = document.querySelector('#name').value;
  const email = document.querySelector('#email').value;
  const phone = document.querySelector('#phone').value;

  console.log(name,email,phone);
  saveData(name, email, phone);
});

function saveData(name, email, phone) {
    fetch('http://127.0.0.1:5000/save_data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ name, email, phone })
    })
    .then(response => response.text())
    .then(message => alert(message))
    .catch(error => console.error(error));
  }
  