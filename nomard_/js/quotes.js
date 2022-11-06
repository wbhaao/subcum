const quotes = [
    {
        quote: "속도를 줄이고 인생을 즐겨라",
        anthor: "engoo"
    },
    {
        quote: "안하는 것보다 늦게 하는게 낫다",
        anthor: "pinter"
    },
    {
        quote: "최악의 선택은 아무것도 선택하지 못하는 것이다",
        anthor: "mark"
    },
    {
        quote: "잘 살아라, 그게 최고의 복수다",
        anthor: "juckerberg"
    },
 
]

const quote = document.querySelector('#quote span:first-child')
const anthor = document.querySelector('#quote span:last-child')
const random_value = quotes[Math.floor(Math.random() * quotes.length)]
console.log(random_value)
console.log(quote)

quote.innerText = random_value.quote
anthor.innerText = random_value.anthor
