function showInputsI() {
    const iAmount = document.getElementById('iAmount').value;
    const ingredientCont = document.getElementById('ingredientCont');
    let ingredients = ingredientCont.children
    for (let x=0; x<ingredients.length; x++) {
        var iSingle = ingredients[x];
        if (parseInt(iSingle.id.slice(1,)) <= parseInt(iAmount)){
            iSingle.style.display = 'block';
            let inputChildren = iSingle.children;
            inputChildren[0].disabled = false;
            inputChildren[1].disabled = false;
            inputChildren[2].disabled = false;
        } else {
            iSingle.style.display = 'none';
            let inputChildren = iSingle.children;
            inputChildren[0].disabled = true;
            inputChildren[1].disabled = true;
            inputChildren[2].disabled = true;
        }
    }
}
function showInputsE() {
    const iAmount = document.getElementById('eAmount').value;
    const ingredientCont = document.getElementById('equipmentCont');
    let ingredients = ingredientCont.children
    for (let x=0; x<ingredients.length; x++) {
        var iSingle = ingredients[x];
        if (parseInt(iSingle.id.slice(1,)) <= parseInt(iAmount)){
            iSingle.style.display = 'block';
            let inputChildren = iSingle.children;
            inputChildren[0].disabled = false;
            inputChildren[1].disabled = false;
            inputChildren[2].disabled = false;
        } else {
            iSingle.style.display = 'none';
            let inputChildren = iSingle.children;
            inputChildren[0].disabled = true;
            inputChildren[1].disabled = true;
            inputChildren[2].disabled = true;
        }
    }
}