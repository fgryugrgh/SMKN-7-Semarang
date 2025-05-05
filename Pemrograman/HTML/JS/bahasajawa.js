const aksaraWyanjana= [
  'ꦲ', 'ꦤ', 'ꦕ', 'ꦫ', 'ꦏ',
  'ꦢ', 'ꦠ', 'ꦱ', 'ꦮ', 'ꦭ',
  'ꦥ', 'ꦣ', 'ꦗ', 'ꦪ', 'ꦚ',
  'ꦩ', 'ꦒ', 'ꦧ', 'ꦛ', 'ꦔ'
];

const labelWyanjana = [
  'ha', 'na', 'ca', 'ra', 'ka',
  'da', 'ta', 'sa', 'wa', 'la',
  'pa', 'dha', 'ja', 'ya', 'nya',
  'ma', 'ga', 'ba', 'tha', 'nga'
];

const pasangan = [
  '꧀ꦲ', '꧀ꦤ', '꧀ꦕ', '꧀ꦫ', '꧀ꦏ',
  '꧀ꦢ', '꧀ꦠ', '꧀ꦱ', '꧀ꦮ', '꧀ꦭ',
  '꧀ꦥ', '꧀ꦝ', '꧀ꦗ', '꧀ꦪ', '꧀ꦚ',
  '꧀ꦩ', '꧀ꦒ', '꧀ꦧ', '꧀ꦛ', '꧀ꦔ'
];

const sandhangan = [
  'ꦶ', // wulu (i)
  'ꦸ', // suku (u)
  'ꦺ', // taling (e)
  'ꦺꦴ', // taling tarung (o)
  'ꦼ', // pepet (ê)
  'ꦁ', // cecek (ng)
  'ꦂ', // layar (r)
  'ꦃ'  // wignyan (h)
];

const labelShandangan = ['i', 'u', 'e', 'o', 'ê', 'ng', 'r', 'h']

const labelPasangan = labelWyanjana

const allAksara = aksaraWyanjana.concat(pasangan, sandhangan)
const allLabel = labelWyanjana.concat(labelPasangan, labelShandangan)

let randomnum = 0
let numba = 0

function shuffle(arr1, arr2) {
    if (arr1.length !== arr2.length) {
        throw new Error("Arrays must be of the same length");
    }

    for (let i = arr1.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));

        // Swap in arr1
        [arr1[i], arr1[j]] = [arr1[j], arr1[i]];

        // Swap in arr2 (same index swap)
        [arr2[i], arr2[j]] = [arr2[j], arr2[i]];
    }
}

shuffle(allAksara, allLabel)

function randomAksara() {
  /*randomnum = Math.floor((Math.random()*allAksara.length)) 
  console.log(randomnum) 
  console.log(allAksara[randomnum])
  console.log(allLabel[randomnum])*/

  document.getElementById("aksara").innerHTML = allAksara[numba] 
  document.getElementById("label").innerHTML = allLabel[numba]
  document.getElementById("counter").innerHTML = numba
  hideAnswer()
  if (numba === allAksara.length - 1) {
    numba = 0
    shuffle(allAksara, allLabel)  
  } else {
      numba++
  }
}

function hide (elements) {
    elements.style.display = 'none';
}

function show (elements) {
    elements.style.display = 'block';
}
 
function hideAnswer() {
  show(document.getElementById('hider'))  
  hide(document.getElementById('label'))
}

function revealAnswer() {
  hide(document.getElementById('hider'))  
  show(document.getElementById('label'))
}

hide(document.getElementById('hider'))  
