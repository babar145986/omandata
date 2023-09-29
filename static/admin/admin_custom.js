function openPrintPreview(url) {
    // Open the URL in a new window or tab
    var printWindow = window.open(url, 'Print Preview', 'width=800,height=600');
  
    // Trigger print preview in the new window
    if (printWindow) {
        printWindow.onload = function () {
            printWindow.print();
        };
    }
  }
  