function changeTree(){
    const treeList = JSON.parse(document.getElementById('treeList').dataset.treelist);
    const locationID = document.getElementById('locationID').dataset.locationid;
    const areaID = document.getElementById('areaID').dataset.areaid;
    console.log(document.getElementById('locationID').dataset.locationid);
    for(let i=0; i<treeList.length; i++) {
        let tree = treeList[i];
        document.getElementById(tree).innerHTML = `<a href='../../treeData/${locationID}/${areaID}/${tree}'><div id="treeDiv" class="">${tree} - tree</div></a>`
    }
}
changeTree();