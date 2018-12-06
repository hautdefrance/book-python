document.addEventListener("DOMContentLoaded", function (event) {

    let last_name = document.querySelector('#id_last_name');
    last_name.value = last_name.value.toUpperCase();

    last_name.addEventListener("focus", () => {
        last_name.value = last_name.value.toUpperCase();
    })

});
