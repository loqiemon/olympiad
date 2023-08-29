
const formInputs = document.querySelectorAll('.register__form-input');
const registerButton = document.querySelector('.register__submit');

function validatePhoneNumber(input) {
    const phoneNumber = input.value.replace(/\D/g, '');
    if (phoneNumber.length !== 11) {
        input.style.borderColor = 'red';
        return false;
    } else {
        input.style.borderColor = '';
        return true;
    }
}


function validateTextFields(input) {
    if (input.value.length < 5) {
        input.style.borderColor = 'red';
        return false;
    } else {
        input.style.borderColor = '';
        return true;
    }
}


function validateForm() {
    let isValid = true

    formInputs.forEach(input => {
        if (input.name === 'phone_number') {
            if (validatePhoneNumber(input) === false) isValid=false;
        } else {
            if (validateTextFields(input) === false) isValid=false;
        }
    });

    return isValid
}

formInputs.forEach(input => {
    input.addEventListener('input', function () {
        if (input.name === 'phone_number') {
            validatePhoneNumber(input);
        } else {
            validateTextFields(input);
        }
    });
});

registerButton.addEventListener('click', (e) => {
    if (validateForm() === false) e.preventDefault()
})
