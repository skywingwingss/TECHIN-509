const chess11 = document.querySelector('chess11');
chess11.addEventListener('click', function (){Move(chess11,0,0)});
const chess12 = document.querySelector('chess12');
chess12.addEventListener('click', function (){Move(chess12,0,1)});
const chess13 = document.querySelector('chess13');
chess13.addEventListener('click', function (){Move(chess13,0,2)});
const chess21 = document.querySelector('chess21');
chess21.addEventListener('click', function (){Move(chess21,1,0)});
const chess22 = document.querySelector('chess22');
chess22.addEventListener('click', function (){Move(chess22,1,1)});
const chess23 = document.querySelector('chess23');
chess23.addEventListener('click', function (){Move(chess23,1,2)});
const chess31 = document.querySelector('chess31');
chess31.addEventListener('click', function (){Move(chess31,2,0)});
const chess32 = document.querySelector('chess32');
chess32.addEventListener('click', function (){Move(chess32,2,1)});
const chess33 = document.querySelector('chess33');
chess33.addEventListener('click', function (){Move(chess33,2,2)});

const player = document.querySelector('playerchess');
const result=document.querySelector('result')
let gamecontinue=true

function Move(chess,x,y) {
    if ((!(chess.textContent==="X")) &&(!(chess.textContent==="O") )&&(gamecontinue)){
        chess.textContent=player.textContent;
        const xhr = new XMLHttpRequest();
        xhr.open("POST", '/play_move', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var json = JSON.parse(xhr.responseText);
                change_page(json);
            }
        };
        xhr.send(JSON.stringify({
            x: x,
            y: y
        }));
    }

}

function change_page(data){
    if(data["sta"]===" "){
        player.textContent=data["chess"];
    }
    else{
        result.textContent=data["sta"]
        document.getElementById("continue").style.display="block";
        gamecontinue=false
    }
    //player.textContent=data["sta"];
}