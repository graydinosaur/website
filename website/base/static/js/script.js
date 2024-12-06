// Get references to the button and menu
const menuToggle = document.getElementById('menu-toggle');
const menu = document.getElementById('menu');

// Toggle the dropdown menu visibility when the button is clicked
menuToggle.addEventListener('click', () => {
    // Toggle the display property to show or hide the dropdown
    if (menu.style.display === 'none' || menu.style.display === '') {
        menu.style.display = 'block'; // Show the menu
    } else {
        menu.style.display = 'none'; // Hide the menu
    }
});
