$(document).ready(function() {
    const csrfToken = $('input[name=csrfmiddlewaretoken]').val();
    console.log(csrfToken);

    $('#add').click(function() {
        calculate('add');
    });
    $('#subtract').click(function() {
        calculate('subtract');
    });
    $('#multiply').click(function() {
        calculate('multiply');
    });
    $('#divide').click(function() {
        calculate('divide');
    });

    function calculate(operation) {
        const numberA = $('#numberA').val();
        const numberB = $('#numberB').val();
        const data = {
        A: parseFloat(numberA),
        B: parseFloat(numberB)
    };
        console.log(numberA, numberB)
        $.ajax({
            url: `/api/${operation}/`,
            method: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json',
            headers: {
                'X-CSRFToken': csrfToken
            },
            success: function (response) {
                console.log(response);
                $('#result').text('Result: ' + response.result);
                $('#result').css('color', 'green');
            },
            error: function (error) {
                console.error(error);
                $('#result').text('Ошибка: ' + error.responseJSON.error);
                $('#result').css('color', 'red');
            }
        });
    }
});
