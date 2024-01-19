function logDailySums() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var transactionsSheet = ss.getSheetByName('Projection 1'); // Change to your sheet name
  var lastRow = transactionsSheet.getLastRow();
  var transactionsData = transactionsSheet.getRange(2, 1, lastRow - 1, 10).getValues(); // Assuming data starts from row 2 and there are 10 columns

  var dailySums = {};

  for (var i = 0; i < transactionsData.length; i++) {
    var transaction = transactionsData[i];
    var date = transaction[6]; // Assuming 'Date' is in the 7th column (index 6)
    var value = transaction[9]; // Assuming 'Value' is in the 10th column (index 9)

    if (!date || isNaN(value)) {
      continue; // Skip rows with missing or invalid data
    }

    date = Utilities.formatDate(new Date(date), "GMT", "MM/dd/yyyy"); // Format date

    if (!dailySums[date]) {
      dailySums[date] = 0;
    }

    dailySums[date] += value;
  }

  // Combine and log the daily sums
  var combinedSums = "";
  for (var date in dailySums) {
    combinedSums += "Date: " + date + ", Total: " + dailySums[date] + "\n";
  }
  
  Logger.log(combinedSums);
}
