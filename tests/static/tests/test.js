let charList = wordList.join(" ").split("")
let currentCharIndex = 0
let charHistory = []
let letterElements = []
let timerElement = null
let timer = null
let initialTime = 30
let currentTime = null
let startTime = null
let mistakes = 0

function startTimer() {
    currentTime = initialTime
    timerElement = document.getElementById("timer")
    timerElement.innerText = currentTime
    timer = setInterval(tick, 1000)
    startTime = Date.now()
}

function tick() {
    currentTime--
    timerElement.innerText = currentTime
    if (currentTime == 0) {
        clearInterval(timer)
        // TODO: time's up logic
    }
}

function handleKeyboardInput(element, event) {
    // TODO: logic, exclusions
}

function compareCharacter(char) {
    let letterElement = letterElements[currentCharIndex]

    letterElement.classList.remove("text-muted")

    if (char !== charList[currentCharIndex]) {
        letterElement.classList.add("text-danger", "text-decoration-underline")
        letterElement.innerText = char
        mistakes++
    }

    charHistory.push(char)
    currentCharIndex++
}

function backspace() {
    currentCharIndex--
    let letterElement = letterElements[currentCharIndex]
    letterElement.classList.remove("text-danger, text-decoration-underline")
    letterElement.classList.add("text-muted")
    letterElement.innerText = charList[currentCharIndex]
    charHistory.pop()
}

function calculateWpm() {
    let wordHistory = charHistory.join("").split(" ")
    let correctWords = 0
    for (let i = 0; i < wordHistory.length; i++) {
        if (wordHistory[i] === wordList[i]) {
            correctWords++
        }
    }
    return correctWords * (60 / initialTime)
}

function calculateAccuracy() {
    let correctChars = 0
    for (let i = 0; i < charHistory.length; i++) {
        if (charHistory[i] === charList[i]) {
            correctChars++
        }
    }
    return (correctChars / charHistory.length) * 100
}

window.addEventListener("load", (event) => {
    letterElements = document.getElementsByClassName("letter")
    //document.getElementById("words").addEventListener("keydown", handleKeyboardInput)
})