  document.addEventListener('DOMContentLoaded', function () {
            const textarea = document.getElementById('autoExpand');
            const charCountDisplay = document.getElementById('charCount');
            const charLimit = 150;

            textarea.addEventListener('input', function() {
                let charCount = textarea.value.length;
                charCountDisplay.textContent = `Characters: ${charCount} / ${charLimit}`;

                if (charCount > charLimit) {
                    charCountDisplay.classList.remove('char-limit');
                    charCountDisplay.classList.add('char-limit-exceeded');
                } else {
                    charCountDisplay.classList.remove('char-limit-exceeded');
                    charCountDisplay.classList.add('char-limit');
                }
            });
        });



  const textArea = document.getElementById("autoExpand");

  textArea.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
      event.preventDefault(); // stops new line
      myFunction();
    }
  });

  function myFunction() {
    console.log("Enter pressed!");
    main()
  }
