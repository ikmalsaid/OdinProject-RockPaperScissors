// Function to generate computer choice
function getComputerChoice() {
  const choices = ['rock', 'paper', 'scissors'];
  return choices[Math.floor(Math.random() * 3)];
}

// Function to play a single round
function playRound(playerSelection, computerSelection) {
  // Check if player selection is valid
  if (!['rock', 'paper', 'scissors'].includes(playerSelection.toLowerCase())) {
    return "Invalid input. Please choose 'rock', 'paper', or 'scissors'.";
  }

  playerSelection = playerSelection.toLowerCase();
  if (playerSelection === computerSelection) {
    return `It's a tie! You both chose ${playerSelection}.`;
  } else if (
    (playerSelection === 'rock' && computerSelection === 'scissors') ||
    (playerSelection === 'paper' && computerSelection === 'rock') ||
    (playerSelection === 'scissors' && computerSelection === 'paper')
  ) {
    return `You win! ${playerSelection} beats ${computerSelection}.`;
  } else {
    return `You lose! ${computerSelection} beats ${playerSelection}.`;
  }
}

// Main game function
function game() {
  let playerScore = 0;
  let computerScore = 0;

  for (let i = 0; i < 5; i++) {
    const playerSelection = prompt(`Round ${i + 1} - Choose rock, paper or scissors`);
    const computerSelection = getComputerChoice();
    const roundResult = playRound(playerSelection, computerSelection);
    console.log(roundResult);

    if (roundResult.startsWith('You win')) {
      playerScore++;
    } else if (roundResult.startsWith('You lose')) {
      computerScore++;
    }
  }

  console.log('Game over!');
  if (playerScore > computerScore) {
    console.log(`You won the game! Final score: ${playerScore} - ${computerScore}`);
  } else if (playerScore < computerScore) {
    console.log(`You lost the game! Final score: ${playerScore} - ${computerScore}`);
  } else {
    console.log(`It's a tie game! Final score: ${playerScore} - ${computerScore}`);
  }
}

// Call the game function to play the game
game();