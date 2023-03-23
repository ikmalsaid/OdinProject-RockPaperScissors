// set variables
let userChoice;
let userChoiceLower;
let cpuItems;
let cpuChoice;

// while true, convert choice to lowercase, compare value and break loop
while (true) {
  userChoice = prompt('Enter rock, paper, or scissors:');
  userChoiceLower = userChoice.toLowerCase();
  if (userChoiceLower === 'rock' || userChoiceLower === 'paper' || userChoiceLower === 'scissors') {
    break;
  }
}

// randomness processor
function getCpuChoice(items) { return items[Math.floor(Math.random()*items.length)]; }

// array of cpu choices
cpuItems = ['rock', 'paper', 'scissors'];

// after break, display values via console
console.log('User entered: ', userChoiceLower);
console.log('CPU entered: ', getCpuChoice(cpuItems));

// game mechanics

function gameResult(player, cpu){
	if (player === 'rock' || player === 'scissors' && cpu === 'paper') { return 'player wins!'; }
	else if (player === 'paper' && cpu === 'rock' || cpu === 'scissors') { return 'cpu wins!'; }
	else { return 'both tied!'; }
}

// game result
console.log('Result: ', gameResult(userChoiceLower, getCpuChoice(cpuItems)));



