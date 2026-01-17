const addElementBtn = document.getElementById("addElementId");
const cardsWrapper = document.getElementById("cardsWrapperId");

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

  const deleteBtn = document.createElement("a");
  deleteBtn.textContent = "Удалить";
  deleteBtn.classList.add("btn", "btn-danger");

  //TODO то что внутри
  cardBody.appendChild(cardTitle);
  cardBody.appendChild(cardText);



  cardBlock.appendChild(cardBody);

  cardBody.appendChild(editBtn);
  cardBody.appendChild(deleteBtn);
  cardsWrapper.appendChild(cardBlock);
};
addElementBtn.addEventListener("click", addElementFunc);
