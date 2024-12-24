const modal = document.getElementById('projectModal');
        const overlay = document.getElementById('modalOverlay');
        const closeModalButton = document.getElementById('closeModal');
        const modalTitle = document.getElementById('modalTitle');
        const modalBody = document.getElementById('modalBody');
        console.log('client-dashboard.js loaded');
        document.querySelectorAll('.view-project').forEach(button => {
            button.addEventListener('click', (event) => {
                const projectName = event.target.dataset.project;
                modalTitle.textContent = projectName;
                modalBody.innerHTML = '<p>Details for project: <strong>${projectName}</strong></p>';
                modal.style.display = 'block';
                overlay.style.display = 'block';
            });
        });

        closeModalButton.addEventListener('click', () => {
            modal.style.display = 'none';
            overlay.style.display = 'none';
        });

        overlay.addEventListener('click', () => {
            modal.style.display = 'none';
            overlay.style.display = 'none';
        });