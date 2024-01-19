// Code in separate .gs files
// File: Helpers.gs
function getTransactionsData() {
  // Code to get transactions data
}

function calculateBalance() {
  // Code to calculate balance
}

function updateDailyBalanceSheet() {
  // Code to update the 'Daily Balance' sheet
}

// Main script
// File: MainScript.gs
function calculateDailyBalance() {
  var transactionsData = getTransactionsData();
  var balanceData = calculateBalance(transactionsData);
  updateDailyBalanceSheet(balanceData);
}
