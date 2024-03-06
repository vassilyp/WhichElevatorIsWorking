const core = require('@actions/core');

console.log("Updating elevators!");

let left_lift = document.querySelector("#left-lift");
let right_left = document.querySelector("#right-lift");

if (core.getInput('elevator-left')) {
    console.log("Left elevator working!");
} else {
    console.log("Left elevator broken");
}

if (core.getInput('elevator-right')) {
    console.log("Right elevator working!");
} else {
    console.log("Right elevator broken");
}