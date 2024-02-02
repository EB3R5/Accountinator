function calculateDailyBalance() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var transactionsSheet = ss.getSheetByName('Projection 1');
  var dailyBalanceSheet = ss.getSheetByName('Sheet11');
  
  var lastRow = transactionsSheet.getLastRow();
  var transactionsData = transactionsSheet.getRange(2, 1, lastRow - 1, 7).getValues(); // Assuming data starts from row 2

  var balanceData = [];
  var dateToBalance = {};
  var balance = 0;

  for (var i = 0; i < transactionsData.length; i++) {
    var transaction = transactionsData[i];
    var date = transaction[5]; // Assuming 'Date' is in the 6th column
    var value = transaction[6]; // Assuming 'Value' is in the 7th column

    if (!date || isNaN(value)) {
      continue; // Skip rows with missing or invalid data
    }

    date = Utilities.formatDate(new Date(date), "GMT", "MM/dd/yyyy"); // Format date

    if (!dateToBalance[date]) {
      dateToBalance[date] = 0;
    }

    balance += value;
    dateToBalance[date] += value;
  }

  for (var date in dateToBalance) {
    balance += dateToBalance[date];
    balanceData.push([date, balance]);
  }

  if (balanceData.length > 0) {
    dailyBalanceSheet.clear();
    dailyBalanceSheet.getRange(1, 1, balanceData.length, 2).setValues(balanceData);
  }
}
