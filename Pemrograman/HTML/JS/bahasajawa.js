const aksaraWyanjana= [
  'ꦲ', 'ꦤ', 'ꦕ', 'ꦫ', 'ꦏ',
  'ꦢ', 'ꦠ', 'ꦱ', 'ꦮ', 'ꦭ',
  'ꦥ', 'ꦣ', 'ꦗ', 'ꦪ', 'ꦚ',
  'ꦩ', 'ꦒ', 'ꦧ', 'ꦛ', 'ꦔ'
];

const labelWyanjana = [
  'ha', 'na', 'ca', 'ra', 'ka',
  'da', 'ta', 'tha', 'la', 'pa',
  'dha', 'ja', 'ya', 'nya', 'ma',
  'ga', 'ba', 'tha', 'dha', 'nga'
];

const pasangan = [
  '꧀ꦲ', '꧀ꦤ', '꧀ꦕ', '꧀ꦫ', '꧀ꦏ',
  '꧀ꦢ', '꧀ꦠ', '꧀ꦱ', '꧀ꦮ', '꧀ꦭ',
  '꧀ꦥ', '꧀ꦝ', '꧀ꦗ', '꧀ꦪ', '꧀ꦚ',
  '꧀ꦒ', '꧀ꦧ', '꧀ꦛ', '꧀ꦔ'
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

function randomAksara() {
  randomnum = Math.floor((Math.random()*allAksara.length)) 
  console.log(randomnum) 
  console.log(allAksara[randomnum])
  console.log(allLabel[randomnum])
  document.getElementById("aksara").innerHTML = allAksara[randomnum] 
  document.getElementById("label").innerHTML = allLabel[randomnum]
  hideAnswer()
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