const addElementBtn = document.getElementById("addElementId");
const cardsWrapper = document.getElementById("cardsWrapperId");

// СОЗДАНИЕ ЭЛЕМЕНТА
const addElementFunc = function addElement() {
  const cardBlock = document.createElement("div");
  cardBlock.classList.add("card", "kub-card");

  const cardBody = document.createElement("div");
  cardBody.classList.add("card-body");

  const cardTitle = document.createElement("h5");
  cardTitle.textContent = "Special title treatment";
  cardTitle.classList.add("card-title");

  const cardText = document.createElement("p");
  cardText.textContent =
    "With supporting text below as a natural lead-in to additional content.";
  cardText.classList.add("card-text");

  const editBtn = document.createElement("a");
  editBtn.textContent = "Редактировать";
  editBtn.classList.add("btn", "btn-warning");
  editBtn.addEventListener("click", function() {
    const editMenu = document.createElement("div");
    const element_H = document.createElement("input");
    const element_P = document.createElement("input");
    const edit_apply_btn = document.createElement("button")
    edit_apply_btn.classList.add("btn", "btn-success");
    element_H.placeholder = ('Заголовок')
    element_P.placeholder = ('Текст')
    cardBody.appendChild(editMenu)
    editMenu.appendChild(element_H);
    editMenu.appendChild(element_P);
    cardBody.appendChild(edit_apply_btn);
  });

  const deleteBtn = document.createElement("button");
  deleteBtn.textContent = "Удалить";
  deleteBtn.classList.add("btn", "btn-danger");
  deleteBtn.addEventListener("click", function() {
    cardBlock.remove();
  });

  //TODO то что внутри

  cardBody.appendChild(cardTitle);
  cardBody.appendChild(cardText);


  cardBlock.appendChild(cardBody);

  cardBody.appendChild(editBtn);
  cardBody.appendChild(deleteBtn);
  cardsWrapper.appendChild(cardBlock);
};

addElementBtn.addEventListener("click", addElementFunc);
