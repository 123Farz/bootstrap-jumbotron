
function clearScreen() {
document.getElementById("result").value = "";
}

function setScreenValue(value) {
const resultElement = document.getElementById("result");
if (resultElement.value === "" && isNaN(value) && value !== ".") return;

resultElement.value += value;
}

function calculateResult() {
const resultElement = document.getElementById("result");
const expression = resultElement.value.trim();

if (expression === "") {
return;
}

try {
const total = eval(expression);
resultElement.value = Number.isFinite(total) ? total : "Error";
} catch (e) {
resultElement.value = "Error";
setTimeout(clearScreen, 1500);
}
}