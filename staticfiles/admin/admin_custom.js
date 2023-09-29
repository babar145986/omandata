function openPrintPreview(url) {
    // Open the URL in a new tab
    var printWindow = window.open(url, '_blank');

    // Wait for the new tab to load
    if (printWindow) {
        // Wait for the window to load
        printWindow.onload = function () {
            // Access the print window's document
            var printDoc = printWindow.document;

            // Define the print stylesheet with desired styles (e.g., A4 size, no margins, 55% scale, centering)
            var printStyles = `
                @page {
                    size: A4;
                    margin: 0;
                }
                body {
                    transform: scale(0.55); /* Set to 55% scale */
                    transform-origin: 0 0;
                    position: absolute;
                    left: 0;
                    top: 0;
                    width: 181mm; /* A4 width */
                    height: 257mm; /* A4 height */
                }
            `;

            // Create a <style> element and add the print styles
            var style = printDoc.createElement('style');
            style.textContent = printStyles;

            // Append the <style> element to the print window's <head>
            printDoc.head.appendChild(style);

            // Trigger the browser's native print dialog
            printWindow.print();
        };
    }
}
