function initializeItemList(listId) {
    const itemList = document.getElementById(listId);

    itemList.addEventListener('click', (event) => {
        if (event.target.tagName === 'LI') {
            event.target.classList.toggle('selected');
        }
    });

    const form = document.getElementById('myForm');
    form.addEventListener('submit', (event) => {
        const selectedItems = Array.from(itemList.querySelectorAll('.selected'));
        const selectedValues = selectedItems.map((item) => item.dataset.value);

        const selectedInput = document.createElement('input');
        selectedInput.type = 'hidden';
        selectedInput.name = 'selected[]';
        selectedInput.value = selectedValues.join(',');

        form.appendChild(selectedInput);
    });
}

// Initialize for the first list
initializeItemList('itemList');

// Initialize for the second list
initializeItemList('itemList2');
initializeItemList('itemList3');
initializeItemList('itemList4');
