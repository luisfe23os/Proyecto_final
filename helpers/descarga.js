document.getElementById('downloadButton').addEventListener('click', async () => {
    const pdfSelect = document.getElementById('pdfSelect');
    const selectedPdf = pdfSelect.value;
   
    if (selectedPdf) {
      const pdfUrl = `/Pdf/${selectedPdf}`;
   
      try {
        const response = await fetch(pdfUrl);
        const blob = await response.blob();
   
        // Crea un objeto URL para el Blob y crea un enlace de descarga.
        const blobUrl = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = blobUrl;
        a.download = selectedPdf;
   
        // Simula un clic en el enlace para iniciar la descarga y luego limpia el objeto URL.
        a.click();
        URL.revokeObjectURL(blobUrl);
      } catch (error) {
        console.error('Error al descargar el archivo:', error);
      }
    } else {
      alert('Por favor, selecciona un PDF antes de intentar descargar.');
    }
  });