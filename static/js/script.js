// Find the file input
const fileInput = document.getElementById("file");

// Find the text that displays the selected filename
const fileName = document.getElementById("file-name");


// Run this whenever the user selects a file
fileInput.addEventListener("change", function () {

    // Check whether a file was selected
    if (fileInput.files.length > 0) {

        // Get the selected file
        const selectedFile = fileInput.files[0];

        // Display its name
        fileName.textContent = selectedFile.name;

    } else {

        // If the user cancels the selection
        fileName.textContent = "No file selected";

    }

});
